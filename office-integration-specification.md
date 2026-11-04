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
5. EDAmbilight interface reconstruction — COMPLETE.
   Authoritative GUI acceptance (authorized to implement on 2026-11-04):
   U1: provide a usable native Qt control panel using the recovered dark cyan
   visual hierarchy, with Control, Topology, Devices and Diagnostics views.
   Qt Widgets is already shipped. Use authenticated per-user named-pipe IPC to
   the existing plugin; the panel must never be a second RGB/capture engine.
   U2: load the current six-device map without changing it. Show actual native
   sample rectangles, hardware LED identities and keyboard matrices, plus an
   on-demand downscaled capture preview and current LED colours. Support zone
   names, move/resize, quarter-turn rotation, reverse ordering, selection and
   individual regions. Save applies the complete validated map atomically,
   rejects stale edits and survives restart. The user owns tomorrow's mapping.
   U3: working enable, 1-30 FPS and smoothing-in-ms controls, per-device enable,
   explicit identify/calibration and deterministic return to ambience. Do not
   display unsupported EDAmbilight algorithms as functioning native controls.
   U4: preserve the LG-only wallpaper/app source policy and retained valid frame;
   correct frame-age versus new-frame submission metrics, transient error
   recovery and native source/session event handling. Provide explicit capture
   recovery for an unchanged unavailable source, without arbitrary timed retries.
   Handle native controller removal synchronously before its storage is freed;
   preserve offline maps, keep remaining outputs running and rebind reconnects.
   U5: verify actual IPC/configuration/GPU integration, malformed and stale edits,
   preview/LED identities and live output. Verify the real Qt panel offscreen at
   1000x700, 1440x900 and 1920x1080 without desktop takeover, including selected
   and expanded editor state. Retain focused rendered evidence.
   U6: deliver one verified versioned integrated GUI release and installed
   launch entry; verify downloaded bytes, actual runtime/module, GUI connection,
   persistence and existing six-device output. Retain 0.2.0 as rollback.
   Design contract: recovered #040c14/#020a10 surfaces, #14F5FF accent, 80px
   navigation rail, readable native text >=14px, labelled controls, central
   growing map and a reserved properties panel. Native platform controls replace
   the original Eel/browser runtime; no Chromium/Python capture engine is added.
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
   U1-U6 passed with ambient/panel da8eda520e4abea88267132e0c83f6b81d5a6449,
   CI 41813919632. Actual Qt renders at all three viewports, real Save action,
   malformed/stale rejection, restart persistence and exact baseline restoration
   passed. Huashu review retained the reference direction and verified readable
   native controls, selected navigation, growing preview and reserved properties.
   A native freed-controller mutex deadlock was traced and fixed with synchronous
   removal/output ownership. The actual KVM disconnect/reconnect retained all six
   maps and rebound both USB devices without restarting the owner.
   Normal release v1.1-office.0.3.0 is published at Darkaxt/OpenRGB, package source
   8ffc2763821373986eb2688fc4737c7724635ae5. Independent public download SHA256:
   9a5dd07e8687d99564fc0f9b565e97e8a4f6683e52eb800e986e395e00771a86.
   All 68 downloaded members match the actual installed package. Loaded plugin
   hash/path verified; active owner PID 103924 runs that version with six online
   devices and 314 LEDs. Live output measured 15.38 FPS over 29.85 seconds,
   73.32 MiB working set and 0.227% total-machine CPU. Software timings do not
   establish physical LED acknowledgment. The Office Ambilight desktop shortcut
   passed readback; all original maps/settings are restored and 0.2.0 is retained.
   Evidence: D:/Tools/OpenRGB/validation/20261104/gui-0.3.0 and
   office-validation/gui-release-0.3.0-20261104.json. No blockers or deferrals.
