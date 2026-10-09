# ChronoAmp — Complete UI Redesign

## Objective

Redesign the entire ChronoAmp user interface to look and feel like a **professional scientific electrochemistry instrument application**, inspired by the attached PalmSens/PSTrace interface.

The current ChronoAmp functionality is already working and must be preserved.

This is primarily a **visual and UX redesign**, not a rewrite of the acquisition, analytical, calibration, or measurement logic.

The new interface should feel like software used to operate a laboratory potentiostat rather than a generic modern desktop application.

The visual reference is the attached PalmSens/PSTrace screenshot.

### Most important visual requirement

**DO NOT use a dark UI.**

The entire application must use a **light theme**.

Do not use:

- black backgrounds
- dark navy backgrounds
- Catppuccin dark colors
- dark cards
- dark control panels
- dark graph backgrounds

The result should resemble professional scientific software with light grey/white surfaces, subtle blue accents, thin borders, and compact controls.

---

# 1. Design direction

Use the PalmSens/PSTrace screenshot as the primary visual inspiration.

The target aesthetic is:

```text
Professional
Scientific
Technical
Clean
Compact
Instrument-oriented
Data-dense
Light
Functional
```

Avoid making ChronoAmp look like:

```text
A consumer application
A marketing dashboard
A web landing page
A mobile app
A modern "card dashboard"
A dark IDE
```

The UI should feel appropriate for:

- electrochemistry laboratories
- biosensor development
- analytical chemistry
- research instrumentation
- university laboratories
- industrial R&D

---

# 2. Overall window structure

The current application is essentially a vertical stack:

```text
Method Panel
Result Banner
Session Toolbar
Live Plot
Control Panel
```

Redesign this into a more instrument-like workspace.

Use a **three-region layout** where appropriate:

```text
┌───────────────────────────────────────────────────────────────┐
│ Toolbar / Connection / Method Status                         │
├───────────────┬───────────────────────────────────────────────┤
│               │                                               │
│   Controls    │                  LIVE PLOT                    │
│               │                                               │
│ Connection    │                                               │
│ Method        │                                               │
│ Measurement   │                                               │
│ Parameters    │                                               │
│               │                                               │
│               ├───────────────────────────────────────────────┤
│               │ Result / Measurement information              │
├───────────────┴───────────────────────────────────────────────┤
│ Status / Session / Instrument information                      │
└───────────────────────────────────────────────────────────────┘
```

The exact proportions can be adjusted based on the actual widgets.

The graph should be the **dominant visual element**, similar to PSTrace.

Do not waste large amounts of space on decorative cards.

---

# 3. Color system

Create a consistent light scientific theme.

Use neutral light surfaces.

Suggested palette:

```text
Application background:
#F2F3F5

Primary panel:
#FFFFFF

Secondary panel:
#F7F8FA

Border:
#C9CDD2

Strong border:
#AEB4BB

Primary text:
#202428

Secondary text:
#5E666F

Disabled text:
#8A9198

Primary accent:
#2F6DAE

Accent hover:
#255B92

Accent light:
#EAF2FA

Success:
#2E8B57

Success light:
#EAF6EF

Warning:
#C58A00

Warning light:
#FFF6DE

Error:
#C0392B

Error light:
#FBEDEC
```

These colors are suggestions, not rigid requirements.

The important requirement is:

**Light surfaces + dark readable text + restrained blue scientific accent.**

Do not use excessive saturated colors.

---

# 4. Main window background

Replace the existing:

```text
#11111b
```

background entirely.

Use a light neutral application background.

The application should resemble a native Windows scientific application.

Avoid huge rounded floating cards.

Use:

- subtle 1 px borders
- small corner radii
- compact spacing
- traditional group boxes/panels
- clear section headers

The screenshot reference is closer to an instrument control application than a dashboard.

---

# 5. Top toolbar

Create a compact top toolbar resembling the PalmSens connection area.

The top section should contain:

```text
[Connection status] [Device selector] [Connect] [Disconnect]
```

and method state somewhere nearby:

```text
Method: IL-6 PEC v1.0
Status: ACTIVE
```

Example:

```text
┌──────────────────────────────────────────────────────────────────┐
│ Connection                                                       │
│ [Refresh] [PalmSens device ▼] [Connect] [Disconnect]            │
│                                                                  │
│ Active Method: IL-6 PEC v1.0   ● CALIBRATED                      │
└──────────────────────────────────────────────────────────────────┘
```

Do not turn these into oversized modern buttons.

Use compact controls similar to scientific instrument software.

---

# 6. Connection panel

The connection area should provide immediate visibility of:

```text
Device
Connection state
Available devices
Connect
Disconnect
Refresh
```

Use a clear status indicator:

```text
● Connected
● Disconnected
● Searching
```

Use color sparingly:

