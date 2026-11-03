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

1. Govee control integration — ACTIVE (O1-O5).
   Verified: Windows compilation; real executable/SDK against UDP peers (20 distinct
   RGB values, correct checksum, idle frame preserved at 30.39 seconds, exactly one
   stream-enable per device); headless real discovery/SDK enumeration of both models;
   user-confirmed red strip/blue bars and perimeter pattern. Actual first-ten indices
   drive the physically left bar; correcting the H8048 names/matrix to match.
   Remaining advancement blockers: final build with corrected bar mapping, sustained
   real-device stream/visual confirmation, stop/start lifecycle and installed parity.
   There are no tracked deferrals. Ambience plugins are explicitly outside this
   requested first step.
2. Final delivery — NOT STARTED (O6).
   Requires all first-stage acceptance criteria and physical confirmation.

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
red/blue; sustained output and startup latency still require observation.
SignalRGB's installed Govee.js currently hashes EC2510D880C4223D74D45C359F41E1542
034262134392FF1904F418B04318B8F (stock); preserve it, do not assume the old fix remains active.
