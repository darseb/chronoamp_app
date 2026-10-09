"""Load, validate, and expose application configuration (defaults, user overrides)."""

from __future__ import annotations

# -- Measurement defaults (hidden from the user) ----------------------------

#: Sampling interval between successive data points (seconds).
DEFAULT_INTERVAL_TIME: float = 0.1

#: Equilibration time before the measurement begins (seconds).
DEFAULT_EQUILIBRATION_TIME: float = 2.0

# -- User-visible defaults --------------------------------------------------

#: Default applied potential shown in the control panel (V).
DEFAULT_POTENTIAL: float = -0.015

#: Default measurement duration shown in the control panel (s).
DEFAULT_RUN_TIME: float = 200.0

#: Stabilized sampling time point (seconds) for signal extraction and calibration interpolation.
TARGET_SAMPLING_TIME_S: float = 185.0

# -- Verdict / interpretation defaults --------------------------------------

#: Fraction of the run (by data-point count) used as the "final window"
#: for computing the summary metric.  0.3 → last 30 %.
FINAL_WINDOW_PERCENTAGE: float = 0.3

#: Mean-current cutoff (µA) that separates POSITIVE from NEGATIVE.
#: Placeholder value — calibrate after real assay validation.
POSITIVE_CUTOFF_UA: float = -0.0001

#: If the standard deviation of the final-window current exceeds this
#: value (µA), the result is flagged as INCONCLUSIVE due to noise.
NOISE_THRESHOLD_UA: float = 5.0

#: Plausible current range (µA).  Values outside this window are
#: considered INCONCLUSIVE (sensor fault, open circuit, etc.).
PLAUSIBLE_CURRENT_MIN_UA: float = -1000.0
PLAUSIBLE_CURRENT_MAX_UA: float = 1000.0

# -- Module 1: Signal Preprocessing defaults --------------------------------

#: Seconds of initial data to discard (capacitive charging transient).
TRANSIENT_TRIM_SECONDS: float = 2.0

#: Hampel filter half-window size (number of neighbours on each side).
HAMPEL_WINDOW_SIZE: int = 3

#: Hampel filter threshold in multiples of Median Absolute Deviation.
HAMPEL_N_SIGMA: float = 3.0

#: Savitzky-Golay smoothing window length (must be odd).
SAVGOL_WINDOW_LENGTH: int = 11

#: Savitzky-Golay polynomial order.
SAVGOL_POLYORDER: int = 2

# -- Module 2: Blank Characterization defaults -------------------------------

#: Minimum number of blank replicates required for LOD calculation.
MIN_BLANK_REPLICATES: int = 3

#: Recommended number of blank replicates for robust statistics.
RECOMMENDED_BLANK_REPLICATES: int = 20

#: K-factor for Limit of Blank (1.645 → 95 % one-sided confidence).
LOB_K_FACTOR: float = 1.645

# -- Module 3: Calibration defaults -----------------------------------------

#: Minimum calibration points required to compute a regression.
MIN_CALIBRATION_POINTS: int = 3

#: Minimum acceptable R² for a calibration fit.
MIN_R_SQUARED: float = 0.99

# -- Module 4: Quality-Control defaults -------------------------------------

#: Maximum acceptable |dI/dt| (µA s⁻¹) for steady-state validation.
MAX_STEADY_STATE_SLOPE_UA_PER_S: float = 0.01

#: Maximum fractional drift between first and second half of the window.
MAX_DRIFT_FRACTION: float = 0.15

#: Minimum signal-to-noise ratio (IUPAC S/N = 3 standard).
MIN_SNR: float = 3.0

#: Maximum coefficient of variation (%) in the final window.
MAX_CV_PERCENT: float = 10.0

# -- Storage defaults -------------------------------------------------------

#: Directory where measurement session CSV files are saved.
SESSIONS_FOLDER: str = "./sessions"

#: Directory where analytical method JSON files are saved.
METHODS_FOLDER: str = "./methods"

# -- Display defaults -------------------------------------------------------

#: Whether concentration values are displayed in scientific notation by default.
DEFAULT_USE_SCIENTIFIC_NOTATION: bool = False

