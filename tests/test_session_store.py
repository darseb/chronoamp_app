"""Unit tests for data.session_store (save_session / load_session)."""

from __future__ import annotations

import math
from datetime import datetime
from pathlib import Path

import pytest

from core.models import DataPoint, MeasurementConfig
from data.session_store import save_session, load_session
from interpretation.verdict import Verdict


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture()
def tmp_sessions(tmp_path: Path) -> Path:
    """Return a temporary directory to use as the sessions folder."""
    return tmp_path / "sessions"


@pytest.fixture()
def sample_config() -> MeasurementConfig:
    return MeasurementConfig(potential=0.25, run_time=10.0, interval_time=0.1)


@pytest.fixture()
def sample_points() -> list[DataPoint]:
    return [
        DataPoint(time=i * 0.1, current=1.2345 + i * 0.001)
        for i in range(50)
    ]


@pytest.fixture()
def sample_timestamp() -> datetime:
    return datetime(2025, 6, 15, 14, 30, 0)


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestSaveAndLoadRoundTrip:
    """save_session → load_session should reproduce every field."""

    def test_metadata_round_trips(
        self,
        tmp_sessions: Path,
        sample_config: MeasurementConfig,
        sample_points: list[DataPoint],
        sample_timestamp: datetime,
    ) -> None:
        path = save_session(
            config=sample_config,
            data_points=sample_points,
            verdict=Verdict.POSITIVE,
            explanation="Signal above threshold (1.234 µA ≥ -0.0001 µA).",
            timestamp=sample_timestamp,
            sessions_folder=tmp_sessions,
        )

        session = load_session(path)

        assert session.timestamp == sample_timestamp.isoformat()
        assert math.isclose(session.applied_potential, 0.25, rel_tol=1e-3)
        assert math.isclose(session.run_time, 10.0)
        assert session.verdict is Verdict.POSITIVE
        assert "above threshold" in session.explanation.lower()

    def test_data_points_round_trip(
        self,
        tmp_sessions: Path,
        sample_config: MeasurementConfig,
        sample_points: list[DataPoint],
        sample_timestamp: datetime,
    ) -> None:
        path = save_session(
            config=sample_config,
            data_points=sample_points,
            verdict=Verdict.NEGATIVE,
            explanation="Signal below threshold.",
            timestamp=sample_timestamp,
            sessions_folder=tmp_sessions,
        )

        session = load_session(path)

        assert len(session.data_points) == len(sample_points)
        for original, loaded in zip(sample_points, session.data_points):
            assert math.isclose(loaded.time, original.time, abs_tol=1e-3)
            assert math.isclose(loaded.current, original.current, abs_tol=1e-5)


class TestFilenamePattern:
    """CSV file should be named {timestamp}_{verdict}.csv."""

    @pytest.mark.parametrize("verdict", [Verdict.POSITIVE, Verdict.NEGATIVE, Verdict.INCONCLUSIVE])
    def test_naming_pattern(
        self,
        tmp_sessions: Path,
        sample_config: MeasurementConfig,
        verdict: Verdict,
    ) -> None:
        ts = datetime(2025, 1, 2, 3, 4, 5)
        path = save_session(
            config=sample_config,
            data_points=[DataPoint(time=0.0, current=0.0)] * 10,
            verdict=verdict,
            explanation="test",
            timestamp=ts,
            sessions_folder=tmp_sessions,
        )

        expected_name = f"20250102T030405_{verdict.value}.csv"
        assert path.name == expected_name

    def test_file_actually_exists(
        self,
        tmp_sessions: Path,
        sample_config: MeasurementConfig,
    ) -> None:
        path = save_session(
            config=sample_config,
            data_points=[DataPoint(time=0.0, current=0.0)] * 10,
            verdict=Verdict.POSITIVE,
            explanation="test",
            timestamp=datetime(2025, 3, 4, 12, 0, 0),
            sessions_folder=tmp_sessions,
        )
        assert path.exists()
        assert path.stat().st_size > 0


class TestMetadataHeaderPreserved:
    """The metadata header written by save_session must survive load_session."""

    def test_all_metadata_keys_present(
        self,
        tmp_sessions: Path,
        sample_config: MeasurementConfig,
        sample_timestamp: datetime,
    ) -> None:
        explanation = "Noisy signal — inconclusive."
        path = save_session(
            config=sample_config,
            data_points=[DataPoint(time=0.0, current=0.0)] * 15,
            verdict=Verdict.INCONCLUSIVE,
            explanation=explanation,
            timestamp=sample_timestamp,
            sessions_folder=tmp_sessions,
        )

        session = load_session(path)

        # Every metadata field should be populated (non-empty).
        assert session.timestamp != ""
        assert session.applied_potential == pytest.approx(0.25, abs=1e-3)
        assert session.run_time == pytest.approx(10.0)
        assert session.verdict is Verdict.INCONCLUSIVE
        assert session.explanation == explanation


class TestLoadNonexistent:
    """load_session should raise FileNotFoundError for missing files."""

    def test_raises(self, tmp_path: Path) -> None:
        with pytest.raises(FileNotFoundError):
            load_session(tmp_path / "does_not_exist.csv")
