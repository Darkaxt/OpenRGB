# Office Screen integration: final delivery checkpoint

User authorized full native LightBulb integration, the exact tray, monthly upstream
maintenance extension and stopping standalone LightBulb. Specification R29-R34.
Stage31 COMPLETE; stage32 ACTIVE. No blockers or tracked deferrals. Final normal
release target is 0.9.1. Final delivery/startup retirement/cleanup remain pending.

Native compiled source56a094a924391d7a0478adc1f3efdd27080b5da2, successful Windows
build42220324884; archive b60fb19216209ec2133d249c9d32da9b843ae2b8eea17f400c469f6c71c642dd.
Matching Ambient691b57b474ace5d1fd98ee08300849d27eaf3dc3, successful Windows
build42220395237; archive775c06569a18954b0a109d59df83e802ec4f769ae89bf8342e5dfc637563cfa7.
Improved SDK-to-simulated-Govee graceful teardown and client shutdown run42222210668
also PASSED against that compiled artifact. Current task source has only allowed
support/docs differences after native compilation; do not rebuild unchanged code.
LightBulb reference f74285784be7bc191872c06b1b5e644eb209b98b, MIT attribution/map/icon.

Accepted behavior: complete imported screen settings, exact independent root pause
menus/all durations/sunrise/persistent resume, official bulb, solar/manual schedule,
transitions/smoothing, hotkeys/exclusions/preview, one gamma/RGB owner, existing
native topology/hardware modes. Actual Screen controls and tray rendered at all
three sizes and 100/150/200%; real editor Save/restore kept the complete configuration.
Two-display gamma temperature/brightness readback, exact baseline restoration,
applied RGB brightness once, stale draft rejection, native hotkey/display/resume/
time message paths, actual foreground exclusion preserving capture, persistent
pause deadlines/offsets through restart and complete cycle preview all passed.
Real main-display capture was observed when interactive. Unchanged relevant code
retains that evidence; current automatic screen-saver rest is expected, not a fake
capture success. No desktop input/foreground takeover was performed.

Final corrected host acceptance: candidate0.9.1 at
D:/Tools/OpenRGB/candidate-screen-0.9.1 passes fresh Screen/gamma/settings checks,
actual Office shutdown with no SDK clients, eight connected idle clients and 32
disconnecting clients, each native exit0 with exact display baseline restoration.
Current native UI export24 views/four Screen tabs/application bulb and Save/restore
passed. Its current preview is truthfully false during automatic screen-saver rest.
Candidate owner PID28300 at checkpoint; recheck exact process/start identity.

Evidence retained locally: D:/Tools/OpenRGB/validation/20261106/screen-0.9.0 and
screen-0.9.1. Private settings, source location, auth tokens and captures are never
release inputs. Original saved LightBulb settings remain untouched. Six-device /
314-LED topology and user RGB settings remain preserved.

The original0.9.0 package(source029eac300c7/plugin322da9f; archivecb779509b0c1d094958eae62324516d67ef4b16f96af0b28f8d2126c54e6ed26)
was published/retrieved but failed final host shutdown with0xc0000005. It is now
explicitly prerelease and not latest, with failure notes; tag/assets retained.
Dump/WinDbg identified unsigned Windows SOCKET accept(-1) missed by '<0', followed
by invalid-client destruction skipping sender join and freeing its mutex. The
corrected native code rejects INVALID_SOCKET, closes failed/late admission, joins
connection workers and sender ownership independently of socket validity, and
changes the condition predicate under its mutex. Earlier old-artifact smoke runs
42220382962/42221086999 passed and do not reliably reproduce the timing-sensitive
race; do not claim they failed. Actual original host dump plus source/dump layout
identified the defect; fixed native CI and real host shutdown passed afterwards.
Retained crash-88724.dmp SHA256 f6cff79a813cbf4fdd23fc60eaec11573525a0f26f80cfecce76f94b738d7e99.

Standalone PID43020 was stopped through the authorized elevation broker only after
exact native start639294986079909296/path/version2.7.2+a23b129 verification; original
settings/startup/app were preserved. Initial WMI timestamp mismatch stopped nothing.
Both display ramps already read neutral after exit; no extra reset was performed.
Private rollback record: state-integration/office-screen-migration.json. Preserve
standalone app and Office0.8.0 package. Do not restart competing gamma. Sign-in still
points to0.8.0 and standalone Run binding still exists until final release acceptance.

Monthly maintenance task updated/read back with all three upstreams, native
LightBulb adaptations, existing timing/status/target, quiet no-change behavior,
exact pins and complete verified release requirement. No extra run was triggered.

Scratch E:/Temp/openrgb-screen-20261106, open cleanup transaction11b910937fb4789e44c311568123550e.
Current D candidate uses D for native DLL/runtime I/O, cleanup transaction
d84473407c93918f4ec5a2d9ab197113: remove immediately after final owner replaces it.
Spent D candidates removed through cc6cbbd412d6a9a81def355b8f39875f and
3a585c49949a9020edfb5def40bd503f (86,452,263 and86,456,426 bytes; no residuals).
Spent symbol cache and unavoidable C crash-dump original removed through
explicit-generated-output transactiond89dbd413a7c7e4b85949afa5a1b5d94 (70,765,161
bytes, no residuals); verified D dump/logs retained. Initial preexisting_protected
inventory was correctly discarded before using the documented generated-output
contract. No local native build tree or new background helper. Persistent owner
runtime-temp remains separate from task scratch.

Next: commit/push final verified source/docs, package exact clean commits and CI
receipts, check package and publish normal0.9.1, independently retrieve/hash/check,
install and activate exact delivered package via existing quiet sign-in, verify
actual loaded module/gamma/map/rest behavior and shortcut icon, retire exact
standalone Run binding via Migrate-LightBulb.ps1, read back everything, clean spent
candidate/E scratch, reconcile final specification and close stage32. The0.9.0
installed candidate/archive are historical published deliverables; do not mutate
or automatically delete them. No further publication permission is needed.
