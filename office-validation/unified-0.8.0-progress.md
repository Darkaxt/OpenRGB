# Unified Office application — verified integration

Stages 29 and 30 are COMPLETE. The normal 0.8.0 release is published and its
independently downloaded payload is installed and verified.

OpenRGB.exe hosts Office's existing pages and one tray with the genuine OpenRGB
application icon. Typed queued UI calls replace the ordinary pipe client.
Capture, OS notifications and output run on a dedicated Qt event thread.
Synchronous removal waits for in-flight output; external diagnostics remain
authenticated. Packages exclude the separate OfficeControl executable.

Devices integrates rescan, native profiles, identity, supported hardware modes,
actual speed/brightness/direction/colour ranges, physical zones and driver
configuration. Mapped geometry is protected. Explicit hardware ownership
survives restart/reconnect, excluding the frame writer; temporary tests/rest
restore the chosen owner. Device memory Save requires a supported applied mode.
Control/Topology/Preview retain their sampling and ambience responsibilities.
Settings now controls the integrated engine. Existing design assets are retained.

Native API 6/source a185a35130b2a9cfe869c6b4241ba27bd6e0c85c passed Windows CI
42113774830. Ambient c39ef18dd14bbc9598e1ebb449d39a679124d7ed passed Windows CI
42124655464, including output while the GUI loop is blocked, removal, teardown,
native ownership/profile/rest contracts and rendered widget interaction.

Actual application exports under local validation/20261106/unified-r2 cover
1000x700, 1440x900, 1920x1080 at 100/150/200% plus 24 native hardware tab views.
Inspected renders retain dark cards/cyan typography and opaque hardware dialogs.
Real group/rotation/name Save/reload restores the original document exactly:
0f393259b7143cd056474139ba6172c3efe1b9bcef5e1652bd7cf003ce31985a.
An earlier export exposed default/alias injection during Save; corrected in the
verified build. The exact original bytes were recovered and restored, not guessed.

Live checks: all six controllers, correct Windows-main-display WGC bounds and
fresh imagery; native handoff/return and stale identity rejection; actual native
profile Save/Load; completed rescan retaining maps; hardware ownership persistence
through restart. Repeated Show requests activate the same process. No desktop
input was used. Profile test artifact was removed with the cleanup helper.
An 8.5-second hidden-UI observation measured 14.83 FPS, 0.373% whole-machine CPU
and 99.3 MiB working set. These are software/native submission measurements;
no new physical lock/display test is claimed for this release.

The startup helper now waits for the host's existing post-construction Show
marker before reading endpoint metadata, preventing a Windows publication race.
The resource observer reuses the existing Win32 counter helper, with no psutil
dependency. Both were verified against the running candidate.

Normal release: https://github.com/Darkaxt/OpenRGB/releases/tag/v1.1-office.0.8.0
targets a4e19a86b0f4f419e965757d6bdb4ca99a751463. Independently retrieved ZIP
SHA-256 b0f0f4c73de2203f75a96b457164c85934283d51c92ad094085df7ef2d78f336
matches the published checksum, GitHub asset digest and verified installed
manifest. All 117 payload members were read back. Native/plugin/runtime
provenance and corrupt-package rejection passed; private state was excluded.
Source-to-native build differences remain limited to reviewed scripts and
documentation; compiled native provenance remains explicit.

Official releases/1.1-office.0.8.0 now owns startup and the desktop shortcut,
including its OpenRGB icon. The actual loaded plugin resolves to that release.
Scheduled cold start and repeated launcher reuse both returned result 0 with
one hidden process in the interactive session; no separate panel or service.
Fresh main-display wallpaper preview, six online controllers and 14.98 FPS were
verified against the installed package, with the original settings hash unchanged.
No new physical lock/display, Windows reboot or sign-out test is claimed.
Delivery records: installed-release.json, installed-cold-start.json,
installed-reuse-start.json, installed-main-display.json, delivery-verification.json
and published-release.json under local validation/20261106/unified-r2.
No remaining blockers or tracked deferrals.

Disposable E:/Temp/openrgb-unified-20261105 uses cleanup transaction
4411e7ea4027a9dd25a4690b3fbf6e3e. First candidate was removed through
30a8bc84a0aa33713ca18b8f74d88c1f. Candidate r2 is registered under
6d63a01c47256aafd96f8a8efa0ce5fa and has been removed after official activation.
Obsolete installed 0.7.5 was removed through e864cec4d82ccd5ccc785eaade531b21;
only 0.8.0 remains under releases. E: scratch transaction also completed,
removing 887,244,452 bytes with no exclusions or residuals. Both retired runtime
transactions completed without residuals. Required validation and CI receipts
remain on D:; the retained prior ZIP provides recovery if needed.
Persistent runtime scratch is state-integration/runtime-temp, independent of
task scratch. Credentials and capture pixels remain local and outside packages.