Connected = green indicator

Disconnected = neutral/red indicator

Searching = blue/orange indicator

Do not use large banners for normal connection state.

---

# 7. Analytical Method panel

The existing Method Panel is functionally correct and must remain.

Redesign it visually.

Currently it uses a dark rounded status bar with:

- badge
- title
- subtitle
- Load Method
- New Calibration
- Deactivate

as documented in the current UI description.

Transform it into a compact scientific configuration section.

Example:

```text
┌───────────────────────────────────────────────┐
│ ANALYTICAL METHOD                             │
│                                               │
│ ● ACTIVE                                      │
│ IL-6 PEC v1.0                                 │
│ IL-6   |   LOD 0.42 pg/mL   |   1–20 pg/mL   │
│                                               │
│ [Load Method] [New Calibration] [Deactivate] │
└───────────────────────────────────────────────┘
```

When no method is active:

```text
┌───────────────────────────────────────────────┐
│ ANALYTICAL METHOD                             │
│                                               │
│ ○ LEGACY MODE                                 │
│ No analytical method loaded                   │
│ Acquisition uses configured legacy thresholds │
│                                               │
│ [Load Method] [New Calibration]              │
└───────────────────────────────────────────────┘
```

Use a subtle status badge rather than a huge colored banner.

---

# 8. Measurement controls

Redesign the current Control Panel into a compact instrument-style control section.

The existing controls include:

- Applied potential
- Run time
- Start
- Stop
- Elapsed time

These must remain functional.

Use a form layout similar to scientific software:

```text
Measurement Parameters

Applied potential:   [ 0.000 ] V
Run time:            [ 10.0  ] s

[ Start Measurement ] [ Stop ]
```

Use standard Qt widgets.

Prefer:

- QDoubleSpinBox
- QComboBox
- QPushButton
- QGroupBox
- QLabel

Avoid huge custom cards.

---

# 9. Main plot

The graph must become the central element of the interface.

This is the most important visual area.

The current graph uses pyqtgraph/pglive and streams data through `DataConnector`; preserve this implementation.

Redesign the plot to resemble the PSTrace graph.

### Plot requirements

Use:

- white/light grey plot background
- thin grey axes
- light grid
- dark readable axis labels
- blue measurement trace
- clear scientific units
- minimal decoration

Example:

```text
                  Chronoamperometry

 Current (µA)
     ↑
     │
 1.0 │
     │       ╱───────
 0.5 │     ╱
     │   ╱
 0.0 ├──────────────────────────────→ Time (s)
     0       5       10       15
```

The plot should visually resemble the PalmSens screenshot rather than a dark plotting library theme.

Do not use:

- dark plot backgrounds
- neon traces
- excessive colors
- excessive rounded containers
- oversized title typography

---

# 10. Plot toolbar

Add a compact plot toolbar inspired by scientific software.

Potential controls:

```text
[Auto Range]
[Zoom]
[Pan]
[Reset View]
[Clear]
[Show Grid]
```

Only expose functionality that already exists or can be safely implemented.

Do not add fake controls.

The toolbar should look like a traditional scientific instrument toolbar: small icons/buttons, compact spacing, unobtrusive appearance.

---

# 11. Result area

The current Result Banner is visually too dashboard-like.

Keep the functionality but redesign it into a compact **measurement result panel**.

The current application supports:

- Positive
- Negative
- Inconclusive

with corresponding status information.

Instead of a huge colored banner, use something closer to:

```text
┌──────────────────────────────────────────────────────────┐
│ RESULT                                                   │
│                                                          │
│ ● POSITIVE                                               │
│                                                          │
│ Concentration: 6.42 pg/mL                               │
│ Signal: 0.421 µA                                        │
│ Method: IL-6 PEC v1.0                                   │
│ QC: PASS                                                 │
│                                                          │
│ Calibration status: Within range                        │
└──────────────────────────────────────────────────────────┘
```

For negative:

```text
● NEGATIVE
Signal below LOB
```

For inconclusive:

```text
● INCONCLUSIVE
Signal within grey zone
```

For above range:

```text
● POSITIVE
Above calibration range
```

Use a light status background with a subtle colored border.

Do not make the entire application turn red/green.

---

# 12. Result colors

Use color only to communicate analytical state.

### Positive

Light green background:

```text
#EAF6EF
```

Green accent:

```text
#2E8B57
```

### Negative

Neutral or very light red:

```text
#FBEDEC
```

Red accent:

```text
#C0392B
```

### Inconclusive

Light amber:

```text
#FFF6DE
```

Amber accent:

```text
#C58A00
```

The background must remain light.

Never use the current dark result backgrounds.

---

# 13. Session actions

The current application displays session actions after a measurement is saved:

- Record as Blank
- Add to Calibration
- Open File
- Open Folder
- Export to Excel

