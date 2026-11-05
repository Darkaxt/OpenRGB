# Windows main-display capture

The user requested capture follow Windows' main display at every location,
including laptop/mouse lighting when the desk monitor and other lights are absent.
The former implementation resolved a saved DISPLAY name and rested when it was
absent. The native owner now resolves MONITORINFOF_PRIMARY at source selection;
display-change and resume events invalidate capture and resolve the new target.
Wallpaper behind floating windows, maximized/fullscreen app priority, manual saver
capture and automatic saver/lock/display rest retain their existing implementation.

Legacy saved display names are ignored in memory. Loading does not rewrite the
saved settings or topology; the panel reports the effective policy as `primary`.
A later explicit Save persists that effective policy. Normalized regions retain
their relative placement across display resolutions. Diagnostics identify the
actual selected display and bounds; user-facing labels/help describe the policy.

Ambient source 59354d41085b5b64842bcb858b812623953bc4f9 passed Windows run
42019153225. Production GPU tests cover selecting either half of a shared host
texture, negative desktop origin and a laptop-only 16:10 image using unchanged
normalized regions. Native lifecycle tests cover primary API metadata, legacy
configuration loading, display-change invalidation, crop replacement, missing
display rest/recovery and laptop/mouse-only output with four offline controllers.
Existing GPU, layout, widget and control regressions also passed.

Installed candidate acceptance: actual Windows primary DISPLAY2 bounds
[0,0,5120,2160] match the owner and live wallpaper preview. The automatic saver
correctly rested all lights; the user's dismissal resumed capture. Six controllers
and 314 LED values remain present, with byte-identical saved settings. Actual
offscreen panel exports cover 21 page/viewport combinations; Control and Help were
visually inspected. A focused 4.33-second sample measured 15.02 Hz output,
1.182 ms median GPU processing and 0.485% whole-machine CPU. Physical undocking
was not performed; topology/offline-device integration tests are not represented
as a physical travel/undock observation.

Stage 23 is COMPLETE. Stage 24 owns final publication, independently downloaded
and installed verification, startup/shortcut rebinding and exact obsolete-output
cleanup. Private acceptance traces, CI logs and package receipts live under
D:/Tools/OpenRGB/validation/20261105/main-display, outside the public package.
