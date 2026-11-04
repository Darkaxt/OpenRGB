# Inverted topology placement grid

Feature acceptance COMPLETE; delivery COMPLETE. Final Ambient source:
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

Normal release v1.1-office.0.6.1 targets Core b0b0906f9841785f17553f43263244b05d561614.
The final ZIP SHA-256 is
45900c443b0df02856a3996dfeca8d6db9dd0acdd8a6e39aab72b4662f593e83.
An independent GitHub download matches the checksum file and asset digest; all
104 members were independently extracted/read back. Installed member hashes and
provenance match. The installed normal/150% view exports show the corrected grid
with actual LG preview and six controllers; private mapping/device configuration
hashes before/after those read-only exports match. New interactive panel PID
124160 has a real window, and the desktop shortcut points to installed 0.6.1.
Older 0.6.0 panels remain running to preserve their drafts. Native 0.5.0 lighting
owner PID 98884 was retained without a restart.

The broad legacy owner observation initially failed its >10 FPS assertion, despite
valid frames, six online devices and no capture/controller error. A scoped read-only
snapshot measured 6.605 FPS against the existing 15 FPS target while the unchanged
0.5.0 owner was running. This GUI-only revision does not claim a new throughput
acceptance or fix that runtime observation; it changes neither the owner binary nor
capture/output code. Actual grid rendering and map preservation checks passed.

Local delivery-receipt.json, published-release.json, installed-* exports and
private-state hash receipts record the actual verification. Temporary consumers
exited before transaction 1a754f802e0b0e6bbf0525ff5657779d removed the exact
E:/Temp/openrgb-inverted-grid-20261104 root: 416 members, 1,179,323,669 bytes,
no exclusions/errors/residuals. The published package, versioned installation and
required validation evidence remain. No feature or delivery blocker/deferral remains.
