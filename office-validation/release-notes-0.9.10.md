# Office Ambilight 1.1-office.0.9.10

The lighting widget now uses native Windows acrylic behind its green surface.
Controls and device artwork stay sharp; rounded corners, pinning and the
expanded/collapsed tray anchor are preserved. Windows transparency and high
contrast preferences select the opaque fallback when effects are unavailable.
The effect is released when the widget hides.

The unified UI already reads native status in memory. The diagnostic
`office-ambience-status.json` now saves meaningful state changes instead of
rewriting every second. Live IPC counters, FPS measurement, health logs and
startup/preview notifications remain available. The optional progress observer
and legacy LightBulb migration read live IPC instead of stale file counters.

Verified on hosted Windows against source
bb7dba4e52f01171c8edfb3131d616d0e6c0028a, run42423239290. Real compositor pixels
prove blur while retaining background colour; native window lifecycle, geometry,
widget interactions and status publication/recovery checks passed. No user
desktop capture, Wallpaper Engine restart or lighting experiment was performed.
