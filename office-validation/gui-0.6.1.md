# Inverted topology placement grid

Feature acceptance COMPLETE; delivery ACTIVE. Final Ambient source:
189588543e633c7bd1664e532a74b6c34ec15ccd.

The old grid used a fixed RGB(120,155,175) pen at alpha 24. It disappeared over
much of the bright wallpaper. The final Ambient source
instead draws one union of device-pixel-aligned grid rectangles using opaque-white
difference composition. The resulting grid pixels are the RGB inverse of the
preview. Intersections are filled once; composition is restored before region
overlays, outlines and handles. Snapping and mapping are unchanged.

Production MapCanvas rendering checks verify light/dark pixels, crossings,
unchanged pixels between lines, Show grid off, unchanged selection/rotation
handles and unchanged map JSON at 100%, 150% and 200% rendering. The complete
Windows CI run 41886233498 passed, including the production widget tests. The
exact artifact's widget tests also passed locally with QT_SCALE_FACTOR=1.5.
Artifact 13352271179 matches GitHub SHA-256
2c337d3594a350184e6f5c538f20d4c7eccfc1ad7c1d5470b37a8da02f3f19cd.

The user identified that the inherited minimum-20-logical-pixel grid spacing
made the visible line count disagree with the percentage label. That clamp is
removed. Integer-indexed lines use the actual percentage, shared with snapping,
without repeated float accumulation. Pixel scans count 99 internal lines for 1%,
19 for 5%, and 9 for 10%, on both axes at small/large canvas sizes and all three
rendering scales. A production pointer drag with 1% snapping lands at 26%/28% as
expected. Final exports show the 100-interval 1% grid rather than the earlier
coarsened approximation. The unpublished first package/install were retired using
transaction f5804c781143b5d0bfedc6e360ca539b: 119 members, 139,300,524 bytes,
no exclusions/errors/residuals; current 0.6.0 panels and 0.5.0 owner were preserved.

Connected candidate exports at normal and 150% scaling use the actual LG capture
and retained six-controller map. The normal wallpaper and high-DPI maximized app
previews both show visible inverted grid lines and cyan selection handles. The
existing app-owned export was read-only; no Save or hardware test was performed.
Final evidence: D:/Tools/OpenRGB/validation/20261104/gui-0.6.1/final-candidate-views
and final-candidate-150percent, with ci-spacing-success.log and
final-high-dpi-widgets.log. Earlier candidate-* exports and ci-success.log are
historical evidence of the superseded spacing; they do not verify the final build.

The first diagnostic launcher returned before the GUI export had finished because
PowerShell does not wait for a GUI executable invoked directly. That original
export completed and exited normally, producing its panel-export.json; its result
was inspected. The launcher now retains Process and calls WaitForExit, used for
the successful high-DPI export. No duplicate original export was launched.

Delivery uses the unchanged native capture/hardware owner. Open older panels and
their unsaved drafts are preserved. Versioned installation and shortcut activation
will use the new panel without restarting lighting. No capture/output code changed.
