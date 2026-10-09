"""Unit tests for data.method_store (save_method / load_method / list_methods / delete_method)."""

import pytest
from pathlib import Path
from data.method_store import save_method, load_method, list_methods, delete_method
from interpretation.method import AnalyticalMethod, QualityConfig
from interpretation.signal_extraction import PreprocessingConfig
from data.importer_models import SignalMetric, CalibrationMeasurement, ImportedMeasurement, MeasurementRole, SourceFileInfo


def test_save_and_load_method(tmp_path: Path):
    method = AnalyticalMethod(
        name="Test Method",
        version="1.0",
        analyte="Glucose",
        technique="Chronoamperometry",
        concentration_unit="mM",
        signal_metric=SignalMetric.MEAN_FINAL_WINDOW,
        preprocessing_config=PreprocessingConfig(
            trim_seconds=1.5,
            hampel_window=7,
            hampel_sigma=2.5,
            sg_window=9,
            sg_order=3,
            final_window_pct=15.0,
        ),
        quality_config=QualityConfig(min_snr=4.0),
    )

    filepath = save_method(method, methods_folder=tmp_path)
    assert filepath.exists()

    loaded = load_method(filepath)
    assert loaded.name == "Test Method"
    assert loaded.version == "1.0"
    assert loaded.analyte == "Glucose"
    assert loaded.signal_metric == SignalMetric.MEAN_FINAL_WINDOW
    assert isinstance(loaded.preprocessing_config, PreprocessingConfig)
    assert loaded.preprocessing_config.trim_seconds == 1.5
    assert loaded.preprocessing_config.hampel_window == 7
    assert loaded.preprocessing_config.hampel_sigma == 2.5
    assert loaded.preprocessing_config.sg_window == 9
    assert loaded.preprocessing_config.sg_order == 3
    assert loaded.preprocessing_config.final_window_pct == 15.0
    assert loaded.quality_config.min_snr == 4.0


def test_list_and_delete_method(tmp_path: Path):
    method = AnalyticalMethod(name="Method A", version="1.0", analyte="Uric Acid")
    filepath = save_method(method, methods_folder=tmp_path)

    summaries = list_methods(methods_folder=tmp_path)
    assert len(summaries) == 1
    assert summaries[0].name == "Method A"

    delete_method(filepath.name, methods_folder=tmp_path)
    summaries_after = list_methods(methods_folder=tmp_path)
    assert len(summaries_after) == 0
