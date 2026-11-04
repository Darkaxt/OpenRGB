# OpenRGB office integration and ambience

Authoritative scope, 2026-11-04: user clarified that device integration is an
intermediate milestone and that the requested endpoint includes working ambience.
Continue autonomously through that endpoint. No desktop UI takeover. Existing
Govee v1.1-office.0.1.0 remains the verified rollback baseline, not overall completion.

## Requirements

- I1: Integrate the six current lighting controllers: Govee H6609, Govee H8048,
  Secretlab MAGRGB NL72S2, Keychron Q6 HE ISO, Lenovo Legion Pro 7 Gen 8 Spanish ISO
  keyboard/front lighting and Logitech G502 X PLUS. Discover the actual connected
  interfaces; enable only relevant detectors and preserve existing mappings.
  Retain the accepted approximate monitor 3/7/4/6 map and the verified bar order.
- I2: Verify each real device's colours and addressable regions, preserved ordinary
  keyboard and mouse input, stable sustained output and bounded CPU/memory use. Reuse the
  Govee evidence where code/configuration and relevant runtime behavior are unchanged.
  No speculative firmware flashing or onboard-profile resets are needed by this scope.
- I3: Preserve existing SignalRGB configuration, plugins, device settings and
  recovery material. Only one active lighting writer per device. G HUB is an
  authorized fallback for mouse button/DPI functions; preserve its saved profile
  and its disabled launch-at-login state. On 2026-11-04 the user authorized recovering
  G HUB after OpenRGB's devices are wired; restore its required service on demand
  if needed rather than restoring automatic boot. Real testing established that
  G HUB overrides part of the mouse's direct lighting: keep its user processes
  closed during OpenRGB use and leave the repaired application available on demand.
  The user explicitly moved onboard-memory button/DPI configuration to later on
  2026-11-04; exact mouse input-profile reproduction is outside this delivery.
  Preserve the saved G HUB profile for that later work, without resetting it.
- A1: Deliver screen ambience for the main LG DISPLAY2, 5120x2160, only. With ordinary
  non-maximized windows covering it, capture the rendered Wallpaper Engine wallpaper
  behind them. A maximized/fullscreen app on the LG takes priority; restoring,
  minimizing or closing it returns to wallpaper. An unobstructed LG desktop can use
  normal screen capture. Apps maximized only on another monitor do not take over.
- A2: On 2026-11-04 the user selected krojew/OpenRGB-Ambient as the engine to wire
  into OpenRGB after local comparison with EDAmbilight. Adapt that native plugin
  and reuse verified capture code where needed. A separate custom debugging UI
  was explicitly left for later and is outside this delivery. Keep the last valid image during
  source changes/capture failures until the new source produces a frame. Honour
  genuine dark content. Provide smooth colour adaptation and prompt wallpaper-change
  response; measure the complete capture-to-device path, including source transitions.
  Do not preserve the prior unexplained twenty-second wallpaper staleness as accepted behavior.
- A3: Map the current physical arrangement into the ambience canvas: monitor edges,
  two vertical bars, desk strip, external keyboard, laptop on the left and mouse
  on the right. The laptop follows the main monitor for this delivery; independent
  laptop-screen ambience remains outside scope.
- D1: Finish integration, physical acceptance and resource checks, then commit and
  deliver one proper verified final release for this complete outcome. Verify its
  published/downloaded and installed package, activation and rollback. No intermediate
  feature release is an overall stopping point. No unrequested startup tasks,
  driver installs, application removal or desktop UI control. Keep credentials and
  personal device settings out of public packages. Transactionally clean scratch.

User scope extension after ambience acceptance, 2026-11-04: SignalRGB may now be
removed after preserving its custom plugins, profiles and pairing/recovery data;
this overrides D1's former application-removal exclusion for SignalRGB only.
After delivery and retirement, investigate EDAmbilight in REA and recreate its
control interface for this system, preserving the working native capture/device
pipeline. OpenRGB currently runs deliberately headless; upstream also has a GUI
and tray. Do not take over the desktop UI. These subsequent authorized outcomes
do not reopen completed stages or permit parallel ACTIVE implementation stages.