6. Monthly upstream maintenance — COMPLETE.
   User requested this after the system/interface work is good and done. Schedule
   a monthly check of the OpenRGB and krojew/OpenRGB-Ambient upstreams, merge and
   verify compatible changes in the maintained forks, remain quiet when unchanged,
   and report conflicts or failing checks. Preserve active lighting and do not
   introduce an unattended desktop takeover or simultaneous device writer.
   Include the user's requested OpenRGB branch inventory/cleanup: remove verified
   obsolete or merged refs while preserving active work and release/rollback refs.
   Active Codex heartbeat monthly-openrgb-upstream-maintenance is saved and read
   back for the first day of each month at 10:00 local time. It owns both fork
   checks and integrated merge/build/release verification, preserves live state,
   and stays quiet without actionable changes. It can be paused/deleted in the app.
   Manual branch inventory and exact apply verification removed 98 branches
   duplicated in canonical upstream; 104 active/protected or unverified-history
   branches remain. No force-push, tag deletion or history purge was performed.
   The helper disables lazy object fetching for future metadata inventories.
   The user also explicitly retired D:/Tools/Better-SignalRGB-Screen-Capture.
   Its absence and lack of active/startup/service/task consumers are verified:
   cleanup d9801efdb7aec09a94aafcb2762077e3 APPLIED, 1,602,216,986 bytes removed.
   The final OpenRGB owner remains healthy with six online devices; 0.2.0 rollback
   and the independent SignalRGB recovery archive are preserved. Spent D: GUI
   candidates/debugger scratch were transactionally removed after consumer exit.
   Evidence: office-validation/maintenance-20261104.json and retained exact branch
   manifest at D:/Tools/OpenRGB/validation/20261104/gui-0.3.0/branch-review.json.
   No required blockers or deferrals remain. Administrative schedule/cleanup
   records do not change the already delivered 0.3.0 application binaries.

## GUI revision requested 2026-11-04

The user rejected palette-only resemblance and explicitly expanded this revision
to working feature parity with all EDAmbilight repository screenshots. Preserve
the six-device native owner, LG-only wallpaper/app policy, physical LED identity,
offline/KVM handling, saved maps and last-valid-frame switching. The user saved
none of the experimental map changes and is waiting for the revised editor.

7. COMPLETE — Reference-led control and topology vertical slice. Acceptance:
   EDAmbilight-style grouped dashboard; readable vector arrows/controls; selectable
   algorithms (mean, percentile, median/dominant, fixed/adaptive with EMA), depth
   and adaptive bounds, black-bar exclusion, scene cut, saturation, brightness
   floor, real spatial blur, presets and advanced disclosure. All controls must
   reach the production sampler/output and persist atomically. Topology supports
   selection, move, eight edge/corner resize handles, cursor feedback, grid/snap,
   pan/zoom, fit, rotation/reverse, undo/redo, names, LED selection, edge presets,
   calibration and live output. No geometry operation renumbers hardware LEDs.
   Verify actual widget mouse paths and native GPU/output settings, plus rendered
   small/normal/large and high-DPI views. Blur must affect sampled RGB, including
   retained static frames, and the mapping view must show its sampling footprint.
   Verified source 4319799: hosted Windows CI 41841845778 passes production GPU,
   mouse resize/cancel/undo/stepper, geometry, lifecycle and IPC checks. The prior
   parked live check was resolved when the user unlocked the laptop. The live
   8602878 engine (unchanged in 4319799; only About/version and documentation
   changed) passed check_processing.py through the actual
   native owner: brightness/saturation reached submitted LED colours; all five
   algorithms exposed valid effective GPU regions; invalid settings were rejected;
   the original map/settings were restored. All 18 connected UI exports include
   the actual LG preview, and the real Save-button round-trip passed. Native
   enable/disable, calibration, identify/return, requested 20 FPS (20.057 measured)
   and explicit capture recovery passed. The unchanged current-task hosted GPU,
   widget and high-DPI evidence remains applicable. No blockers or deferrals.
   Closure design assessment found no required consolidation: capture/output
   remain owned by one native process and topology operations preserve indices.
