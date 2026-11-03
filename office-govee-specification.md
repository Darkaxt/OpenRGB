# OpenRGB Govee office trial

Authorization: user requested an OpenRGB fork/trial and authorized installation,
device control and command/source work on 2026-11-03. Desktop UI interaction is
prohibited. The user explicitly placed ambience plugins in a second step; this
deliverable is device control only. No ambience/capture rewrite belongs here.

## Requirements

- O1: Fork OpenRGB, preserve upstream provenance and add H6609 and H8048 as
  20-addressable-zone devices. H8048 represents two 10-zone bars; preserve the
  accepted H6609 3/7/4/6 perimeter approximation in the test documentation.
- O2: Install an isolated Windows x64 build and run its SDK server without a GUI.
  Use a separate configuration containing only these two Govee addresses, with
  unrelated detection disabled and loopback SDK binding. No system driver,
  startup entry, motherboard access or keyboard/mouse migration is required.
- O3: Give one application ownership of Govee output during the test. Preserve
  SignalRGB configuration/plugins/layouts and a concrete return procedure. Never
  run competing Govee writers. Earlier custom HTML isolation remains recoverable.
- O4: Verify real discovery and SDK enumeration, 20 RGB values per controller,
  distinct test colours, component order and colour updates after the previously
  observed stream-refresh intervals. Distinguish successful UDP writes from
  physical confirmation: the stream has no per-frame hardware acknowledgement.
  Ask the user for visual confirmation without taking over their desktop.
- O5: Log discovery/mode changes, stream enables and colour-send statistics using
  the existing logging system. Avoid periodic stream-enable commands for these
  models; preserve existing behavior for other devices. Verify actual packet
  encoding, lifecycle and resource behavior. Logging must not store desktop pixels.
- O6: Deliver the verified fork changes, a versioned usable Windows package,
  hash/source provenance, headless start/stop/test instructions and rollback.
  Verify the delivered/installed files. Public distribution includes no personal
  device addresses, identifiers, settings or diagnostic logs.

## Stages

1. Govee control integration — COMPLETE (O1-O5).
   Verified: Windows compilation; real executable/SDK against UDP peers (20 distinct
   RGB values, correct checksum, idle frame preserved at 30.39 seconds, exactly one
   stream-enable per device); headless real discovery/SDK enumeration of both models;
   user-confirmed red strip/blue bars and perimeter pattern. Actual first-ten indices
   drive the physically left bar; correcting the H8048 names/matrix to match.
   Corrected native build c5df4c43 passed the full SDK/UDP and bar-matrix checks
   locally and in hosted run 41729321503. Real discovery/enumeration and corrected
   bar names verified on the installed build. User confirmed the two-minute 15 FPS
   stream had no dark flashes or freezes; 1800 frames/device completed with zero
   UDP send failures. Stop/start passed with PID/executable/start-time ownership.
   OpenRGB measured 28.9 MiB working set, 9.27 MiB private, 0.042% whole-machine CPU
   during streaming; Python sender processes added 29.34 MiB working set.
   There are no tracked deferrals. Ambience plugins are explicitly outside this
   requested first step.
2. Final delivery — COMPLETE (O6).
   Published v1.1-office.0.1.0 as a normal GitHub release with Windows x64 ZIP and
   SHA256 asset. Independently downloaded it, checked its hash, release/tag/source
   metadata and all 41 installed package members. The installed executable's SDK
   enumerates both real controllers with corrected names and successfully sends
   the verified perimeter/bar pattern. No blockers or tracked deferrals remain.
   Disposable candidates and current OpenRGB scratch were transactionally cleaned.

## Starting evidence

Upstream master 8f3ee202f7abe171e26372cfdc53256593d03ff3; fork
https://github.com/Darkaxt/OpenRGB; branch codex/govee-office. The current Govee
driver supports LAN UDP/4003. Its model table lacks H6609/H8048, and its idle
keepalive repeats stream enable. The previous SignalRGB test established that
re-entering stream mode causes a visible dark flash on the H8048.

Canonical source D:/Projects/OpenRGB. Installed tool/runtime will live under
D:/Tools/OpenRGB with isolated state there. Disposable downloads use
E:/Temp/openrgb-office-20261103; local native build output, if required, uses
D:/Temp/openrgb-office-build-20261103 for native/small-file I/O and must be
transactionally cleaned after its last consumer. GitHub-hosted compilation is
preferred to avoid adding load to the already struggling laptop.

Current candidate: cf2c2cf6866a68d66ead5f70ba7196e339467ae6, downloaded artifact
SHA256 51155e529f5753f7de01f98070a4d2ec626c8c20f543752e883c5f6855bbb91a.
The initial CI harness waited on stdout redirected away by Windows console
attachment; its compiled artifact was retained and the corrected native-log event
test passed locally. Native Govee broadcast discovery also succeeds on the real LAN.
The initial solid command briefly blanked at mode entry before the user confirmed
red/blue. At that checkpoint sustained output had not yet been observed; the later
stream and stop/start acceptance results below supersede that checkpoint.
SignalRGB's installed Govee.js currently hashes EC2510D880C4223D74D45C359F41E1542
034262134392FF1904F418B04318B8F (stock); preserve it, do not assume the old fix remains active.

## Delivered result and retention

Release: https://github.com/Darkaxt/OpenRGB/releases/tag/v1.1-office.0.1.0
Package source/tag commit: 1978c49ee5b301447b88c5feeb66b4ca655d2dc9.
Native compilation commit: c5df4c4375541f94ffd02f5a08ff65b405f1f20b.
The package script verifies that native source is unchanged between those commits.
Package SHA256: 43a255d68f49952cd80356d5e241a567ba77cefe7f69dfd84ee2567d100acbed.
Executable SHA256: 101E408C9034FA6C9A950DE5FE3F0428B921C3DE7444714B5165CBD5CDD0E059.

Retained usable package: D:/Tools/OpenRGB/packages; active installation:
D:/Tools/OpenRGB/releases/1.1-office.0.1.0. SDK Python environment and private
configuration/native logs remain in D:/Tools/OpenRGB/python and state. The
user-authorized headless SDK server is the continuing consumer of state/runtime-temp
(empty at delivery); its launcher explicitly assigns TEMP/TMP there and no startup
registration was added. Stop-Office.ps1 verifies the recorded process identity and
releases streaming; reopening SignalRGB afterward restores its existing setup.

The two-minute real stream completed 1800 frames/controller at 15 FPS, zero UDP
send failures, with user-confirmed no flashes/freezes. Another 30-second stream
provided the active resource sample. No smoothing is implemented in this diagnostic
animation; its colour ramp wraps abruptly. No ambience or other-peripheral migration
is part of this release. The user permits G HUB as a fallback for mouse bindings/DPI
when a later lighting migration is undertaken.

Cleanup receipts: candidate runtimes c877dc650c149a19223f938081d58d58 removed
156248071 bytes; OpenRGB scratch 53d0e28ee8d6e72297a478114a374493 removed
146257222 bytes; generated source-side Python cache 5557be064dce06763074a363781c8bbb
removed 10440 bytes. Final runtime, package, source, private state and the existing
SignalRGB configuration/plugins/layouts were retained. The historical initial
startup blank is documented above; subsequent sustained control and stop/start
acceptance passed, and no permanent hardware acknowledgement is claimed.
