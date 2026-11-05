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

Stages 23 and 24 are COMPLETE. Normal release
[v1.1-office.0.7.3](https://github.com/Darkaxt/OpenRGB/releases/tag/v1.1-office.0.7.3)
targets 6b77dde9e2441a85a64032ea05348128236cf68a. Its independently downloaded ZIP
matches the checksum, GitHub digest and all 111 installed payload files:
`0af054ebc5a212b2ebf3e94c1adeef57f37ba0a646dd8e001247c95b0b7b03c4`.
Native/plugin/panel binaries and the capture-check script exactly match the live
accepted candidate. Package provenance and corrupt-payload rejection passed.

Windows was locked during final runtime observation: all six controllers are
online and all 314 values are black, with capture released and no error. The
optional live observer was cancelled because intentional rest has no image;
stage 23 supplies the genuine live acceptance for the identical binaries. Saved
settings remain byte-identical. Shortcut/startup bind official 0.7.3; manually
invoking the sign-in task returned zero and reused the sole headless owner in the
interactive session. Candidate, obsolete 0.7.2 and exact task scratch were removed
through reviewed cleanup tickets. Only official 0.7.3 remains under releases.
No blocker or tracked deferral remains. Private acceptance traces, CI logs and package receipts live under
D:/Tools/OpenRGB/validation/20261105/main-display, outside the public package.