8. COMPLETE — Complete screenshot feature and visual reconciliation. Acceptance:
   device/zone enable, counts, identify-all and edit-topology links; settings for
   connection test/reconnect, runtime/log access and lifecycle; actual live preview
   plus original EDAmbilight procedural preview controls (including local music,
   effects, postprocessing and presets); standby behavior driven by real Windows
   lock/display events; working loading/error/reconnect feedback. Native local
   IPC replaces the reference's SDK connection and web-port settings; WGC retains
   the required occlusion-safe source policy instead of adding incompatible
   foreground-capture fallbacks. Record each reference feature and its verified
   native equivalent in the companion GUI review. No inert imitation controls.
   Source and integration evidence: Ambient 4319799, successful Windows CI
   41841845778; all six native pages exported at 1000x700, 1440x900 and 1920x1080,
   both normal and 150% scaling. The real editor Save button persisted a temporary
   zone-name edit and restored the complete original map. The packaged native
   restart script stopped the exact owner gracefully, started one replacement,
   and verified native and authenticated endpoint readiness. The candidate's
   actual loaded plugin path was verified. Original procedural effects, particle
   modes, local audio and preset round-trip passed in the packaged browser page.
   The resumed actual LG preview and versioned panel exports passed without
   AllowUnavailable. About displays the package version. The six-controller
   read-only SDK observation completed 453 output advances in 30.77 seconds
   (14.72 measured across observer startup), with no capture errors and about
   0.252% total CPU. Live device removal/reconnection changed online count 6→4→6
   without restarting the owner, losing maps or interrupting the other devices.
   The user explicitly permits continuing with temporarily missing controllers;
   supported controller arrival/recovery must bind automatically. No missing
   peripheral alone is a reason to stop the other lighting. The lifecycle tests
   cover safe removal, replacement registration, persisted offline bootstrap and
   rescan. These results verify behavior, not visual fidelity. Visual acceptance
   was reopened by the user's corresponding-page screenshots and explicit request
   for a difference checklist and recovered iconography on 2026-11-04. The native
   panel does not reproduce the reference's page composition, fonts, icons,
   navigation, card treatments or control styling. This internal advancement
   blocker is resolved only by reference-led implementation and matching-page
   rendered verification; release cannot complete before that verification.
   The comparison/checklist and asset recovery are completed. The user's "Go
   ahead and fix them" explicitly authorizes implementation of the recorded
   differences. Preserve the functional evidence and private map. Current plan
   within this single ACTIVE stage: implement the shared original fonts/icons,
   shell and rendered controls; rebuild corresponding Control/Topology/Devices/
   Settings views and relevant preview/help/loading states; integrate and verify
   actual native renderings, UI interactions and unchanged live-owner behavior;
   reconcile each checklist item before closing the stage. These are work items
   inside stage 8, not concurrent implementation stages. Stage 9 owns final
   versioned packaging/publication and independent delivery verification.
   Retained evidence is under D:/Tools/OpenRGB/validation/20261104/gui-0.4.0.
   The private map is preserved. Exact spent
   D:/Temp/openrgb-gui-parity-20261104 and E:/Temp/openrgb-gui-parity-20261104
   outputs were transactionally removed after consumer exit (251,720,026 and
   657,827,304 bytes respectively); no candidate runs from Temp.
9. COMPLETE — Integrated final release and delivery. Acceptance: all revision
   requirements reconciled, existing lifecycle tests preserved, actual installed
   runtime and private-map continuity checked, normal versioned release published,
   independently downloaded/hash-verified, shortcut activation verified and spent
   task artifacts transactionally cleaned. Preserve 0.3.0 rollback.
   Published normal release v1.1-office.0.5.0 targets verified Core b6ef96ad63e;
   independently downloaded ZIP matches SHA-256 and GitHub asset digest, with
   all 100 members read back. Final installed native owner and Ambient DLL are
   loaded from D:/Tools/OpenRGB/releases/1.1-office.0.5.0; six controllers and
   314 LEDs stream at approximately 15 FPS. Installed GUI export and real Save
   round-trip pass. Desktop shortcut activates this version. Private map and
   device configuration hashes are unchanged. Published 0.3.0 rollback remains.
   Exact spent D:/Temp/openrgb-ui-fidelity-20261104 and
   E:/Temp/openrgb-ui-final-20261104 were transactionally removed after their
   consumers exited. No unresolved blocker or tracked deferral remains for this
   UI revision. Delivery evidence: office-validation/gui-release-0.5.0-20261104.json.

