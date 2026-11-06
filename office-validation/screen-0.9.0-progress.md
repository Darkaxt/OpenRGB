# Office Screen integration and 0.9.2 visual update

Current R35/R36 request: stage33 ACTIVE; stage34 NOT STARTED. Source-derived
LightBulb sundial, state cues and exact-field slider companions are integrated;
native 48-DIP header controls are integrated. Acceptance remains pending Windows
caption regression, installed render/DPI and real owner full-day preview checks.
No tracked deferrals. Advancement blocker is internal acceptance work; stage34
cannot advance until it passes. Existing live/startup binding remains0.9.1.

Checkpoint: Ambient534bd00c7eb68421ea361434fc356a296bd910e3,
Windows run42229330586. Earlier run42227721465 found a test-only Qt QObject lookup
compile error; corrected. Run42228519139 verified sundial/slider/motion, capture,
policy and existing behavior but caught native restore failure. Qt6.8.3 source
setWindowState_sys proves frameless restore uses MoveWindow while Windows snap
uses WS_MAXIMIZE. Caption/tray actions now use one native system-command owner;
the same restore regression and tray reopen must pass before activation.
Native af664a16c462d72e8602b53c3ee5b2c64ff13653 has authoritative R35/R36 and
scripts/office/Verify-Office-Visuals.ps1 and check_screen_visuals.py. Next: observe
the original CI run, retrieve verified artifact, prepare exact candidate, stop
one native owner, export all scales and run owner preview; preserve settings.

Scratch: E:/Temp/openrgb-lightbulb-visuals-20261106 (transaction
ee237c8cfd9d4142ad0a3f1ec7e00888). Native runtime candidate
D:/Tools/OpenRGB/candidate-office-0.9.2 uses D: for sustained/native runtime I/O
(transaction0cfebc579c976bbc6110b29c2bcc04ba); remove immediately after its last
consumer exits and final release supersedes it. Retained acceptance destination:
D:/Tools/OpenRGB/validation/20261106/screen-visuals-0.9.2.

## Previously completed 0.9.1 delivery

Specification R29-R34: stage31 COMPLETE; stage32 COMPLETE. No blockers or tracked
deferrals. Final software is published, independently retrieved, installed and
active. Full verified receipt: screen-release-0.9.1-20261106.json.

Normal/latest release:
https://github.com/Darkaxt/OpenRGB/releases/tag/v1.1-office.0.9.1
Release source ebceeac7164a3dd887cdee6d6f2ce3394b83b766.
Native56a094a924391d7a0478adc1f3efdd27080b5da2/build42220324884; actual graceful
SDK/controller wire verification42222210668. Ambient691b57b474ace5d1fd98ee08300849d27eaf3dc3/
build42220395237. LightBulb reference f74285784be7bc191872c06b1b5e644eb209b98b;
MIT attribution, source/feature map and unmodified official bulb are included.
Downloaded package SHA256143b9813102857eae1e880d3707d40ef490b9a39a8adf8ef21b023772fb6cd3c
matches the published asset/checksum. Delivered tag/assets/publication/latest and
all installed member hashes were checked independently.

Active installation: D:/Tools/OpenRGB/releases/1.1-office.0.9.1. Cold-started by the
existing quiet sign-in task (interactive/limited, IgnoreNew, no kill deadline),
not a new startup helper. Actual loaded plugin, process/start identity and one
native process/tray passed. Final live readback: main-display app capture, all six
devices/314 LEDs online, both-display gamma valid, screen management enabled,
manual pauses cleared, original RGB map/settings and imported source preserved.
Shortcut points to the final native launcher and bulb. Standalone LightBulb process
is absent and its exact Run entry was retired only after accepted final gamma.
Original application/settings and Office0.8.0 remain retained. Explicit rollback:
D:/Tools/OpenRGB/validation/20261106/screen-0.9.1/ROLLBACK.txt and private migration
record under state-integration. Do not run competing gamma writers.

Accepted integration: exact independent root pause menus/all choices, persistent
sunrise/duration/manual pauses, solar/manual scheduling, transitions/smoothing,
hotkeys/exclusions and full-day preview. Actual native UI/tray renders at all three
sizes and 100/150/200%, real editor Save/restore, source-derived contracts, Windows
production capture/UI/lifecycle checks, two-display gamma temperature/brightness
readback and exact exit restoration, brightness factor once, native event/hotkey
paths, actual foreground exclusion preserving RGB capture, deadline/offset restart
persistence and complete preview passed. Final corrected Office host additionally
exited zero with absent, idle and disconnecting SDK clients while restoring exact
original ramps. No desktop input/foreground takeover or private data publication.

Delivery exposed inherited Windows SDK unsigned INVALID_SOCKET admission and
sender lifetime defects in0.9.0 after gamma teardown had completed. Native0.9.1
rejects failed/late admissions and joins connection/sender ownership before its
resources disappear, with the wait predicate changed under its mutex. The actual
host dump/source identified the race; old-artifact smoke runs42220382962 and
42221086999 passed and were not claimed to reproduce it. Fixed native Windows
checks and real host shutdown passed.0.9.0 is honestly marked prerelease/not-latest
with failure notes and retained tag/assets. Final0.9.1 supersedes it.

The existing monthly-openrgb-upstream-maintenance automation now monitors and
implements compatible LightBulb changes as native adaptations alongside both
forks. Timing/status/target and quiet no-change behavior remain preserved. Source
pins, ABI, private state, one ownership model and verified full release are required.
No extra monthly run or duplicate automation was created.

Required private evidence is retained under D:/Tools/OpenRGB/validation/20261106/
screen-0.9.0 and screen-0.9.1: source import/gamma/readback/restoration, native
exclusion/hotkey/lifecycle, private persistence, UI renders, package/download and
sign-in/runtime/module receipts, rollback and reviewed cleanup manifests/results.
Original dump SHA256f6cff79a813cbf4fdd23fc60eaec11573525a0f26f80cfecce76f94b738d7e99
is retained locally with the diagnosis; private captures/settings are not Git inputs.

Cleanup complete through reviewed exact-target tickets after each last consumer:
- D candidates cc6cbbd412d6a9a81def355b8f39875f,3a585c49949a9020edfb5def40bd503f,
  d84473407c93918f4ec5a2d9ab197113:86,452,263 /86,456,426 /86,471,975 bytes.
- Spent debugger cache and unavoidable C dump original, documented explicit
  generated-output transactiond89dbd413a7c7e4b85949afa5a1b5d94:70,765,161 bytes.
- E:/Temp/openrgb-screen-20261106, transaction11b910937fb4789e44c311568123550e:
  1,479,789,319 bytes. All ticketed members removed; no residuals or active scratch
  consumers. Published packages, installed release, required evidence and rollback
  preserved. Persistent owner runtime-temp remains separate under state-integration.

This final documentation/receipt commit records verified delivery after the
immutable release source above. It changes no shipped executable, feature or
configuration and does not require another software release.