## Staged execution and reconciliation

1. Device integration — COMPLETE (I1-I3).
   Verified: Govee baseline physical acceptance; native network regressions in
   CI 41733515534, 41735201548 and 41736410371; the latter two include graceful
   shutdown. Real detection now recognizes Keychron SRGBmods 1.0.6 / 109 LEDs.
   The current Legion C++ GET path reads 102 keys, six front sections and auxiliary
   1501; its saved 960-byte profile response is unchanged after the diagnostic runs.
   These are diagnostic/integration evidence, not complete physical acceptance.
   Current native candidate: 1d0abb5e, CI 41739950727 SUCCESS, including the
   detection-readiness regression and graceful exit. Downloaded artifact SHA256
   aaec8ebfc9e28b758f6f6fb7e1344075f7169f2614d96271f1652618345450a0;
   47 installed members verified in D:/Tools/OpenRGB/releases/candidate-integration-1d0abb5e.
   Live inventory and keyboard geometry pass for all six controllers and again
   after clean native restart (current PID 67736).
   User confirmed the five non-mouse colour patterns and stable animation. Mouse
   purple/blue split persisted while G HUB ran, then became green when its user
   processes were stopped: actual coexistence conflict established and isolated.
   G HUB recovered via broker request 77aefd7b481d472a8c919a5121df78fa: service
   Manual/Running, app autostart false, saved mouse profile retained. Its user
   processes are closed for exclusive OpenRGB lighting. Exact onboard input-profile
   work was explicitly moved outside this delivery by the user (see I3).
   Exclusive 1800-frame/controller run completed in 120.012 seconds at 15 FPS:
   native 29.73 MiB working set / 0.144% whole-machine CPU; sender 26.34 MiB / 0.042%.
   User confirmed no dark flashes on all six and the mouse's final red/yellow frame.
   Native exit code 0 and six-device restart verified; the complete saved Legion
   960-byte profile response is unchanged after real Direct streaming.
   Retained sanitized evidence: office-validation/device-integration-20261104.json.
   No remaining blockers or tracked deferrals for this stage.
