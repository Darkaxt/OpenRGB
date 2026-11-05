# Unified Office application — implementation in progress

The user explicitly resumed this task. Stage 29 is ACTIVE; stage 30 is NOT
STARTED. No candidate is activated: installed 0.7.5 remains the sole owner.
Its saved topology/settings remain untouched. These notes do not claim delivery.

Implemented integration: OpenRGB.exe hosts Office's existing pages and one tray;
typed queued UI calls replace the ordinary pipe client. Capture, OS notifications
and output are constructed and destroyed on a dedicated Qt event thread.
Synchronous controller removal still waits for in-flight output. Diagnostic IPC
remains authenticated. Normal packages exclude OfficeControl.exe.

Devices adds rescan, native profiles, metadata, contextual mode controls, actual
hardware zones and schema-backed driver options. Capability flags/ranges control
the editor; mapped hardware geometry is protected. Native mode ownership persists
across reconnect/restart, excluding those devices from ambience writes. Rest and
tests temporarily take over and then restore the hardware selection. Hardware
memory save requires a successfully applied supported mode, not just a dropdown
selection. Settings controls the integrated engine without a second process.

Native API 6/build a185a35130b2a9cfe869c6b4241ba27bd6e0c85c passed Windows CI
42113774830, including SDK-to-wire/idle checks. Downloaded CI artifact digest:
5d155a0845f3121bff7638bf93b6f640542d4cc937c539a3f0313cbe3bd829f2.
Ambient 971263d compiled successfully. Its runtime test demonstrated output
while the GUI loop was blocked, synchronous removal, worker affinity and actual
worker teardown. The hardware editor test rejected an invalid empty snapshot
from its fixture; the fixture is corrected in aac9ffd. That revision also adds
profile/test/pause restoration checks and the genuine OpenRGB icon. The Windows
workflow for the complete current result must still be inspected.

Support scripts now use the existing process's identity-addressed Show event.
Shortcut and sign-in launches serialize on the same named owner-launch mutex.
Export renders the actual unified application offscreen; package/install checks
bind native/plugin/runtime hashes and reject a separate panel executable.
Syntax checks pass; package integration/activation/render acceptance is pending.

Remaining stage-29 acceptance: successful complete current Windows regressions;
package and installer rejection checks; actual app-owned page/hardware renders
and scaling; live sole-owner capture, mode/return/profile/rescan, process reuse,
settings preservation, quiet startup/tray lifecycle. Fix any failures before
closing the stage. No tracked deferrals. Stage 30 owns final publication,
independent release download, installed provenance/startup verification and
transactional retirement of obsolete releases/scratch.

Disposable inputs are confined to E:/Temp/openrgb-unified-20261105, registered
before creation with cleanup transaction 4411e7ea4027a9dd25a4690b3fbf6e3e.
No host native build tree is used; Windows compilation runs in hosted CI.
Persistent runtime scratch remains state-integration/runtime-temp, independent
of expendable task files. Retained final evidence will use a named validation
directory under D:/Tools/OpenRGB, with no pixels or credentials published.
