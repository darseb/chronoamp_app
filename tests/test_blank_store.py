"""Unit tests for interpretation.blank_store — blank measurement storage."""

from __future__ import annotations

import json

import pytest

from interpretation.blank_store import BlankStats, BlankStore


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

@pytest.fixture
def tmp_blank_path(tmp_path):
    """Return a temporary path for blanks.json."""
    return tmp_path / "blanks.json"


# ---------------------------------------------------------------------------
# BlankStore basics
# ---------------------------------------------------------------------------

class TestBlankStore:
    def test_starts_empty(self, tmp_blank_path) -> None:
        store = BlankStore(path=tmp_blank_path)
        assert store.count == 0
        assert store.get_stats() is None

    def test_add_blank_increments_count(self, tmp_blank_path) -> None:
        store = BlankStore(path=tmp_blank_path)
        store.add_blank(0.05)
        assert store.count == 1
        store.add_blank(0.06)
        assert store.count == 2

    def test_get_stats_returns_none_below_minimum(self, tmp_blank_path) -> None:
        store = BlankStore(path=tmp_blank_path)
        store.add_blank(0.05)
        store.add_blank(0.06)
        # Default MIN_BLANK_REPLICATES = 3, so 2 is not enough.
        assert store.get_stats() is None

    def test_get_stats_returns_valid_with_enough_blanks(self, tmp_blank_path) -> None:
        store = BlankStore(path=tmp_blank_path)
        values = [0.050, 0.055, 0.060, 0.048, 0.052]
        for v in values:
            store.add_blank(v)

        stats = store.get_stats()
        assert stats is not None
        assert stats.count == 5
        assert abs(stats.mean - sum(values) / len(values)) < 1e-10
        assert stats.stdev > 0
        # LoB = mean + 1.645 * stdev
        assert stats.lob > stats.mean

    def test_lob_formula(self, tmp_blank_path) -> None:
        """Verify LoB = mean + 1.645 × σ."""
        store = BlankStore(path=tmp_blank_path)
        for v in [1.0, 2.0, 3.0]:
            store.add_blank(v)
        stats = store.get_stats()
        assert stats is not None
        import statistics
        expected_mean = statistics.mean([1.0, 2.0, 3.0])
        expected_std = statistics.stdev([1.0, 2.0, 3.0])
        expected_lob = expected_mean + 1.645 * expected_std
        assert abs(stats.lob - expected_lob) < 1e-10

    def test_reset_clears_all(self, tmp_blank_path) -> None:
        store = BlankStore(path=tmp_blank_path)
        store.add_blank(0.05)
        store.add_blank(0.06)
        store.add_blank(0.07)
        assert store.count == 3

        store.reset()
        assert store.count == 0
        assert store.get_stats() is None
        assert not tmp_blank_path.exists()


# ---------------------------------------------------------------------------
# Persistence
# ---------------------------------------------------------------------------

class TestBlankStorePersistence:
    def test_persists_to_json(self, tmp_blank_path) -> None:
        store = BlankStore(path=tmp_blank_path)
        store.add_blank(0.05)
        store.add_blank(0.06)

        assert tmp_blank_path.exists()
        data = json.loads(tmp_blank_path.read_text())
        assert data["currents"] == [0.05, 0.06]

    def test_loads_on_init(self, tmp_blank_path) -> None:
        # Write some data.
        store1 = BlankStore(path=tmp_blank_path)
        store1.add_blank(0.10)
        store1.add_blank(0.20)
        store1.add_blank(0.30)

        # Create a new store from the same file.
        store2 = BlankStore(path=tmp_blank_path)
        assert store2.count == 3
        assert store2.currents == [0.10, 0.20, 0.30]

    def test_handles_corrupt_file(self, tmp_blank_path) -> None:
        tmp_blank_path.write_text("not valid json!!!")
        store = BlankStore(path=tmp_blank_path)
        assert store.count == 0


# ---------------------------------------------------------------------------
# Properties
# ---------------------------------------------------------------------------

class TestBlankStoreProperties:
    def test_has_enough(self, tmp_blank_path) -> None:
        store = BlankStore(path=tmp_blank_path)
        assert not store.has_enough
        for i in range(3):
            store.add_blank(float(i))
        assert store.has_enough

    def test_currents_returns_copy(self, tmp_blank_path) -> None:
        store = BlankStore(path=tmp_blank_path)
        store.add_blank(1.0)
        c = store.currents
        c.append(999.0)
        # Internal list should not be modified.
        assert store.count == 1