Keep these functions.

Instead of presenting them as a large dashboard row, create a compact toolbar:

```text
Saved: sample_001.csv

[Record as Blank]
[Add to Calibration]
[Open]
[Open Folder]
[Export Excel]
```

Use small standard buttons and separators.

---

# 14. Status bar

Add a proper bottom status bar.

It should show information such as:

```text
Connected: PalmSens EmStat
Method: IL-6 PEC v1.0
Status: Ready
Sampling: 10 Hz
```

During acquisition:

```text
Connected: PalmSens EmStat
Method: IL-6 PEC v1.0
Status: Measuring...
Elapsed: 7.4 s
```

At completion:

```text
Status: Measurement complete
```

This keeps important information visible without using large banners.

---

# 15. No-device state

The current application replaces the main interface with a "No potentiostat detected…" overlay when no device is available.

Keep this behavior, but redesign it.

Use a clean light panel:

```text
┌─────────────────────────────────────────────┐
│                                             │
│          Potentiostat not connected         │
│                                             │
│       Connect a PalmSens device to begin.   │
│                                             │
│              [ Refresh Devices ]            │
│                                             │
└─────────────────────────────────────────────┘
```

Do not use a huge red warning.

The absence of a device is an operational state, not an error that requires alarming visuals.

---

# 16. Import Wizard redesign

The Import Wizard is an important part of the new Analytical Method system.

Keep its functionality, but redesign it using the same light scientific UI language.

The wizard should use a traditional structure:

```text
Step 1 — Select Files
Step 2 — Assign Measurements
Step 3 — Assign Concentrations
Step 4 — Review Calibration
Step 5 — Save Method
```

Use a clean left-side or top progress indicator.

Example:

```text
1. Files     2. Assignment     3. Calibration     4. Save
   ●--------------○----------------○---------------○
```

The calibration preview should prominently display the scientific plot.

Do not turn the wizard into a giant colorful onboarding flow.

---

# 17. Settings and configuration

Use standard scientific application controls.

Where possible:

```text
QGroupBox
QFormLayout
QComboBox
QDoubleSpinBox
QCheckBox
QPushButton
QTableWidget
```

Avoid custom web-style controls unless necessary.

The UI should feel like Qt desktop software.

---

# 18. Typography

Use a clean Windows-compatible UI font.

Prioritize readability.

Suggested hierarchy:

```text
Application title:     16–18 px
Section title:         12–14 px bold
Field labels:          10–11 px
Normal text:           10–11 px
Secondary text:        9–10 px
Result value:          16–20 px
```

Do not use giant headings.

This is scientific software, so information density is desirable.

---

# 19. Borders and panels

Use subtle borders:

```text
1 px
#C9CDD2
```

Panel radius:

```text
3–6 px
```

Do NOT use:

```text
20 px
30 px
40 px
```

rounded containers.

The PalmSens reference has a traditional technical application aesthetic.

Match that visual language.

---

# 20. Spacing

Use compact spacing.

Suggested:

```text
Outer margin: 8–12 px
Section spacing: 6–10 px
Widget spacing: 4–8 px
Button padding: compact
```

Avoid large empty spaces.

The interface should maximize useful working area for the graph.

---

# 21. Resizing behavior

The application must remain usable when resized.

Prioritize:

1. plot
2. measurement controls
3. method information
4. result information

The plot should expand to use available space.

Do not use fixed absolute coordinates for the overall layout.

Use:

```text
QSplitter
QHBoxLayout
QVBoxLayout
QGridLayout
QFormLayout
```

where appropriate.

The window should work at approximately:

```text
1280 × 800
1920 × 1080
```

and remain usable at smaller desktop resolutions.

---

# 22. Preserve all existing functionality

This redesign must NOT break:

- PalmSens connection
- acquisition
- live plotting
- start/stop
- method loading
- method activation
- method deactivation
- calibration creation
- result interpretation
- session saving
- Excel export
- blank recording
- adding calibration points
- file opening
- folder opening
- existing legacy mode
- existing tests

Do not modify analytical calculations simply because UI code is being redesigned.

Do not modify the acquisition thread architecture.

Do not replace pyqtgraph/pglive unless there is an unavoidable technical reason.

---

# 23. Modernize the architecture only where appropriate

Refactor the UI carefully if necessary.

Maintain a clean separation:

```text
Core
    ↓
Measurement
    ↓
Analysis
    ↓
UI
```

Do not place analytical calculations inside Qt widgets.

The UI should consume data from the existing analytical layer.

---

# 24. Remove the existing dark theme completely

Search the project for the current Catppuccin styling and remove it from the main application.

In particular, replace references corresponding to:

```text
#11111b
#1e1e2e
#313244
#45475a
#cdd6f4
#89b4fa
#f38ba8
```

where they are currently used as the primary theme.