2. Main-monitor ambience — COMPLETE (A1-A3).
   Stage 1's integrated device set is available. User now confirms consistent
   wallpaper colours across the six devices, including behind an ordinary window,
   successful LG maximize/restore switching and prompt actual wallpaper replacement.
   Selected engine: https://github.com/Darkaxt/OpenRGB-Ambient, canonical checkout
   D:/Projects/OpenRGB-Ambient, branch codex/office-ambience, upstream 778fdcbf8a9e20ccb41dbd7e597d361f294c69de.
   EDAmbilight repository b497e19a29adaa0666b74c89a03a7b82d7b2c922 contains docs;
   its verified v1.2.0 release includes readable HTML/JS and embedded Python 3.12
   bytecode (capture/ambilight/OpenRGB modules), rather than original engine sources.
   Nonexecuting REA inventory and official PyInstaller archive listing are retained
   at D:/Tools/OpenRGB/validation/20261104. EDEvent2Led is the same author's game
   event controller and explicitly documents binary-only distribution.
   Next: integrate native plugin loading without a desktop window, the LG source
   policy, physical sampling map, retained frames and timing diagnostics; then
   verify the complete source-to-six-controller workflow and wallpaper replacement.
   Source selection investigation, 2026-11-04: user clarified that the unresolved
   case is wallpaper hidden by ordinary windows. Unobstructed/maximized native
   capture already supplies the standard behavior. Wallpaper Engine's
   Chroma color output was evaluated using UnifiedRGB's native shim. Its native
   ABI/pipe test passed, but the installed Wallpaper Engine loader checks both
   Authenticode trust and publisher Razer USA Ltd.; metadata cannot satisfy that.
   No validation bypass was attempted. The single pilot DLL, originally absent,
   was removed through reviewed cleanup and the approved administrator broker.
   Retained source/license and loader evidence: D:/Tools/OpenRGB/validation/20261104.
   The user selected WGC next and explicitly ruled out composed-monitor DXGI as
   a wallpaper fallback. Preserve the old BSRGB WorkerW/PrintWindow code unchanged.
   WGC rejects the actual child renderer HWNDs with E_INVALIDARG; their visible
   top-level Progman ancestor is capturable and its LG crop excludes the floating
   app. Real 120-frame tests measured 18.55-27.52 FPS; the run with a floating
   window covering one third of the LG delivered 18.55 FPS, 98 changing grids,
   median GPU downscale/readback 0.55 ms, 41.86 MiB RAM and 0.091% host CPU.
   Read-only captured BMP inspection showed animated wallpaper without the app.
   User has no desktop icons, so visible-icon exclusion is not verified.
   No source-to-physical-device latency claim follows from these capture probes.
   Native host build: 82f150a2, CI 41752570205 SUCCESS. Ambient plugin candidate:
   ec36299f4a6b4dc16ff0138b49820410a4895c2e, CI 41755069942 SUCCESS. Production
   D3D11 shader regression passes selected-monitor crop, RGB ordering, regional
   samples and genuine black. Both archives independently match GitHub SHA256;
   the installed native executable and plugin members passed readback hashes.
   Candidate activated without UI at D:/Tools/OpenRGB/releases/candidate-ambience-82f150a2,
   PID 71804, private state D:/Tools/OpenRGB/state-integration. Previous PID 67736
   exited normally with code 0. Its previous candidate remains a defined rollback
   until the final release is accepted. No second lighting writer is running.
   Real wallpaper-to-controller run observed 15.21 FPS over 30.44 seconds, 71.93 MiB
   working set, 0.168% whole-machine CPU and two GPU 3D samples 0.79/0.91%.
   Median GPU processing 0.43 ms; median callback-to-native-submit 24.61 ms,
   max 61.19 ms. This is software submission latency, not physical LED acknowledgment.
   First wallpaper frame 480.62 ms; no capture errors in the sustained sample.
   All six SDK colour rows are nonblack; five changed during this wallpaper sample,
   while the mouse samples its static lower-right region. No physical appearance
   or new source-switch acceptance is inferred from those software counters.
   Retained evidence: office-validation/ambience-candidate-20261104.json.
   User acceptance received 2026-11-04: all six follow the soft wallpaper with
   consistent colours; LG maximize/restore plus wallpaper replacement "all works".
   Final combined-case check: the user confirms maximizing on the laptop has no
   effect and explicitly accepts the result as stable enough, with any later
   quirks to be reported. This closes current physical acceptance without another
   desktop takeover or repeated test ceremony. No remaining stage blockers or
   tracked deferrals. The final release remains separate and is not yet delivered.
   Native probe scratch D:/Temp/openrgb-wgc-native-20261104 was removed after its
   last use: transaction 579efa625a090532b1642530164665f1 APPLIED, 4,026,031 bytes.
3. Final delivery — COMPLETE (D1).
   Published normal release v1.1-office.0.2.0 at Darkaxt/OpenRGB, source 1294ef8c.
   Independent public download matches GitHub digest and SHA256 sidecar:
   c6d365f2a363a369e5100680d4f039cb6dd4fe76f6660cae7a88b3b1027fa953.
   All 56 installed members read back correctly at D:/Tools/OpenRGB/releases/1.1-office.0.2.0;
   the actual loaded ambient module, fresh frame after owner creation, six-device
   inventory and continuing output passed. Active owner PID 28460, no visible UI.
   Packaged native/plugin bytes exactly match the accepted candidate and CI builds.
   Wrong plugin metadata is rejected before extraction. Private state is excluded.
   Retained release evidence: office-validation/release-0.2.0-20261104.json.
   The capture-free 1d0abb5e candidate is intentionally retained for six-device
   rollback using the existing state; older published 0.1.0 remains Govee fallback.
   Remaining E: analysis inputs serve the explicitly authorized REA stage. Retire
   the now-unused 82f150a2 candidate through its exact cleanup transaction.
   Candidate cleanup 0d6ce034e84f5c5501b68d4a13bd4de5 APPLIED: 57 members,
   78,711,912 bytes. No remaining delivery blockers or deferrals.