Stage 8 closure, 2026-11-04: Ambient 8a45dd6e6fc2de43d21d9049f9d4355a9eb3cc28,
successful Windows CI 41858244832. Recovered fonts/icons load natively without
fallback; production switch/slider/stepper, corner resizing, physical identities,
quarter-turn handle, undo/redo and four-turn tests pass. Corresponding native
pages and loading/offline/empty/rotated fixtures were inspected against the
modern references. `accepted-views` and `accepted-150percent` under
D:/Tools/OpenRGB/validation/20261104/gui-0.5.0 each export all seven pages at the
three required sizes and exit normally. The real Save action persisted temporary
rotation/name changes and restored the exact original map; JSON receipt reports
actual LG preview and no capture error. Native normalized mapping and single-owner
transport adaptations are explicit in all 90 resolutions in
office-validation/gui-0.5.0.md. Earlier failed visual/export iterations remain
historical evidence, not current blockers. No stage 8 blocker or deferral remains.

Design contract (user-directed reference fidelity, 2026-11-04): compare each native
page with its corresponding EDAmbilight repository screenshot. Use the modern
ss-* screenshot family as the main visual baseline, including the explicitly
supplied Settings reference, and record older screenshot-* variants separately.
Recover and use actual shipped iconography and Orbitron/Rajdhani typography;
reproduce the 80px icon rail, compact page-specific header, reference card layout,
double bezels, subtle surface depth, numeric readouts, toggles and sliders. The
former assistant-selected Segoe/88px/generic Qt approximation is rejected.
Preserve readability, correct transforms, real corner resizing, keyboard matrices
and native owner/source policy. Native transport adaptations do not justify
unrelated visual departures or fake SDK/web-port controls. Small/normal/large and
high-DPI actual renders remain required, with corresponding-page comparisons;
functional tests alone cannot establish visual compliance. Audit checklist:
D:/Projects/OpenRGB-Ambient/design-reference/VISUAL-PARITY-CHECKLIST.md.

User-requested rotation affordance (2026-11-04, stage 8): make orientation visible
even for square sampling regions. Add a floating quarter-turn rotate action
connected to the selected shape's own top edge, following that edge after each
rotation, plus a labelled top edge and first/last LED cues. Preserve physical LED
indices, pixel aspect, undo/redo and saved orientation. Verify click/hit targets,
four turns, save/load metadata and that resize handles remain usable. Existing
quarter-turn sampling semantics remain; no arbitrary-angle sampling is implied.

The former LG built-in LED investigation remains parked; Govee is the installed
monitor-lighting alternative. The unrelated VLC screenshots belong to another chat.
Canonical OpenRGB source: D:/Projects/OpenRGB; preserve current path bindings.

## Selected-device topology and group movement (2026-11-04)

User-authorized revision: show the selected device without the clutter of all
devices, and select multiple tree entries to move their lights together (including
the laptop keyboard, front strip and auxiliary light).

Requirements: T1 provide explicit Selected devices (default), Selected zones and
All devices visibility; T2 device-row selection includes all its zones, Ctrl
toggles entries and Shift selects a tree range, with matching canvas selection;
T3 a drag or arrow-key movement translates every selected LED by the same bounded
delta, preserving spacing, physical indices and unselected regions; T4 one undo
reverses a group gesture, Escape cancels it, save/reload retains geometry and
selection; T5 retain readable selection counts, single-zone editing/rotation and
existing visual layout, including offline devices. No capture/device protocol
change or desktop takeover. The existing map remains intact during acceptance.

Design contract: preserve current recovered typography, cyan editor, 80px rail
and responsive split panes. Replace the ambiguous all-regions switch with a
compact labelled view choice; selection uses highlighted rows, cyan member
outlines and one group boundary. Keep enable checkboxes independent of selection.

10. ACTIVE — Selected-device multi-selection feature (T1–T5). Implement and
    verify production tree/canvas gestures, common-delta bounds, undo/cancel,
    actual Save/readback/restoration, retained offline maps, and screenshots at
    1000x700/1440x900 with 100%/150% scaling. Internal acceptance blockers: these
    paths are not yet implemented; resolution is the complete verified feature.
11. NOT STARTED — Integrated 0.6.0 delivery. Depends on stage 10; publish normal
    verified package, independently retrieve/hash/read back, activate installed
    launcher without disturbing an unsaved panel, and clean exact scratch.
    Existing native capture/runtime remains unchanged; 0.5.0 is rollback.
New disposable work: E:/Temp/openrgb-integration-20261104. Native build scratch,
if required, uses D:/Temp/openrgb-integration-build-20261104 for I/O; prefer hosted
compilation to avoid host load. Keep runtime state separate under D:/Tools/OpenRGB.