Do not simply invert the current colors.

Build a coherent new light theme.

---

# 25. Use a centralized light theme

Create a centralized stylesheet/theme configuration rather than scattering color literals throughout the code.

For example:

```text
ui/theme.py
```

or an appropriate existing theme mechanism.

Define semantic roles such as:

```python
WINDOW_BACKGROUND
PANEL_BACKGROUND
INPUT_BACKGROUND
BORDER
TEXT
TEXT_SECONDARY
ACCENT
SUCCESS
WARNING
ERROR
PLOT_BACKGROUND
GRID
```

This will make future visual changes easy.

Prefer semantic names over hard-coded color values.

---

# 26. Visual hierarchy

The hierarchy should be:

```text
                 MAIN PLOT
                    ↓
           Measurement controls
                    ↓
             Result / Analysis
                    ↓
             Method / status
                    ↓
              Session actions
```

The graph is the workspace.

The controls support the graph.

The analytical result supports the measurement.

Everything else should stay compact.

---

# 27. Target visual result

The final application should visually resemble a **light-theme PalmSens/PSTrace-inspired scientific workstation**:

```text
┌─────────────────────────────────────────────────────────────────┐
│ ChronoAmp                                                       │
│ Connection [Device ▼] [Connect] [Disconnect]                    │
├───────────────────┬─────────────────────────────────────────────┤
│ ANALYTICAL METHOD │                                             │
│ ● ACTIVE          │                                             │
│ IL-6 PEC v1.0     │              CHRONOAMPEROMETRY              │
│ LOD ...           │                                             │
│ [Load] [New]      │                                             │
│                   │                                             │
│ MEASUREMENT       │                                             │
│ Potential [0.00]  │                   LIVE PLOT                 │
│ Time      [10.0]  │                                             │
│                   │                                             │
│ [START] [STOP]    │                                             │
│                   │                                             │
│                   ├─────────────────────────────────────────────┤
│                   │ RESULT                                      │
│                   │ ● POSITIVE     6.42 pg/mL                  │
├───────────────────┴─────────────────────────────────────────────┤
│ Status: Connected | Method: IL-6 PEC v1.0 | Ready              │
└─────────────────────────────────────────────────────────────────┘
```

This is only a conceptual arrangement. Use the existing application's actual widgets and functionality when implementing.

---

# 28. Important: inspect before changing

Before modifying anything:

1. Inspect the current UI code.
2. Identify all existing widgets.
3. Identify existing signals/slots.
4. Identify which widgets are referenced by `main_window.py`.
5. Identify dependencies between UI and analytical logic.
6. Preserve those interfaces wherever possible.

Do not rewrite the application blindly.

---

# 29. Implementation strategy

Implement in phases:

### Phase 1 — Theme

Create the centralized light scientific theme.

### Phase 2 — Main window layout

Reorganize the existing widgets into the new instrument-style layout.

### Phase 3 — Plot

Restyle the pyqtgraph widget to use a light scientific plot appearance.

### Phase 4 — Method panel

Redesign the analytical method status/control area.

### Phase 5 — Measurement controls

Redesign the control panel.

### Phase 6 — Result

Redesign the result presentation.

### Phase 7 — Session toolbar

Redesign the post-measurement actions.

### Phase 8 — Import Wizard

Apply the same visual language to method creation/import.

### Phase 9 — Connection/no-device states

Redesign those states.

### Phase 10 — Responsive behavior

Test several window sizes.

---

# 30. Do not add unnecessary functionality

This task is primarily a visual/UX redesign.

Do not add:

- machine learning
- new analytical models
- new hardware features
- unrelated menus
- unnecessary dashboards
- decorative animations
- excessive icons
- unnecessary navigation systems

Focus on making the existing functionality **clearer, more professional, and easier to operate**.

---

# 31. Acceptance criteria

The redesign is complete only when:

- The entire application uses a light theme.
- No major UI background is dark.
- The main interface visually resembles scientific instrument software.
- The live plot is the dominant workspace.
- Controls are compact and organized.
- The interface resembles the PalmSens/PSTrace screenshot in spirit, without copying it exactly.
- The Analytical Method functionality remains fully accessible.
- Legacy mode remains accessible.
- Method loading remains accessible.
- Calibration creation remains accessible.
- Results remain easy to interpret.
- No existing acquisition functionality is broken.
- Existing tests continue passing.

Run the complete existing test suite after the redesign.

Also manually launch the application and inspect the UI at multiple resolutions.

At the end, provide:

```text
Files changed
Theme implementation
Layout changes
Widget changes
Plot changes
Responsive behavior
Tests passed
Known limitations
```

Most importantly:

**Build ChronoAmp as a professional light-theme scientific instrument application inspired by PalmSens/PSTrace — not as a generic modern dashboard.**