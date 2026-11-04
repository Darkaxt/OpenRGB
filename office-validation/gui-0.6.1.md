# Inverted topology placement grid

Feature acceptance COMPLETE; delivery ACTIVE.

The old grid used a fixed RGB(120,155,175) pen at alpha 24. It disappeared over
much of the bright wallpaper. Ambient source aafbbec1bbd2882e388e34245019ef2c0ea79224
instead draws one union of device-pixel-aligned grid rectangles using opaque-white
difference composition. The resulting grid pixels are the RGB inverse of the
preview. Intersections are filled once; composition is restored before region
overlays, outlines and handles. Grid spacing, snapping and mapping are unchanged.

Production MapCanvas rendering checks verify light/dark pixels, crossings,
unchanged pixels between lines, Show grid off, unchanged selection/rotation
handles and unchanged map JSON at 100%, 150% and 200% rendering. The complete
Windows CI run 41883193147 passed, including the production widget tests. The
exact artifact's widget tests also passed locally with QT_SCALE_FACTOR=1.5.
Artifact 13351121513 matches GitHub SHA-256
a07e466cf2aff2d5b01938828f6c4c785a0a0970c6801481bd24e834c4a28722.

Connected candidate exports at normal and 150% scaling use the actual LG capture
and retained six-controller map. The normal wallpaper and high-DPI maximized app
previews both show visible inverted grid lines and cyan selection handles. The
existing app-owned export was read-only; no Save or hardware test was performed.
Evidence: D:/Tools/OpenRGB/validation/20261104/gui-0.6.1/candidate-views and
candidate-150percent, with ci-success.log and high-dpi-widgets.log.

The first diagnostic launcher returned before the GUI export had finished because
PowerShell does not wait for a GUI executable invoked directly. That original
export completed and exited normally, producing its panel-export.json; its result
was inspected. The launcher now retains Process and calls WaitForExit, used for
the successful high-DPI export. No duplicate original export was launched.

Delivery uses the unchanged native capture/hardware owner. Open older panels and
their unsaved drafts are preserved. Versioned installation and shortcut activation
will use the new panel without restarting lighting. No capture/output code changed.