4. SignalRGB retirement — COMPLETE.
   Registered silent uninstaller exited 0 and removed registration. The leftover
   deployed application binaries were removed through reviewed transaction
   4ea16de43db0fefcbe1288bb24f22549: 219 members, 610,735,291 bytes, APPLIED.
   App directory, processes, services and scheduled tasks are absent. The old
   BetterSignalRGBCapture login value is disabled and preserved for recovery.
   1,571 files hash-verified in G:/Archives/SignalRGB/2026-11-04-office-migration,
   with private pairing/settings registry exports and a defined recovery procedure.
   Original Documents/custom profile content is preserved. Native OpenRGB PID 28460
   continues from the published release; six-device inventory and fresh wallpaper
   output pass after retirement. Retained evidence: office-validation/signalrgb-retirement-20261104.json.
   No remaining stage blockers or tracked deferrals.
5. EDAmbilight interface reconstruction — ACTIVE.
   Inspect the actual shipped interface/engine through REA and establish a bounded
   authoritative UI specification. Recreate the applicable control surface around
   the existing native backend, including all six devices and the required LG
   wallpaper/app policy. Keep current lighting running during analysis. This
   outcome requires its own verified integrated release.
   Incorporate the supplied companion-plugin review: validate the failed-session
   recovery path against native lifecycle signals, distinguish new-frame delivery
   latency from reused-frame age, and clear transient diagnostics after confirmed
   successful frames. Preserve the currently accepted capture pipeline.
   Latest user direction: stop the train/mapping investigation and focus on
   EDAmbilight GUI REA; the user will adjust mappings tomorrow with the new tooling.
   REA recovered the shipped v1.2.0 HTML/CSS/JS, all nine inline script bodies,
   24 frontend RPC names, scene persistence and calibration contracts. Exact
   retained sources/hashes and pure geometry replay are at
   D:/Tools/OpenRGB/validation/20261104/edambilight-gui-v1.2.0.
   Companion source report: D:/Projects/OpenRGB-Ambient/EDAMBILIGHT-GUI-REVIEW.md.
   Sanitized evidence: office-validation/edambilight-gui-20261104.json.
   GUI REA is complete at the frontend-contract boundary; the GUI itself is not
   implemented or installed. Its integration/release and the review's native
   recovery/telemetry corrections remain current-stage acceptance blockers,
   not completed work or later-stage deferrals. Native settings are unchanged.
6. Monthly upstream maintenance — NOT STARTED.
   User requested this after the system/interface work is good and done. Schedule
   a monthly check of the OpenRGB and krojew/OpenRGB-Ambient upstreams, merge and
   verify compatible changes in the maintained forks, remain quiet when unchanged,
   and report conflicts or failing checks. Preserve active lighting and do not
   introduce an unattended desktop takeover or simultaneous device writer.
   Include the user's requested OpenRGB branch inventory/cleanup: remove verified
   obsolete or merged refs while preserving active work and release/rollback refs.

The former LG built-in LED investigation remains parked; Govee is the installed
monitor-lighting alternative. The unrelated VLC screenshots belong to another chat.
Canonical OpenRGB source: D:/Projects/OpenRGB; preserve current path bindings.
New disposable work: E:/Temp/openrgb-integration-20261104. Native build scratch,
if required, uses D:/Temp/openrgb-integration-build-20261104 for I/O; prefer hosted
compilation to avoid host load. Keep runtime state separate under D:/Tools/OpenRGB.
