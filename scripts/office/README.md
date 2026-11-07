# OpenRGB office ambience 1.1-office.0.3.0

This package includes the native six-controller OpenRGB build and the adapted
OpenRGB-Ambient plugin. It captures the Windows main display's rendered Wallpaper
Engine wallpaper behind ordinary windows; maximized/fullscreen apps on that
display take priority. Apps on other displays do not take over. Main-display and
resolution changes refresh capture automatically, including when undocking to
the laptop. Connected lights retain their normalized maps; desk devices can stay
offline. Legacy saved DISPLAY names no longer pin capture to a disconnected LG.

Supported office controllers: H6609 (20 regions, perimeter 3/7/4/6), H8048 (left
10/right 10), Secretlab NL72S2 (48), Keychron Q6 HE ISO SRGBmods (109), Legion Pro
7 Gen 8 Spanish ISO (102 keys, 6 front sections, auxiliary), G502 X PLUS (8).

The manually launched lighting owner is headless: no tray or startup task. It
binds the SDK only to 127.0.0.1:6742. Keep SignalRGB, G HUB's user processes and
other RGB writers closed. Saved mouse button/DPI profile work is outside this
release; G HUB's existing profile remains available separately.

## Existing installation

Keep private state in `D:/Tools/OpenRGB/state-integration`; never copy it into a
public package. That directory already contains the verified device addresses,
locally reused Secretlab credential and `office-ambience.json`:

```json
{"monitor":"primary","fps":15,"smoothing_ms":140}
```

After installing the hash-verified package into its versioned release directory:

```powershell
pwsh -NoProfile -File D:/Tools/OpenRGB/releases/1.1-office.0.3.0/office/Start-Office.ps1 -InstallRoot D:/Tools/OpenRGB/releases/1.1-office.0.3.0 -StateRoot D:/Tools/OpenRGB/state-integration -AllDevices -Ambience
```

`Start-Office.ps1` checks the native executable and plugin hashes and rejects a
second OpenRGB/SignalRGB writer. Its child TEMP/TMP stays in the private runtime
directory. The native owner event provides detection readiness and graceful stop.
Pairing, keymaps, firmware, ordinary input bindings and boot settings are not reset.

## Observe and stop

Use the dedicated Python environment with pinned `requirements.txt`:

```powershell
D:/Tools/OpenRGB/python/Scripts/python.exe -B D:/Tools/OpenRGB/releases/1.1-office.0.3.0/office/office_devices.py inventory
pwsh -NoProfile -File D:/Tools/OpenRGB/releases/1.1-office.0.3.0/office/Stop-Office.ps1 -StateRoot D:/Tools/OpenRGB/state-integration
```

Atomic `office-ambience-status.json` is a last-state diagnostic checkpoint,
updated on source/pause/readiness/error changes, not every second. Its frame
counters and timings describe that checkpoint; use authenticated `office_control.py`
snapshots or the manually invoked `watch_ambience.py` for live progress. The unified
UI already uses in-memory snapshots. Ten-second health logs remain available.
This is software timing;
Govee streaming does not acknowledge physical LED application. Native logs and
`owner.json` remain in the state directory. The stop script verifies PID, creation
time and executable, requests normal teardown, waits for exit and releases Govee
streaming. No arbitrary execution deadline or periodic stream re-enable is used.

## Native control panel

Open the installed **Office Ambilight** shortcut, or run:

```powershell
pwsh -NoProfile -File D:/Tools/OpenRGB/releases/1.1-office.0.3.0/office/Open-Office-Control.ps1
```

OpenRGB.exe hosts the Office panel and its tray in the same process. Opening the
shortcut activates the existing application. Sign-in starts it quietly; closing
the window keeps lighting running when the tray preference is enabled. Exit
Office Ambilight tears down capture and output. An independent event thread owns
capture/output, so GUI work cannot starve the lights. Control adjusts output
FPS, smoothing and enable. Topology displays the
actual main-display preview, sampling rectangles and live LED colours for all six devices.
Select a zone or individual LED, then drag or edit its percentage coordinates.
Rotate and reverse preserve hardware LED identities. Save applies the draft
atomically; Reload discards it. Opening the panel leaves the existing map intact.
Devices provides inclusion, Identify, rescan, native profiles and contextual
OpenRGB hardware details. Native modes expose only supported controls and actual
driver ranges. Applying a hardware effect hands that device away from ambience;
Use ambience restores its screen mapping. Hardware profiles and manual device
memory saves are distinct from the sampling topology. Rest/tests restore the
selected owner afterward. Geometry changes that would invalidate a mapped device
are protected. Diagnostics provides explicit capture recovery. Calibration stops
when requested or on disconnect.
Disconnected controllers keep their saved regions and appear offline. Native
removal synchronizes with output before OpenRGB frees a controller; reconnecting
the same device rebinds it without rearranging hardware LED indexes.

Normal UI commands use typed queued calls inside the application. The retained
same-user diagnostic pipe uses a random per-process authentication value stored
only in private `office-control.json`; do not publish that file. The launcher and
installer verify native/plugin/runtime payloads against packaged provenance.

## Capture and recovery

Main-display brightness following reads Windows' applied gamma ramps once per
second, including LightBulb's scalar dimming. The strongest linear channel sets
the light intensity without applying LightBulb's colour temperature. Your saved
brightness is the baseline; Control → Advanced options → Output balance can
disable following and shows the applied factor. This is a measured display
attenuation, not an exact copy of LightBulb's rounded percentage. The readback
does not measure the monitor's physical backlight or HDR tone mapping. Nonlinear
colour-calibration ramps are reported as unsupported; failed reads retain the
last valid factor only on the same display, otherwise the baseline is used.
Static captures still react to brightness changes without recapturing/resampling.
Identify/calibration keep their reference colours, and rest always remains black.
No display gamma writes or LightBulb configuration changes are made.

The tested WGC target is the top-level Progman wallpaper host; its child renderer
is not capturable on this machine. GPU processing crops only the main display and reads
back one RGBA value per LED. Previous valid colours remain during source changes
and capture failures. Genuine black content is honored. Visible desktop-icon
exclusion is not verified: the current desktop has no icons, and a nonempty
visible icon list is rejected rather than substituted with foreground capture.

The previous 0.2.0 package remains a defined GUI-free ambience rollback; its owner
ignores the newly persisted `layout` member, using its original approximate map.
For a capture-free six-device rollback, stop the active owner and run the retained
`candidate-integration-1d0abb5e` with `-AllDevices` and without `-Ambience`, using
the same state directory. The separately published v1.1-office.0.1.0 is the older
Govee-only rollback. Preserved SignalRGB settings/plugins are another recovery
input; do not run simultaneous lighting writers.

The package records release, native and ambient source commits separately in
`office-build.json`, plus CI archive hashes. The native code is identical to the
verified compiled revision; current support scripts and sanitized acceptance
evidence are packaged from the release commit. No credentials or screenshots
are included. See `AMBIENCE.md` for capture details and retained upstream credit.
