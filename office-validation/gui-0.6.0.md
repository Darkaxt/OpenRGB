# Device-focused topology and group movement

Feature acceptance COMPLETE; delivery COMPLETE.

Ambient source `f4a9881c9d773ea736ac7532ef82b8dc2ff96be1` implements the existing
editor's multi-zone selection and visibility. No capture, sampling or hardware
protocol source changed. The old single-zone-only selection state was the cause
of the limitation; a deduplicated device/physical-LED target list now owns edits.

T1: Show defaults to Selected devices, with Selected zones and All devices.
Production controls and native screenshots verify the three scopes. T2: device
rows include every zone; real Qt platform mouse events exercise Ctrl toggle and
Shift range selection, with independent enable checkboxes. Canvas picking uses
the same tree selection; overlapping parent/child selection deduplicates LEDs.
T3: real canvas drags and arrows apply a single clamped translation to all targets
across devices, preserving spacing, unselected regions and physical identities.
T4: one undo restores the full gesture, redo reapplies it, Escape cancels it.
The connected native panel's Save test persisted a moved 109-LED laptop group,
reloaded with group selection intact, restored the exact original layout, then
confirmed unchanged private layout and device-configuration hashes. T5: original
single-zone handles/rotation tests remain passing; offline records use the same
retained layout and selection. Native view exports include the existing offline
fixture and all seven pages across three window sizes, plus device/group views.
Normal and 150% scaling were visually inspected, including small-window scrolling.

The initial Shift test failed because direct QWidget mouse injection omitted
Qt's global modifier state. Qt 6.8.3 QAbstractItemView::currentChanged consults
that state when setting its range anchor. The corrected test injects through
QTest's window/QPA path and passes; production selection semantics were retained.
Qt Test is a test-only dependency, absent from the product's runtime dependencies.

Local evidence is retained under
`D:/Tools/OpenRGB/validation/20261104/gui-0.6.0/`: `candidate-views`,
`candidate-150percent`, and private-state hash receipts (no credential contents).
The native panel reports actual LG preview, six controllers, no source error,
editor_save_roundtrip=true and multi_selection_save_roundtrip=true. Output maps
are restored before screenshots; supplemental selected-device/selected-zones
states are explicitly in-memory UI fixtures, not saved hardware changes.

Artifact `13347841390`, run `41876936394`, matches GitHub digest
`621c32c65a302800dfb2fc9836e281002c8ba5c66f2d0bae11627608ecd89f44`.
Its compiled production widget tests passed locally. All CI steps succeeded,
but the job remains in_progress without a conclusion at this checkpoint.
No successful-CI receipt has been synthesized; normal final download/packaging
and publication remained blocked on external run finalization at that checkpoint.
The original run/watch was retained. Feature stage closure is based on inspected native local
acceptance; it does not claim completed CI or a delivered 0.6.0 release.

The same run subsequently completed successfully. The original watch returned
exit 0; `ci-success.log` records passing capture, lifecycle, layout, production
widget and control checks. The normal verified-CI downloader then validated
the successful completed run, exact source and immutable artifact digest. It
matches the artifact already exercised locally. No duplicate CI run or fabricated
success receipt was used.

Normal release [v1.1-office.0.6.0](https://github.com/Darkaxt/OpenRGB/releases/tag/v1.1-office.0.6.0)
targets Core `a00488e41f9e9c84a27498a129d1597ca2cc0e9d`. Published ZIP SHA-256
`41a5c34965feaa6ea2080591c46e8b0308d0d4c86ee43cc80b1ac0f42789b968`
matches independent download, checksum file and GitHub asset digest. Independent
extraction read back all 102 members. Installed 0.6.0 panel PID 36676 and desktop
shortcut point to the versioned install. The installed native view export passed
with actual LG preview and all six retained maps; it was read-only, so its Save
flags are false rather than duplicating the already-passing exact-binary Save
test. Actual output observation recorded six online devices at 15.091 FPS.

The working 0.5.0 native owner PID 98884 was intentionally retained: no lighting
restart was needed for this GUI-only update. The 0.6.0 installed panel works with
that unchanged authenticated control protocol. Private hashes were verified
unchanged after the Save check and again before opening the interactive panel;
later user edits are independent. Published 0.5.0 remains available for rollback.

`delivery-receipt.json`, `installed-owner.json`, `installed-views` and
`cleanup-applied.json` are retained beside the other local evidence. Exact spent
`E:/Temp/openrgb-multiselect-20261104` was transactionally deleted after consumer
exit: 274 members, 739,468,288 bytes, no exclusions/errors/residuals. No temporary
consumer remains. All T1–T5 and delivery requirements are satisfied; no blocker
or tracked deferral remains. This closing evidence commit does not alter the
verified immutable package/source tag.

Scoped design-debt assessment: selection target ownership is centralized in
MapCanvas::targets; view filtering, tree selection, save restoration and actual
LED editing share that state. No additional abstraction/refactor is required
for this feature. Existing native capture and output remain on installed 0.5.0.
