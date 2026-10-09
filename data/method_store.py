"""Persist and retrieve Analytical Methods as JSON files.

Saved methods encode all calibration parameters, blank statistics,
and provenance data needed to interpret future measurements.
"""

from __future__ import annotations

import json
import logging
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from config.settings import METHODS_FOLDER
from data.importer_models import (
    CalibrationMeasurement,
    ImportedMeasurement,
    MeasurementRole,
    SignalMetric,
    SourceFileInfo,
)
from interpretation.blank_store import BlankStats
from interpretation.calibration import CalibrationResult
from interpretation.detection_limits import DetectionLimit
from interpretation.method import (
    AnalyticalMethod,
    MethodValidationResult,
    QualityConfig,
    ValidationCheck,
)
from interpretation.signal_extraction import PreprocessingConfig

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Data classes Serialization Helpers
# ---------------------------------------------------------------------------

def _serialize_method(method: AnalyticalMethod) -> dict[str, Any]:
    """Convert an AnalyticalMethod to a JSON-serializable dictionary."""
    d = asdict(method)
    
    # Handle Enums
    if hasattr(method.signal_metric, "value"):
        d["signal_metric"] = method.signal_metric.value
    else:
        d["signal_metric"] = str(method.signal_metric)
    
    # Handle PreprocessingConfig if it wasn't converted by asdict
    if hasattr(d.get("preprocessing_config"), "to_dict"):
        d["preprocessing_config"] = d["preprocessing_config"].to_dict()

    for m in d.get("source_measurements", []):
        if "role" in m and hasattr(m["role"], "value"):
            m["role"] = m["role"].value

    return d


def _deserialize_method(data: dict[str, Any]) -> AnalyticalMethod:
    """Convert a dictionary back into an AnalyticalMethod."""
    
    # Enum restoration
    data["signal_metric"] = SignalMetric(data["signal_metric"])
    
    for m in data.get("source_measurements", []):
        m["role"] = MeasurementRole(m["role"])
        # Reconstruct inner objects
        m["source"] = ImportedMeasurement(**m["source"])

    # Reconstruct source_measurements
    source_measurements = [CalibrationMeasurement(**m) for m in data.get("source_measurements", [])]
    data["source_measurements"] = source_measurements
    
    # Reconstruct source_files
    source_files = [SourceFileInfo(**sf) for sf in data.get("source_files", [])]
    data["source_files"] = source_files
    
    # Reconstruct complex attributes
    if data.get("preprocessing_config"):
        data["preprocessing_config"] = PreprocessingConfig.from_dict(data["preprocessing_config"])
    if data.get("quality_config"):
        data["quality_config"] = QualityConfig.from_dict(data["quality_config"])
    if data.get("blank_stats"):
        data["blank_stats"] = BlankStats(**data["blank_stats"])
    if data.get("calibration_result"):
        data["calibration_result"] = CalibrationResult(**data["calibration_result"])
        
    if data.get("lod"):
        data["lod"] = DetectionLimit(**data["lod"])
    if data.get("loq"):
        data["loq"] = DetectionLimit(**data["loq"])
        
    if data.get("calibration_range") is not None:
        data["calibration_range"] = tuple(data["calibration_range"])

    if data.get("validation"):
        checks = [ValidationCheck(**c) for c in data["validation"].get("checks", [])]
        data["validation"] = MethodValidationResult(checks=checks)
        
    # Drop unknown keys gracefully if schema evolved
    valid_keys = AnalyticalMethod.__dataclass_fields__.keys()
    filtered_data = {k: v for k, v in data.items() if k in valid_keys}
    
    method = AnalyticalMethod(**filtered_data)
    from interpretation.method import validate_method
    validate_method(method)
    return method


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

@dataclass
class MethodSummary:
    """A lightweight summary of a saved method for UI listing."""
    filename: str
    name: str
    version: str
    analyte: str
    status: str
    created_at: str
    
    @property
    def display_name(self) -> str:
        return f"{self.name} v{self.version} ({self.analyte})"


def save_method(
    method: AnalyticalMethod,
    methods_folder: str | Path | None = None,
) -> Path:
    """Save an AnalyticalMethod to a JSON file.

    The filename is derived from the method name and version.
    """
    folder = Path(methods_folder) if methods_folder else Path(METHODS_FOLDER)
    folder.mkdir(parents=True, exist_ok=True)

    safe_name = "".join(c if c.isalnum() else "_" for c in method.name)
    safe_version = "".join(c if c.isalnum() or c == "." else "_" for c in method.version)
    filename = f"{safe_name}_v{safe_version}.json".lower()
    filepath = folder / filename

    data = _serialize_method(method)
    
    with filepath.open("w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2)

    logger.info("Method saved: %s", filepath)
    return filepath.resolve()


def load_method(filepath: str | Path) -> AnalyticalMethod:
    """Load an AnalyticalMethod from a JSON file."""
    filepath = Path(filepath)
    if not filepath.exists():
        raise FileNotFoundError(f"Method file not found: {filepath}")

    with filepath.open("r", encoding="utf-8") as fh:
        data = json.load(fh)

    try:
        return _deserialize_method(data)
    except Exception as exc:
        raise ValueError(f"Failed to parse method file {filepath}: {exc}") from exc


def list_methods(methods_folder: str | Path | None = None) -> list[MethodSummary]:
    """List all saved methods in the methods directory."""
    folder = Path(methods_folder) if methods_folder else Path(METHODS_FOLDER)
    if not folder.exists():
        return []

    summaries: list[MethodSummary] = []
    
    for filepath in folder.glob("*.json"):
        try:
            with filepath.open("r", encoding="utf-8") as fh:
                data = json.load(fh)
                
            summaries.append(MethodSummary(
                filename=filepath.name,
                name=data.get("name", "Unnamed"),
                version=data.get("version", "1.0"),
                analyte=data.get("analyte", "Unknown"),
                status=data.get("status", "UNKNOWN"),
                created_at=data.get("created_at", ""),
            ))
        except Exception as exc:
            logger.warning("Failed to read method summary from %s: %s", filepath.name, exc)
            
    # Sort by creation date descending
    summaries.sort(key=lambda x: x.created_at, reverse=True)
    return summaries


def delete_method(filename: str, methods_folder: str | Path | None = None) -> None:
    """Delete a saved method file."""
    folder = Path(methods_folder) if methods_folder else Path(METHODS_FOLDER)
    filepath = folder / filename
    
    if filepath.exists():
        filepath.unlink()
        logger.info("Deleted method: %s", filepath)
    else:
        logger.warning("Attempted to delete non-existent method: %s", filepath)
