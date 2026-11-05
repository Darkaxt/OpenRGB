# Automatic idle screensaver rest

The ordinary idle saver differs from the Ctrl+Alt+L launch on this machine.
The read-only probe observed Windows' `Screen-saver` input desktop, the active
SPI saver flag and the configured fullscreen `WPXSCR~1.SCR` window. The 0.7.1
owner selected screensaver capture but received zero frames and reported WGC
`The parameter is incorrect.` It retained wallpaper colours (maximum channel
240) throughout the failed capture. Dismissing the saver restored wallpaper.

The explicit automatic-saver policy now rests all lighting, releases capture and
clears retained input. Exit uses the existing desktop/window event path to acquire
fresh imagery. The manually launched saver on Default remains a capture source.
No idle timeout, desktop input, wallpaper settings or saved mapping is changed.

Windows runs 41944655734 and 41944987152 passed native lifecycle, production GPU,
layout, widget and IPC checks. Coverage includes forced black across all six
controllers during automatic rest, overriding manual test modes, no stale colour
replay, fresh-frame recovery and unchanged settings. Manual saver window selection
remains covered on an isolated desktop. The candidate at Ambient a378a2e is
installed for the real automatic cycle. Final source d878b47 only corrects the
policy description; Windows run 41946005515 also passed all those checks.

Installed candidate readiness, six-device output and package provenance passed.
The genuine automatic cycle now passed: Screen-saver/SPI true selected
automatic-screensaver rest, released capture and held all 314 LED values at zero
throughout the recorded 16-second saver interval. Dismissal restored Default and
wallpaper with a fresh frame; all six controllers resumed submissions. The probe
completed successfully and the user's physical test confirmed off/resume working.
The custom configuration remains byte-identical. No desktop input was simulated.
Stage 21 is COMPLETE; final release verification is stage 22.
Private diagnostic traces and package verification receipts are retained under
`D:/Tools/OpenRGB/validation/20261105/automatic-saver`; this public record contains
no topology, credentials or control tokens.
