Office Ambilight now samples the current Windows desktop wallpaper image first
after valid resume, then switches to a fresh live frame. Wallpaper Engine's
Windows override image is used when configured. Spanning wallpapers are cropped
to the actual main monitor through Windows' read-only wallpaper API; the existing
LED map and GPU colour processing are retained. Image paths/pixels remain private.

It continues looking for an eligible capture source after
unlock instead of waiting for another window notification. Unchanged unavailable
sources no longer generate repeated source switches. Capture setup reuses the
unchanged compiled GPU shaders instead of recompiling them on every restart.

Screensaver and lock protection still require a usable desktop, new session
input when the automatic-saver gate is held, and freshly read wallpaper imagery
before initial lighting resumes. Live output requires a fresh captured frame.
Existing device maps, screen adjustments, Awake preferences
and Windows power settings are preserved.

Windows CI verifies event-free source recovery, stable waiting diagnostics,
actual GPU sampling, capture lifecycle and the no-input screensaver regression.
