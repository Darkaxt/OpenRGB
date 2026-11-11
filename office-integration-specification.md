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
- A1: Deliver screen ambience for the Windows main display, resolved live rather
  than pinned to the LG or a DISPLAY number (user scope change, 2026-11-05).
  Originally this was LG DISPLAY2, 5120x2160 only. With ordinary
  non-maximized windows covering it, capture the rendered Wallpaper Engine wallpaper
  behind them. A maximized/fullscreen app on the main display takes priority; restoring,
  minimizing or closing it returns to wallpaper. An unobstructed main desktop can use
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
  laptop-screen ambience remains outside scope. When undocked, the laptop's main
  display drives its connected lights using the same normalized saved regions.
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

10. COMPLETE — Selected-device multi-selection feature (T1–T5). Implement and
    verify production tree/canvas gestures, common-delta bounds, undo/cancel,
    actual Save/readback/restoration, retained offline maps, and screenshots at
    1000x700/1440x900 with 100%/150% scaling. Verified production Qt/QPA tree
    Ctrl/Shift gestures, parent/device selection, visibility filters, cross-device
    common-delta movement, bounds, parent/child de-duplication, undo/redo, Escape,
    arrow movement and retained unselected identities. Actual connected panel
    Save/reload preserved the selected laptop group and restored the original
    private map/configuration hashes. Normal and 150% rendered views inspected.
    Evidence: office-validation/gui-0.6.0.md. No feature blocker/deferral remains.
11. COMPLETE — Integrated 0.6.0 delivery. Depends on stage 10; publish normal
    verified package, independently retrieve/hash/read back, activate installed
    launcher without disturbing an unsaved panel, and clean exact scratch.
    Existing native capture/runtime remains unchanged; 0.5.0 is rollback.
    GitHub run 41876936394 completed successfully after delayed runner
    finalization. The original managed watch observed completion; diagnostics
    and the normal verified-CI download match the same immutable artifact.
    Normal release v1.1-office.0.6.0 is published at Core a00488e41f9. The
    independently downloaded ZIP matches checksum and GitHub digest; all 102
    members were read back. Installed 0.6.0 panel and desktop shortcut verified;
    actual installed view export has six devices, live LG preview and no error.
    Native 0.5.0 owner PID 98884 was retained without restarting lighting; actual
    six-device output remains approximately 15 FPS. Private maps/configuration
    were restored exactly before opening the new interactive panel. The exact
    E:/Temp/openrgb-multiselect-20261104 scratch root was transactionally removed
    after all consumers exited (739,468,288 bytes). No blocker or deferral remains.
    Evidence: office-validation/gui-release-0.6.0-20261104.json.
## Inverted placement grid (2026-11-04)

The placement grid must invert the image pixels beneath its lines, so it remains
visible across bright and dark wallpaper. Invert intersections once, keep lines
crisp at normal/high DPI, and leave non-grid pixels, selection colours, handles,
snapping and saved maps unchanged. Show grid off removes the overlay.
User correction: remove the old implicit 20-pixel spacing clamp. The labelled
percentage must determine visible divisions on each axis (1% = 100 intervals),
matching snap positions independently of viewport size, DPI and zoom.

12. COMPLETE — Production canvas pixel checks verify exact RGB inversion on
    light/dark inputs, single inversion at crossings, unchanged non-grid pixels,
    Show grid off, selection handles and saved maps at 100%/150%/200% rendering.
    Hosted Windows run 41883193147 passed; its exact production widgets also
    passed locally with 150% Qt scaling. Connected normal/high-DPI exports show
    actual LG content and six controllers. The inherited 20-pixel clamp is removed:
    production pixel scans count 99 internal lines for 1%, 19 for 5%, and 9 for
    10%, on both axes at small/large sizes and 100%/150%/200% rendering. Real canvas
    dragging with snapping lands on the visible 1% lines. Final Windows run
    41886233498 and local 150% production widgets pass. Final connected normal/
    high-DPI exports were inspected. No feature blocker/deferral remains.
13. COMPLETE — Deliver verified 0.6.1 package through the normal release channel,
    independently retrieve/read back it, update the installed launcher and clean
    exact scratch. Preserve the user's open mapping draft and running lighting.
    The first unpublished candidate was transactionally removed after the user's
    spacing correction; its last consumers had exited. The final package must use
    Ambient 189588543e633c7bd1664e532a74b6c34ec15ccd, verified by run 41886233498.
    Normal release v1.1-office.0.6.1 targets Core b0b0906f984. Independent download
    matches its checksum and GitHub digest; all 104 installed/downloaded package
    members were read back. Installed normal/150% views retain actual LG preview,
    six devices and unchanged private-state hashes. New panel PID 124160 has a
    real window; desktop shortcut targets 0.6.1. Older panels/drafts and native
    owner PID 98884 remain intact. Exact E: scratch was transactionally removed
    after all temporary consumers exited. No feature/delivery blocker or deferral
    remains. Evidence: office-validation/gui-release-0.6.1-20261104.json.

## Readable topology and media-aware sampling (2026-11-04)

The user has saved the final topology: preserve its exact regions, names, indices
and settings except explicit user edits. Unselected regions in All devices must
use the selected-region line geometry/weight in visible neutral grey; selected
regions remain cyan and render above context. Blur belongs beside the Preview,
with a synchronized control beside Topology, using the existing saved blur value.
The independent animation playground remains browser content captured through the
existing maximized/fullscreen LG policy; do not add another RGB writer.

Black-bar detection must conservatively identify credible media mattes, supported
by common 4:3, 16:9, 16:10 and cinema ratios. Ratio alone must not crop; require
consistent near-black borders and positive content evidence. Reject ordinary dark
edges and retain legitimate black frames. Transform normalized sample coordinates
without modifying the saved topology. Avoid repeating a whole detection per LED;
keep image work on the GPU and verify common formats, dark-content rejection,
format transitions and integrated sampling. Do not redesign unrelated algorithms.

14. COMPLETE — Responsive panel preview, readable topology and shared Preview/Topology blur. Verify real
    rendered grey/cyan outlines, overlap ordering, synchronized controls and saved
    map preservation at normal/high DPI; clarify existing algorithms/playground.
    User priority 2026-11-04: fix the audited output starvation before further
    media-border implementation. Preview encoding must run outside the lighting
    event thread and capture mutex, with one bounded/coalesced job and cached
    generation-aware delivery. Hidden panels must stop image polling; unchanged
    and metadata-only snapshots must avoid image transfer/decoding. Preserve
    retained static frames, source changes, valid black, saved maps and shutdown.
    Prevent duplicate panel instances. Verify actual 15 FPS output with visible
    Preview and hidden panel, plus native worker/lifecycle regression checks.
    Immediate user-requested obsolete-release retirement is part of this stage:
    five duplicate panels exited normally; six unused release directories were
    transactionally removed (487,069,805 bytes); current 0.5.0 owner and 0.6.1
    panel remain until replacement. Private saved state hashes are unchanged.
    Production Windows run 41903597071 verifies coalescing, retained frames,
    encoding outside the capture lock/output thread, visibility gating and
    lifecycle. Installed candidate 600a8f5 holds 14.88 FPS with 29.54 fresh input
    FPS under five preview requests/second (median request 8.61 ms); metadata-only
    demand holds 14.80 FPS (median request 2.83 ms). Six devices remain online and
    the private map hash is unchanged. Normal/150% installed renders verify grey
    context and synchronized blur. Evidence: gui-0.7.0/candidate-*-performance.json
    and candidate-state-check.json. Closure assessment: no required consolidation
    remains beyond final consumer migration/obsolete-directory cleanup in 16.
15. COMPLETE — Conservative media-border detection integrated with native GPU
    sampling. Verify format/content evidence, transitions, valid black and actual
    runtime sampling/performance with the final saved topology retained.
    Windows run 41919043899 verifies paired margin/content evidence, 4:3, 16:9,
    16:10 and cinema formats, format transitions, asymmetric/dark/unsupported
    rejection and genuine black. Installed combined build fd38160 with detection
    enabled and five preview requests/second holds 14.92 output FPS with 29.98
    fresh input FPS, 0.665 ms GPU sampling and 0.92% total CPU. The owner's
    temporary setting was restored byte-for-byte after a clean owner exit;
    the restarted owner readback confirms six online devices, 314 LEDs and the
    original hash/settings. A transient endpoint publication sharing race in the
    diagnostic readiness reader was followed by confirmed actual endpoint
    readiness; it did not affect restoration or native output. No feature
    blocker/deferral remains. Closure assessment: the shared 1-pixel GPU pass
    avoids per-LED detection; no required architectural consolidation remains.
16. COMPLETE — Responsive-preview 0.7.0 release, independent download/readback, native owner/
    panel activation and readback. Retire obsolete release directories only after
    consumers/path bindings are migrated, preserve live drafts, and clean scratch.
    This delivery follows stages 14, 15, 17 and 18: the urgent performance correction
    and screensaver/rest policy take implementation priority, but do not authorize
    dropping the previously requested media-border resilience from final delivery.
    Normal release v1.1-office.0.7.0 was published at Core a9628e6fdeba6c0cfa08883615de5c7835388b49
    with Ambient cf06cbb7a7e5ed8e16176cf18bb2c9b80495c40a. Independent published
    ZIP/checksum download, GitHub asset digest, tag/source readback and every one
    of 107 installed payload members passed verification. SHA-256:
    c750022ce3c8f512f43152c9287f69325b50d0187758dcf3a74727772809392e.
    The official owner and panel run from releases/1.1-office.0.7.0, the desktop
    shortcut points there, six controllers/314 LEDs are online and the final map
    hash is unchanged. Superseded unpublished 0.7.0 package/root and final test
    candidate were transactionally removed after consumer migration. Earlier
    obsolete 0.5.0/0.6.1 folders are gone; only current 0.7.0 remains in releases.
    All 332 members of this stage's E scratch and the two spent native CI inputs
    were transactionally removed after required receipts/evidence were retained.
    No blocker or tracked deferral remains. Final reconciliation reuses the
    stage-14/15/17/18 closure assessments: no required consolidation is missing.

17. COMPLETE — Screensaver capture and automatic rest (user request 2026-11-04).
    The configured LG screensaver takes capture priority while active. Windows
    session lock or Windows display sleep forces every controller black and
    releases capture; calibration/identify and animated standby cannot override
    rest. Unlock/wake resumes the normal LG wallpaper/maximized-app policy from
    fresh frames, preserving saved mapping and brightness. Observe desktop-switch,
    WTS and power events, including startup on a locked/unavailable input desktop.
    Never switch the user's desktop or capture the secure lock screen. Verify
    production event/output tests, source selection, recovery, actual installed
    state and saved-map preservation. Windows session display notifications cover
    OS display sleep; an independently powered-off panel that Windows still
    reports connected/awake cannot be inferred from that notification alone.
    User-reported tray regression: the tray context menu must paint an opaque,
    readable background with visible selected/disabled items and separators,
    overriding the general transparent QWidget theme. Verify normal/high DPI.
    Manual Ctrl+Alt+L on this machine starts WPXSCR~1.SCR on Default while the
    SPI screensaver flag remains false. Recognize its fullscreen .scr/class window
    directly, including tool windows spanning monitors, and crop only the LG.
    Delivery belongs to 16 after the retained stage-15 requirement is verified.
    Verified: Windows run 41912140012, installed Ctrl+Alt+L source/colour/frame
    counters and user acceptance of saver/return and actual lock/off/unlock/resume.
    Owner-only power-message verification covers black/fresh recovery without
    changing host power. Run 41915198440 verifies opaque tray-menu rendering and
    selection at 100%/150%/200%. User authorized closing the old hidden panel;
    no OfficeControl consumer remained when exact retirement was checked.
    Known scope: capture reconstruction has a measured startup delay; no arbitrary
    waits were added. No current-stage blocker or deferral remains. Closure
    assessment: existing event/owner architecture suffices; no consolidation needed.

18. COMPLETE — Skip unchanged capture and settled lighting output (user request
    2026-11-05, required before the next release). When no new WGC frame arrives,
    retain the last valid source. When WGC delivers identical LG pixels, determine
    equality on the GPU before mip generation, blur, media detection or LED
    sampling; skip that processing and preview invalidation. No full-resolution
    CPU readback or collision-prone approximate fingerprint may classify changing
    imagery as static. Processing-setting/map/source changes still invalidate
    affected work. Pending colour adaptation must finish on the output clock even
    after input becomes static. Only changed LEDs update controller buffers; only
    devices with changed output submit a hardware frame, except a demonstrated
    protocol keepalive requirement. User clarification: when a refresh is needed,
    resend cached colours at the lowest verified reliable frequency, independently
    of capture/sampling, rather than driving the entire pipeline as a keepalive.
    Prefer batched writes where a protocol requires
    a full device frame rather than multiplying transactions per changed LED.
    First delivery and reconnected controllers must receive a complete state,
    including black, even when retained colours equal their initialized buffer.
    Rest, manual tests, enable/disable and genuine black remain correct. Verify
    exact pixel changes (including outside sampled areas), static frame counters,
    GPU-processing/preview reuse, partial device/LED writes, smoothing convergence,
    reconnect and sustained actual static Govee retention without black flashes.
    Report capture callbacks, processed changes, skipped inputs, output ticks and
    real device submissions distinctly; no claim of 15 new hardware frames for
    static content. Preserve the saved topology and release only after acceptance.
    Verified Windows run 41924410667 at Ambient cf06cbb: exact LG pixel equality,
    a one-bit pixel change, other-monitor exclusion, preview reuse, retained-map
    invalidation, changed LED/device submissions, adaptation convergence, first
    black, rest and reconnect. Installed six-controller/314-LED candidate passed
    a documented Wallpaper Engine pause/play test: 65.92 settled seconds, zero
    sampling passes, LED writes or owner device submissions; playback resumed
    and the exact saved topology hash was unchanged. User confirmed steady Govee
    strip/bars without flashes. Existing driver refreshes cached colours after
    30 seconds of silence (checked every 10 seconds), without B1 stream re-entry
    for H6609/H8048. This cadence is verified reliable in that observation, not
    an established absolute device timeout/minimum. Owner counters exclude those
    independent refreshes and do not imply hardware acknowledgements. Animated
    demand processed 15.03 changes/sec and skipped 14.55 duplicates/sec, with
    0.85% total CPU; installed normal/150% clock/update labels fit. No acceptance
    blocker or deferral remains. Closure assessment: existing capture/device
    ownership suffices; no new service or architectural consolidation is needed.

19. COMPLETE — Draft blur must change the Preview and Topology source image before
    Apply (2026-11-05 user report). The current slider only edits the draft while
    the preview uses the owner's applied blur (observed 0 versus draft 10).
    Large blur must integrate the sampled footprint rather than duplicate sharp
    edges at sparse sample offsets; verify high-frequency detail is smoothed.
    Send a bounded read-only preview override through the existing IPC/worker,
    using the same GPU filter as LED extraction. Do not apply draft settings,
    mutate/save topology or alter actual LED colours when rendering the draft.
    Cache by source revision and blur; reject stale blur images after a newer
    slider change. Return to zero must restore the source without double blur.
    Identical source/blur must reuse the cache; hidden panels remain quiet and
    PNG encoding remains outside the capture/output lock. Verify production GPU,
    real widget request/render paths, static input and no hardware/config writes.
    User override: terminate the program when replacement is needed, including
    unsaved drafts, without asking again. Preserve the saved topology/settings.
    Verified production Windows run 41930768086 (Ambient 12df982): static draft
    rendering, exact zero restoration, applied/draft equivalence without double
    blur, dense-detail integration, cache reuse, actual widget request/decode and
    stale-value rejection. Installed GPU read-only 0/10/0 comparison on the same
    retained wallpaper visibly blurred the image with mean RGB changes
    22.66/14.42/18.74, zero LED writes/submissions/sampling, exact source restoration
    and byte-identical settings. All six controllers/314 LEDs remained online.
    Playback resumed; visible-preview demand held 14.91 Hz, 0.541 ms GPU work,
    8.37 ms median request and 0.77% total CPU. Existing normal/high-DPI UI layout
    checks apply to the unchanged UI code in the final shader build. No blocker
    or deferral remains. Closure assessment: the existing GPU worker/IPC/cache
    suffices, without a new capture path or second RGB writer.
20. COMPLETE — Publish and independently verify Office 0.7.1 after stage 19;
    verify package hashes/provenance and actual installed owner/panel rendering,
    preserve saved settings, migrate shortcut/consumers and retire spent scratch
    and obsolete release only after the old draft/consumers are safely closed.
    Published normal release v1.1-office.0.7.1 at completed source ccdeeaa5;
    independently downloaded ZIP/checksum and verified the tag, GitHub digest,
    complete 108-member installed payload, plugin/panel provenance and installer
    rejection checks. Installed owner PID 115236 reports all six controllers and
    actual 640x270 preview at 14.92 Hz; panel PID 117828 and the verified desktop
    shortcut use the official 0.7.1 directory. Actual final app exports cover the
    required pages and show the corrected preview instruction. Saved topology
    SHA-256 remains identical. Both candidate roots, obsolete 0.7.0 installation
    and this task's E: scratch were removed through completed reviewed cleanup
    tickets; only the current release directory remains. Recovery packages and
    required acceptance evidence remain. No blocker or tracked deferral remains.

21. COMPLETE — Automatic idle screensaver rest (2026-11-05 user clarification).
    Distinguish Windows' automatic screensaver state/input desktop from the
    manually launched Ctrl+Alt+L saver. Automatic saver entry must force all
    configured lights off and release stale capture; exit must reacquire fresh
    imagery and resume. Preserve manual saver capture, lock/display rest, saved
    custom settings/topology and the sign-in task. Verify the native six-device
    output path, a genuine automatic entry/exit observation and recovery. Do not
    alter the user's idle timeout or simulate desktop input. Existing source only
    treats both saver cases as capture sources, so automatic entry has no explicit
    rest policy. The read-only probe caught Screen-saver/SPI true, the .scr window,
    zero captured frames and WGC "The parameter is incorrect" while retained
    output stayed nonzero (maximum channel 240). Thus inaccessible saver capture
    replayed stale wallpaper colours instead of resting. Preserve this evidence
    separately from the working manual Default-desktop saver path.
    Implemented and installed candidate a378a2e; final d878b47 changes only its
    policy documentation. Windows run 41946005515 passed production GPU,
    lifecycle, widget, layout and IPC checks. All six controllers remain online
    and the saved custom configuration is byte-identical. The genuine automatic
    cycle is now verified: Screen-saver/SPI true selected automatic-screensaver
    rest, released capture, and all 314 LED values remained zero throughout the
    recorded 16-second saver interval. Dismissal restored Default/wallpaper with
    a fresh captured frame and six-controller submissions. Saved configuration
    remained byte-identical; the user confirmed physical off/resume working.
    Probe session 46530 completed successfully; candidate.jsonl is retained under
    D:/Tools/OpenRGB/validation/20261105/automatic-saver. No blocker or deferral
    remains. Closure assessment: existing lifecycle and native output ownership
    suffice; no service, timer override or additional capture path is needed.
22. COMPLETE — Deliver verified 0.7.2 after stage 21: published/downloaded and
    installed provenance, saved configuration, desktop shortcut and sign-in
    binding migrated before obsolete runtime retirement; cleanup exact scratch.
    Published normal release v1.1-office.0.7.2 at source 22b58b05 with Ambient
    d878b47. Independently downloaded ZIP/checksum, verified tag commit and GitHub
    digest, all 109 installed payload members and package provenance/rejection
    checks. The official owner reports six online controllers/314 LED values;
    Windows was locked during final observation, so capture was correctly released
    and every output value was black, without capture errors. Genuine automatic
    off/resume acceptance is recorded in stage 21; no fresh-preview claim is made
    for this locked-session observation. Final installed panel exports covered
    all 21 page/viewport combinations. Desktop shortcut and sign-in binding use
    official 0.7.2; manually invoked sign-in task completed with result zero and
    reused the sole headless owner in the interactive user session. Saved custom
    configuration is byte-identical. Candidate and obsolete 0.7.1 installations
    and exact E: scratch were transactionally removed; only official 0.7.2 remains
    under releases. Recovery packages and required acceptance evidence remain.
    No blocker or tracked deferral remains.

23. COMPLETE — Windows main-display capture (2026-11-05 user request, A1/A3).
    Resolve the primary display on source selection and display-change/resume
    events, regardless of legacy saved monitor name. Retain wallpaper-only capture
    behind floating windows and app/manual-saver priority on that display only.
    Preserve automatic-saver/lock/display rest, saved topology/custom processing,
    offline device maps and the single native owner. Resolution/main-display
    changes must refresh the crop without rewriting normalized regions. Verify
    production Windows monitor selection, display-change invalidation, crop
    switching, offline laptop/mouse output and unchanged saved settings. Update
    UI/help/diagnostics to describe and identify the actual main display.
    Implemented in Ambient 59354d4. Windows run 42019153225 passed production GPU,
    lifecycle, layout, widget and IPC checks: native primary-display resolution,
    topology event invalidation, different crop origins/resolutions, normalized
    map preservation, laptop/mouse-only output and rest/recovery are covered.
    Installed candidate reports primary DISPLAY2 at [0,0,5120,2160], matching
    Windows. Automatic saver entry correctly rested all lights without capture
    error. After the user's dismissal, the original live check and export sessions
    completed: actual wallpaper preview matches native primary bounds, six devices
    online, all 314 values present and saved configuration byte-identical. Actual
    app exports cover 21 page/viewport combinations; Control/Help render the new
    main-display policy correctly. Focused observation measured 15.02 Hz output,
    1.182 ms median GPU processing and 0.485% whole-machine CPU over 4.33 seconds;
    this short sample is not a sustained workload benchmark. Physical undocking
    was not performed; synthetic topology transitions and two-device native output
    are explicitly distinguished from that observation. No blocker or deferral
    remains. Closure assessment: existing display events, WGC crop, normalized
    map and offline inventory satisfy portability without another capture engine.
24. COMPLETE — Deliver 0.7.3 after stage 23: verify normal published/downloaded
    and installed artifacts, exact source provenance, current main-display output,
    shortcut/sign-in migration, preserved settings and obsolete-release/scratch
    cleanup. Physical undocking is not simulated by changing the user's display
    configuration; distinguish deterministic integration coverage from any actual
    undock observation.
    Normal release v1.1-office.0.7.3 targets 6b77dde9e2441a85a64032ea05348128236cf68a
    with Ambient 59354d4. Independently downloaded ZIP/checksum match the GitHub
    asset digest; all 111 installed payload files and tested candidate runtime
    binaries match. Package provenance and corrupt-plugin/panel rejection passed.
    Official owner is the sole native writer, with six controllers online; saved
    configuration remains byte-identical. Windows was locked during final native
    observation, correctly releasing capture and resting all 314 LED values.
    Live acceptance uses stage 23's identical runtime binaries, rather than
    claiming a locked-session preview. Shortcut/sign-in bind official 0.7.3;
    the manually invoked scheduled task returned zero and reused one headless
    interactive-session owner. Candidate and obsolete 0.7.2 installations and
    exact E: scratch were transactionally removed. Only official 0.7.3 remains
    under releases. Required acceptance/CI receipts and recovery packages remain.
    No blocker or deferral remains; final reconciliation reuses stage 23's
    existing-event/crop/map ownership assessment, with no further machinery.

### Incident correlation logging — authorized 2026-11-05

R25: Retain a bounded, append-only Ambilight diagnostic journal independent of
the generic OpenRGB log and replace-in-place status snapshot. Each record must
identify UTC time, monotonic process time, PID/TID, session and build provenance.
Record capture/source creation and release intent/completion, first frames,
capture/Direct3D errors with HRESULT and removal reason, desktop/session/display
events, rest transitions, control actions and device availability changes.
Include low-frequency health snapshots, without recording every frame, pixels,
window titles, credentials or control tokens. Journal errors must be visible
without changing capture/output policy. Preserve prior records across restart,
bound retention, and verify readable complete records after abrupt process exit.
The existing empty pre-crash generic log remains an unresolved evidence gap;
do not assert a buffering cause or change capture recovery on that assumption.

25. COMPLETE — Implement R25 end-to-end, regression-test abrupt-exit persistence,
    rotation/concurrent callback writes and real lifecycle integration. Verify
    the Windows build and live journal/capture while preserving saved settings.
    Ambient ab7286b, Windows run 42055069171: actual process ExitProcess without
    destructor preserves the last intent, restart appends, concurrent callbacks
    remain parseable, bounded rotation and observable I/O failure pass. Production
    session/display/rest/control handlers persist events; existing GPU/layout/IPC
    behavior passes. Live candidate 92b2cdd records actual capture creation, first
    frame, health and complete release/recreate pairs with six online devices,
    unchanged saved settings, 14.91 Hz output and 0.212% total CPU over 12.68 s.
    Live validation caught an empty source-revision field; ab7286b fixes resolved
    Git plumbing and adds an exact-revision test. Its capture/journal behavior is
    unchanged; final installed build/restart identity is verified in stage 26.
    Generic log emptiness is not attributed to buffering: its source already
    flushes each record. The independent write-through journal closes that
    diagnostic gap without modifying capture policy. No blocker or deferral
    remains. Closure assessment: one small bounded writer serves the existing
    native owner; no service, new capture engine or per-frame logging is needed.
26. COMPLETE — Deliver verified 0.7.4 after stage 25: publish/retrieve and
    verify package provenance, install/activate one owner, migrate shortcut and
    sign-in binding, verify current capture plus durable records, clean obsolete
    release and exact scratch after consumers migrate.
    Normal v1.1-office.0.7.4 targets 0cf15d067797785aec0cf422007b5a376b029fbe
    and Ambient ab7286b20969db720c4d9d7b699432bbc431ccd7. Independent download
    matches the published SHA-256 and all 112 installed payload files. Sole owner
    PID 19700 records the exact Ambient revision, capture stages, first frames and
    health alongside prior sessions. Capture matches Windows primary DISPLAY29
    at 5120x2160 after the NVIDIA update; saved configuration remains identical.
    Activation observed six controllers online; final read-only preview observed
    four online, without changing device availability or asserting physical output.
    Final short measurement: 14.90 Hz output, 0.279% total CPU over 12.42 seconds;
    this is not a sustained benchmark. Sign-in task returned zero, reused the sole
    headless owner and launched no panel; shortcut and binding use official 0.7.4.
    Candidate/obsolete 0.7.3 cleanup transaction f86fc8f266ccfc7c12c9ec768e7189e1
    and exact E:/Temp/openrgb-journal-20261105 transaction
    e5be184d1242d560bd2c3a47140c3401 both applied completely. Only 0.7.4 remains
    under releases; verified recovery packages and incident evidence are retained.
    Persistent acceptance: D:/Tools/OpenRGB/validation/20261105/journal.
    No blocker or tracked deferral remains. R25 is reconciled against persisted
    lifecycle/error/provenance records, abrupt-exit/rotation checks and actual
    installed output. Prior DirectX incident attribution remains unknown; this
    delivery improves evidence and does not claim to repair that incident.

### Main-display dimming follow — authorized 2026-11-05

R26: Investigate read-only Windows gamma-ramp observation before considering any
LightBulb modification. Follow the Windows main display's applied scalar dimming
in ordinary ambience output, multiplying the user's existing brightness baseline
without rewriting it. Brightness changes must affect retained/static captured
colours without recapture or GPU resampling. Preserve colour hue, topology,
Identify/calibration and mandatory lock/sleep black output. Add a user-facing
follow toggle and observable applied factor/read status; unsupported/nonlinear
readback must not be silently presented as valid. Preserve the last valid factor
only for the same display on read failure; a display change resets it. Do not
modify display gamma, LightBulb's process/settings, or ScreenBar Halo hardware.

27. COMPLETE — Implement R26 through native output and panel controls, focused
    regression tests and live validation of gamma reads/static-input dimming,
    unchanged baseline/topology, test/rest behavior and resource use. Read-only
    probe observes primary DISPLAY2 at 0.86073 with linear equal-channel ramps.
    Windows integration run 42087443347 passed for ambient 3b73d9b, including
    retained-frame dimming, toggle, Identify bypass, rest/reconnect and UI tests.
    Local read-only gamma observation costs 1.006 ms median for both displays;
    native observation reads just the main display at 1 Hz. Saved settings remain
    byte-identical (0f393259b7143cd056474139ba6172c3efe1b9bcef5e1652bd7cf003ce31985a).
    User dismissed the saver; live candidate owner 52532 and independent GDI
    readback agree exactly at 0.843408 on DISPLAY2. Fresh wallpaper preview,
    all six controllers and 14.92 Hz output verified, with unchanged saved map.
    Focused 6.64-second observation measured 0.684% whole-machine CPU and 85.3 MB
    working set. Package-provenance/corrupt-payload rejection and panel export
    checks passed. No remaining blockers.
    No tracked deferrals.
28. COMPLETE — Deliver verified 0.7.5 after stage 27: normal release download
    and installed-payload verification, sole-owner/startup/shortcut activation,
    preserved settings and transactional retirement of obsolete binaries/scratch.
    No tracked deferrals.

Stage 28 delivery: normal published v1.1-office.0.7.5 targets e08914ab7fafcb9075194df47145dfadb85b7d5a.
The independently downloaded ZIP matches GitHub digest and checksum
79a9c6de1a6b47a209a25e11da8b4436592108f0549d74f10ebf16759201f44a.
All 116 installed members and accepted runtime binaries match. Owner 34204 runs
the official 0.7.5 path with valid factor 0.84337755, fresh capture and six online
controllers. Sign-in task reuses that sole headless owner (result 0); startup and
shortcut target 0.7.5. Saved settings retain their original hash. No blockers or
tracked deferrals remain. No implementation stage is ACTIVE.
E:/Temp/openrgb-lightbulb-20261105 was removed through transaction
cc5e483cdd80f2287d192567d8229437 (716123770 bytes). Candidate
D:/Tools/OpenRGB/candidate-brightness-0.7.5 was removed through
09e28b47ba6b58de91f719facb07f5a6 (171697073 bytes); obsolete 0.7.4 installation
through bf6d42c1644afc84344e186a25f36ff2 (85828315 bytes). All applied without
residuals; only 0.7.5 remains under releases. Recovery ZIPs remain intentional
package outputs. Continuing runtime uses state-integration/runtime-temp
independently of disposable scratch. Required acceptance receipts remain under
D:/Tools/OpenRGB/validation/20261105/lightbulb.

### Unified Office application — authorized 2026-11-05

R27: OpenRGB.exe hosts the existing Office UI and its single tray. Ordinary UI
requests use in-process, queued calls rather than the authenticated local pipe.
Construct the capture/output owner on its own Qt thread (including COM, native
event windows and timers); a stalled GUI must not stall lighting. Keep diagnostic
IPC and its authentication, controller-removal barriers, single-owner startup,
quiet sign-in, graceful exit and the existing capture/rest/recovery semantics.
Opening the shortcut activates the existing application; it must not start a
second hardware owner. Normal delivery has no separate OfficeControl executable.

R28: Integrate applicable OpenRGB hardware management deliberately, using the
existing Office visual system. Devices owns discovery/rescan, connection and
hardware identity, native hardware zones, supported modes and their actual
speed/brightness/direction/colour capabilities, hardware save when supported,
and driver-specific configuration. Hardware mode is an explicit per-device
alternative to ambience, retained across reconnect/restart. Temporary tests and
lock/display/saver rest must restore the selected owner afterwards. Never let
the frame sender overwrite a hardware effect. Capability-dependent controls
must be absent/disabled with an explanation when unsupported, not simulated.
Keep saved offline maps and reject stale device identities or geometry changes
that would invalidate a live map. Discovery uses OpenRGB's existing detector
configuration; this change does not add hardware protocols or enable unsafe
detectors. Native profiles are coordinated hardware snapshots on Devices, not
sampling-layout presets. Preserve existing device inclusion and Identify.

Feature placement/design contract:
| Area | Integration decision |
| --- | --- |
| Control | Keep capture/source policy, algorithms, sampling, smoothing, brightness following and ambience presets. Device switches remain ambience inclusion. |
| Topology | Keep sampling groups, individual LED regions, selection/resize/rotation/grid; native hardware geometry is inspected/configured in Devices, never mistaken for a screen region. |
| Devices | Replace shallow hardware cards with selectable native details and contextual mode/zone/driver controls; retain topology shortcuts, availability and Identify. Place rescan and native profiles here. |
| Settings | Replace the ordinary pipe connection form with integrated engine/application lifecycle; keep preferences and diagnostics access. SDK server remains supported by OpenRGB. |
| Preview | Keep live capture, submitted LED overlay, spatial blur and animation playground. No second capture/output writer. |
| Diagnostics/Help | Explain the single process, output ownership, actual capabilities and recovery. Retain journal and authenticated external diagnostics. |
| Tray/shortcut | One tray, show/hide Office UI, return from tests, exit entire app; sign-in stays hidden. |

Use existing Orbitron/Rajdhani typography, Material Symbols, dark cards/cyan
controls, accessible names and responsive scrolling. Verify real app-owned
renders at 1000x700, 1440x900 and 1920x1080; relevant 150%/200% scaling and
hardware detail states must remain usable. No desktop takeover is required.
Preserve office-ambience.json and LightBulb configuration during migration.

29. COMPLETE — Implement and integrate R27/R28 as a complete single-process
    workflow, including contextual native device controls and independent output.
    Acceptance: focused lifecycle/removal/mode/rest/profile/UI regressions;
    rendered design evidence; one real integrated owner with unchanged topology,
    live capture and observed hardware availability; GUI isolation demonstrated.
    Verified native CI 42113774830 and Ambient CI 42124655464. Actual unified
    renders cover all seven pages at three sizes and 100/150/200% scaling, plus
    four hardware tabs for each controller. Real editor group/rotation/name
    Save/reload preserves the exact original settings digest. Live native mode
    handoff, stale identity rejection, profile Save/Load, six-device rescan and
    native-selection persistence across restart passed. Repeated Show activation
    reused the sole process. Worker tests prove output while the GUI is stalled,
    synchronous removal and actual teardown. Main-display preview and all six
    controllers verified; 14.83 FPS, 0.373% total CPU, 99.3 MiB working set in an
    8.5-second hidden-UI observation. Evidence: local validation/20261106/unified-r2.
    No remaining blockers.
    No tracked deferrals.
30. COMPLETE — Deliver normal 0.8.0 from the verified integrated result;
    independently retrieve/check package and source provenance, activate the
    one-app startup/shortcut/tray, preserve settings, retire obsolete release and
    disposable artifacts transactionally.
    Published normal release v1.1-office.0.8.0 targets
    a4e19a86b0f4f419e965757d6bdb4ca99a751463. Independently downloaded ZIP
    SHA-256 b0f0f4c73de2203f75a96b457164c85934283d51c92ad094085df7ef2d78f336
    matches the published checksum, GitHub asset digest and installed manifest.
    All 117 payload members were verified on installation; native/plugin/runtime
    provenance and rejection of corrupt packages passed before publication.
    Official releases/1.1-office.0.8.0 is the sole installed release. The loaded
    plugin, desktop shortcut and startup binding resolve to it; no separate
    OfficeControl process or executable is delivered. Scheduled cold start and
    existing-owner reuse both completed with result 0 in the interactive session,
    without a visible window, service or settings changes. Main-display capture
    returned fresh wallpaper imagery at 14.98 FPS with all six controllers online.
    No new physical lock/display or Windows reboot test is claimed.
    Candidate r2 and obsolete 0.7.5 installation were removed through transactions
    6d63a01c47256aafd96f8a8efa0ce5fa and e864cec4d82ccd5ccc785eaade531b21;
    scratch transaction 4411e7ea4027a9dd25a4690b3fbf6e3e also completed with no
    residuals. Required delivery/acceptance receipts remain under local
    validation/20261106/unified-r2. The prior ZIP remains a defined recovery
    package under packages; private state and ongoing runtime scratch are retained.
    No remaining blockers or tracked deferrals.

Completed task scratch: E:/Temp/openrgb-primary-display-20261105, transaction
233478697ae060aaa348c6b5712fcb9d; candidate-office-0.7.3, transaction
da535003603a041f0750fb4552cf34cc; obsolete official 0.7.2, transaction
53280ea20dc448eb4fd06548f758bb28. All were removed after last use and verified
consumer migration to official 0.7.3. Persistent acceptance evidence:
D:/Tools/OpenRGB/validation/20261105/main-display.

Completed disposable work: E:/Temp/openrgb-idle-saver-20261105 (transaction
64911687cb030386e5d2e789094ec0a6), candidate-office-0.7.2 (transaction
792e317edbae9cf3305feed04ef934ae) and obsolete official 0.7.1 (transaction
ff74ae783d5d046022c85a4375574b96) were removed after consumer migration and
independent delivery verification. Persistent acceptance and CI receipts:
D:/Tools/OpenRGB/validation/20261105/automatic-saver.

Completed disposable work: E:/Temp/openrgb-draft-blur-20261105 (hosted build inputs
and package checks) was transactionally removed. Persistent acceptance:
D:/Tools/OpenRGB/validation/20261105/gui-0.7.1. The continuing owner/panel use
D:/Tools/OpenRGB/state-integration/runtime-temp independently of task scratch.
Completed disposable work: E:/Temp/openrgb-grey-context-20261104 was transactionally
removed after final release verification. Hosted Windows builds; no native host
build tree. Persistent verification: D:/Tools/OpenRGB/validation/20261104/gui-0.7.0.
Earlier disposable work: E:/Temp/openrgb-inverted-grid-20261104 was removed. No native host build
scratch is needed; compilation uses the existing hosted Windows workflow.
The exact spent native-82f150a2.zip/receipt inputs under the earlier
E:/Temp/openrgb-integration-20261104 were removed; other pre-existing investigation
material in that legacy directory was outside this cleanup. Native build scratch,
if required, uses D:/Temp/openrgb-integration-build-20261104 for I/O; prefer hosted
compilation to avoid host load. Keep runtime state separate under D:/Tools/OpenRGB.

## Integrated screen adjustment and tray — authorized 2026-11-06

Authorization: user requested LightBulb integration, corrected the exact tray menu,
then said "go ahead". The user also requested adding upstream LightBulb changes
to the existing monthly maintenance task. Scope is already_authorized, including
normal verified final release and necessary local activation/startup migration.

R29: Integrate LightBulb's functional screen controls in the existing native Qt
Office application: day/night temperature and brightness, location-based/manual
sunrise/sunset, transition duration/offset, smoothing, fullscreen/application
exclusions, editable global hotkeys, offsets/reset and cycle preview. Adapt the
actual MIT source at Tyrrrz/LightBulb f74285784be7bc191872c06b1b5e644eb209b98b;
retain attribution, exact source pin and a feature/source map. Keep one application,
one tray and the existing dark/cyan design; global startup/update/UI preferences
belong to Office settings rather than a second application's updater or tray.

R30: Display gamma is owned once, on the existing worker, independently of RGB
capture/output and GUI responsiveness. Apply to the connected displays as LightBulb
does. Preserve native gamma baselines, restore safely on graceful exit, handle
display/power/session/timezone changes, surface failures and avoid competing gamma
writers. Do not copy unexplained timed retries. Keep actual applied screen brightness
separate from RGB's manual baseline; integrated brightness following must apply
the dimming factor exactly once, including static frames. Preserve hue behavior.

R31: Use the official LightBulb bulb icon for the tray and unified application.
Exact top-level tray menu: Open; Disable lighting submenu; Disable screen adjustments
submenu; separator; Exit. Both submenus provide Until enabled again, Until sunrise,
1/5/15/30 minutes, 1/3/6/12 hours and 1 day. When disabled, offer the corresponding
Enable action. No Screen wrapper or extra Open/Exit wording. Disable lighting
blacks all owned RGB outputs (including selected native effects) while preserving
maps, device modes and baseline; resuming restores the selected owners. Screen
disable follows the configured neutral/daytime behavior. The two pause states are
independent; screen fullscreen exclusion never disables Ambilight app capture.
Explicit duration/deadline behavior must survive restart and handle system clock,
timezone and sleep/resume changes deterministically. Lock/display/saver black
output continues to take precedence over manual RGB enable and temporary tests.

R32: Import the user's existing LightBulb settings, including location, exclusions
and hotkeys, without overwriting the source settings or Office topology. Current
LightBulb 2.7.2 source a23b129 uses 6600K day/night, 100%/85% brightness, automatic
solar times, 3-hour transitions and fullscreen pause. Verify actual local values
at migration. Retire the separate LightBulb runtime/startup binding only after
the integrated candidate is verified; preserve a concrete rollback to standalone
LightBulb and Office 0.8.0. Never silently elevate or change system gamma-range
policy. Do not publish private location, settings, tokens or captures.

R33: Extend the existing monthly-openrgb-upstream-maintenance heartbeat to monitor
and implement compatible Tyrrrz/LightBulb upstream changes in this native integration,
alongside both Office forks. Track the incorporated pin and adaptations. Preserve
its timing, destination, status, quiet/no-change behavior, signing/provenance checks,
verified release requirement and existing branch-retirement safeguards. Preserve
current Windows-main-display capture behavior (supersedes old LG-only wording).

R34: Verify complete integrated feature behavior: source-derived solar/cycle/gamma
contracts, imported settings, all pause choices and independent owners, persistence,
hotkeys/exclusions, real gamma readback/restoration and live RGB output without
double dimming. Verify actual app-owned Screen/tray renders at 1000x700, 1440x900,
1920x1080 with representative 150%/200% scaling and accessible labelled controls.
Use existing hosted Windows checks and diagnostic IPC/offscreen exports; no desktop
takeover or extra RGB/gamma writer. Retain focused evidence and clean expendable
scratch through transactional-cleanup. Deliver a normal verified 0.9.1 release
(superseding the 0.9.0 candidate whose delivery exposed an inherited SDK shutdown
defect), independently retrieve/check it, activate one-app startup and verify delivery.

31. COMPLETE — Complete integrated Screen controls and independent tray pauses
    (R29-R33, feature verification R34). First real workflow: imported schedule →
    native display gamma → applied brightness → RGB follow exactly once, controlled
    by the Screen UI and exact tray menu. Finish all required controls, ownership,
    lifecycle and migration preparation before acceptance validation. Verified:
    Windows build 42216299806 at Ambient 322da9f; source-derived policy and native
    UI/lifecycle regressions; exact imported settings; 100/150/200% actual Qt
    renders; all pause choices and real output independence; two-display gamma
    readback, native event/hotkey/exclusion paths and exact exit restoration;
    persistent deadlines/offsets through native restarts; complete cycle preview;
    live main-display capture and existing topology Save/restore. Local evidence:
    D:/Tools/OpenRGB/validation/20261106/screen-0.9.0. User made the screen available
    and authorized killing standalone LightBulb; exact native PID/start/path/version
    was broker-verified before its exit. Original settings/startup/app preserved.
    R33 automation updated/read back. Reopened during delivery: final candidate
    stop exited 0xc0000005 after completed gamma/capture teardown. Dump plus source
    identifies SDK accept(-1) converted to unsigned SOCKET, missed by '<0'; invalid
    client destruction skips sender join, freeing its mutex beneath the thread.
    That blocker is resolved by native 56a094a, compiled run 42220324884 and
    matching Ambient691b57b/run42220395237; additional actual SDK-to-Govee graceful
    teardown run42222210668 passed. Real Office host verification of no/idle/
    disconnecting SDK clients exited zero each time and restored exact display
    baselines. Fresh Screen/gamma/map checks and current app renders passed;
    unchanged source retains earlier capture/hotkey/exclusion/preview/DPI evidence.
    Evidence: D:/Tools/OpenRGB/validation/20261106/screen-0.9.1. No blockers or
    tracked deferrals.
32. COMPLETE — Final 0.9.1 patch delivery and activation (R32/R34). Stage31 passed.
    Published 0.9.0 is explicitly prerelease/not-latest after failed local shutdown
    acceptance; its tag/assets are preserved. Normal 0.9.1 delivers the corrected
    complete outcome. Verified normal/latest release v1.1-office.0.9.1 points to
    ebceeac7164a3dd887cdee6d6f2ce3394b83b766. Independently downloaded ZIP hash
    143b9813102857eae1e880d3707d40ef490b9a39a8adf8ef21b023772fb6cd3c matches
    published asset/checksum. All installed members, exact loaded native/plugin,
    cold quiet sign-in, real main-display capture, six devices/314 LEDs, both
    display gamma ramps, imported settings and unchanged map passed readback.
    One process/tray remains; standalone LightBulb Run binding retired after
    acceptance, original application/settings and concrete rollback retained.
    Commit/push verified sources; publish normal package with licenses/source pins;
    independently download and verify package, activate one-app startup, retire
    standalone LightBulb startup/runtime after acceptance, verify rollback and
    package behavior, and clean spent scratch. All those criteria passed. Three
    exact D candidates, spent debugger cache/original OS dump and E task scratch
    were transactionally removed after consumer exit; required local evidence,
    published packages and rollback remain. No blockers or tracked deferrals.

## LightBulb visual controls and integrated window header (2026-11-06)

Authorization: already_authorized by the user's requests to incorporate LightBulb's
rotating GUI elements and Helium-style window controls. Preserve R29-R34 and all
existing capture, gamma, topology, tray and startup ownership contracts.

R35: Adapt the actual pinned LightBulb DashboardView sundial, Arc/ArcPoint and
cycle-state icon behavior into the native Screen page. Show day/night/transition
arcs, the moving current-time marker, effective time, sunrise/sunset, applied
temperature/brightness and day/night/transition/paused/disabled cues. Full-day
preview must drive the same owner's clock and settings as gamma, never a second
independent simulation. Add temperature/brightness slider companions to the
existing exact-value controls. Preserve keyboard operation, save semantics,
private imported settings and offset reset. Keep source/license mapping current.

R36: Integrate minimize, maximize/restore and close into the existing 48-DIP header,
following the user's Helium reference. No separate OS title strip. Preserve real
Windows caption drag/double-click/system menu, all resize edges, work-area bounds
on maximize, Windows snap hit testing, keyboard access and existing close-to-tray/
unsaved-change/Exit behavior. Interactive header controls must not become drag
regions. Retain the native window taskbar identity and one process/tray.

R37 (explicit user clarification, 2026-11-06): G502 mouse, Keychron keyboard and
Legion laptop lighting are optional when disconnected. Their absence alone must
not block delivery/maintenance or prompt for reconnection. Preserve their saved
maps and existing removal/reconnect behavior; do not disable their integration.
Wireless lighting availability (Govee H6609, Govee H8048, Nanoleaf/Secretlab MAGRGB)
remains significant for the delivery/maintenance check. This applies to stage34
and the existing monthly maintenance task; screen/gamma checks remain required.

Design contract: existing dark/cyan EDAmbilight rail, fonts and cards remain.
Use LightBulb's muted blue day, amber night and warm transition sundial colors;
180-DIP dial, legible state/time readouts and adjacent sunrise/sunset labels.
Caption buttons occupy 46 x 48 DIP each at the far right, with a red close hover.
Check actual native pages at 1000x700, 1440x900 and 1920x1080, plus 150/200% DPI.
Screen tabs remain scrollable at the minimum size. Motion must respect the existing
reduced-motion preference and stop when hidden; preview remains usable without
interpolation. No screen/gamma/capture lifecycle or scheduling redesign.

33. COMPLETE — Complete R35/R36 native UI integration and acceptance. Verify real
    owner-clock preview binding, rendered day/night/transition/paused states,
    slider/exact-value/save synchronization, hidden/reduced-motion lifecycle,
    caption hit regions and window actions, all size/scaling renders and unchanged
    real owner/settings/gamma/RGB state. Passed matching native0f2004caa4002542e4d548c47f2d88c6ecfdd264/
    build42230209667 and Ambient e30f9256394ab201809df8f0177e17befc80ebda/
    build42230279239. Native caption regression includes the actual shared launcher
    helper, snap hit regions, maximize/work area, restore, minimize, double-click,
    tray reopen and normal close. Actual host verifies all eight resize edges
    without changing visibility or desktop focus. Real app galleries at every
    required size/scale, real editor Save/restore, slider/exact-field saves,
    hidden/reduced-motion interpolation and rendered cycle states passed. Full
    owner preview completed natively at5999.87x; applied gamma matches its target,
    original map/settings/pauses/offsets/imported file remain preserved. Evidence:
    D:/Tools/OpenRGB/validation/20261106/screen-visuals-0.9.2. Closure assessment:
    cycle geometry and window activation each have one owner; no required debt,
    blockers or tracked deferrals remain for this stage.
34. COMPLETE — Deliver normal 0.9.2 after stage33, using R37 for device availability.
    Commit/push verified source,
    use matching successful native/Ambient artifacts (including native activation
    through the same Windows system-command path as the caption), independently
    retrieve/check published package/source/checksum/assets,
    install and cold-activate through existing startup, verify actual owner and
    loaded plugin, UI/gamma/devices/private-state preservation, and transactionally
    clean spent outputs. Record the final release receipt and rollback binding.
    Normal/latest0.9.2 published at source535947fb787f088d85df875cceea47ecde5ad7d6;
    downloaded SHA2567f4bbf9ff3f119c692f3f85d9c062a2f3f32c81e4f8479f72fdbff1bae9852a5
    matches published digest/checksum. All132 installed members and the actual
    native/plugin modules verified. Existing quiet sign-in task cold-started final
    root, result0, one headless owner101132, no standalone LightBulb startup/process;
    both-display gamma, capture, original configuration hashes and shortcut passed.
    Candidate and E scratch were transactionally removed with no residuals.
    Final reconnection readback: the same owner101132 reports6/6 online,314 LEDs,
    valid capture and both-display gamma. Original configuration digest comparison
    passed. Earlier4/6 observation was physical USB absence, now resolved; R37 also
    explicitly removes local-device presence as a delivery gate. The monthly task's
    saved prompt now distinguishes optional local devices from required wireless
    lighting; status, schedule, target and quiet notification intent are preserved.
    Stage/final debt assessment remains unchanged: no required refactoring,
    unresolved blockers or tracked deferrals. Shipped binaries/assets are unchanged;
    subsequent receipts/specification updates record delivery and user policy only.

## Main-display application awake policy (2026-11-06)

Authorization: already_authorized. The user reports Helium fullscreen playback
still triggering the automatic screensaver, asks to inspect PowerToys Awake, and
requires preventing screensaver mode whenever any app is maximized/fullscreen on
Windows' main display. Preserve R35-R37, private settings and the single owner.

R38: In the default Automatic mode, reuse the real main-display application selection for a native awake request.
Any visible, non-minimized, non-cloaked application maximized or covering the main
display qualifies, including Helium fullscreen without relying on browser media
signals or foreground focus. Floating/windowed apps, secondary-display-only apps,
desktop/wallpaper hosts and screensaver windows do not qualify. Release immediately
when the last qualifying main-display app is restored/minimized/closed/moved away.
Do not persistently change screensaver, lock, power-plan or user-input settings.

R39: PowerToys Awake source pin ba946c9885d189dda9b40e2990c5cbf3b4835bbc uses
SetThreadExecutionState. Microsoft's API documentation explicitly says that API
does not stop screen savers. Use the documented handle-scoped PowerCreateRequest /
PowerSetRequest DisplayRequired plus SystemRequired instead; Windows documents
that DisplayRequired prevents automatic screensaver activation. Scope requests
to the existing worker/process with deterministic clear/close on ineligibility,
lock, suspend/display-off/secure desktop, shutdown and constructor failure. Respect
manual sleep/lock and manually launched savers. Preserve existing automatic idle
rest (lights off) when no qualifying main-display app is present. No extra process,
tray, polling thread, synthetic input, persistent system setting or idle deadline.

R40: Verify the full native policy through real window/monitor selection and native
request acquisition/release, lifecycle events, optional local hardware, untouched
screen/power configuration and a real owner readback. Expose request state/error in
existing diagnostics and record source provenance. Required release is normal0.9.3,
with matching verified plugin/native sources, independently retrieved package,
installed/cold-started owner and unchanged state/rollback/cleanup guarantees.

R41 (user extension, 2026-11-06): Integrate the supplied PowerToys Awake tray
controls into an Awake submenu of the single Office tray: interval submenu,
expiration date/time chooser, indefinitely, Off (selected power plan), and Keep
screen on. Add Automatic as the initial mode for R38; an explicit manual mode
overrides Automatic. User clarification: place Automatic in this same Awake
submenu as the single control for automatic protection, rather than a separate
settings toggle. Off releases all Office awake requests; timed/expiration modes
return to Off when their user-selected deadline expires. Manual Keep screen on
controls display/screensaver inhibition; unchecked still prevents system sleep.
An unchecked manual mode retains its system-only request while the display is
off; R39's display-off release applies to Automatic and display-on requests.
Automatic always keeps the display on and disables that checkbox. Preserve the
existing lighting/screen pause submenus and Open/Exit behavior. Use PowerToys'
actual default intervals (30 minutes/1 hour/2 hours), importing this user's existing
KeepDisplayOn/custom interval preferences without changing their PowerToys files.
Persist Office awake mode/deadline/preferences separately and atomically, restore
valid active deadlines after restart, and expire past deadlines immediately.
The existing PowerToys Awake is currently Off under the shared PowerToys runner;
do not terminate or disable unrelated PowerToys utilities. New source reference
includes TrayHelper.cs and GetDefaultTrayOptions in Manager.cs. Verify real Qt
menu/dialog actions, checks/enabling, owner dispatch, persistence and expiry along
with R38/R39. Complete this extension before the single final0.9.3 release.

35. COMPLETE — Implement R38/R39/R41 and complete feature acceptance from R40: existing
    window selection → scoped native requests → restore/minimize/close/secondary/
    session/power transitions → deterministic release and preserved idle rest.
    Complete native manual modes/tray controls, persistence and explicit-deadline
    expiry. Focused actual Windows tests plus real installed owner/settings readback.
    Verified by Ambient fca2cdabfe1588366a504f2883f1cbb1407da987, successful native
    CI42247379089 (real private-desktop windows and independent powercfg request
    inventory), real Qt actions and all-scale packaged renders, live owner manual
    modes/expiry, actual cold-restart deadline restoration, unchanged settings/
    power preferences, valid gamma and required wireless availability. Evidence:
    D:/Tools/OpenRGB/validation/20261106/awake-0.9.3. No blockers or deferrals.
36. COMPLETE — Final0.9.3 delivery (R40). Publish once stage35 passes; verify
    actual release/assets/source, independently retrieve, install/cold-activate
    existing task/shortcut and read back actual owner/request/gamma/wireless state.
    Preserve maps/imported state and0.9.2 rollback. Clean spent scratch through
    exact-target transactions. No tracked deferrals.
    Published v1.1-office.0.9.3 at9678d98d13b05989a6cc9c5566fd581adbf86966;
    independent download SHA256f813da4e8434ad7e4f56fa5a1df5ed75c32f0493d671dd51d5d7915bac60be60.
    Both assets/source/normal publication verified; all137 installed members and
    the actually loaded plugin matched. Existing sign-in task cold-started one
    headless owner with result0, unchanged task policy and updated shortcut.
    Delivered owner passed manual modes/expiry, Automatic readback, preserved
    state and wireless/gamma checks. Exact cleanup transaction applied172 members
    /844156371 bytes with no residuals. Previous0.9.2 install/package preserved.
    Final R38–R41 reconciliation: all satisfied and verified; blockers0, deferrals0.

## Screensaver resume correction (2026-11-06)

R42: Fix the observed0.9.3 nighttime resume. At21:16:55Z Windows reported
Default/automatic_saver=false; at21:16:59Z output resumed while the user remained
asleep. The upstream cause of that Windows transition is unconfirmed; do not
change Windows/Wallpaper Engine settings or attribute it without evidence.
Once an automatic screensaver is observed, keep every device black and Awake
released until both a usable normal desktop and a new session input event have
been observed. Desktop/display/topology events, capture frames and elapsed time
alone must not clear this state. Preserve it across native app restarts through
separate atomic private runtime state. GetLastInputInfo is a session input signal,
not proof that input is physical; record only event timestamps/state, no keys,
window titles or device input contents. Query/storage failures must be visible
and must not permit unverified resume. Preserve manual screensaver capture,
manual lighting/screen pauses, gamma settings, topology and existing Awake modes.
After valid resume, discard pre-rest imagery and require a fresh captured frame.

R43: Regression verification must replay saver-active → Default without changed
input → display/topology changes → restart → unchanged input (all black/no Awake),
then changed input on a normal desktop → fresh capture/output. This no-input
state-clear condition is replayed in the Windows regression fixture; the natural
host cycle separately verifies actual idle entry, sustained black and input resume.
Include query
failure, first valid sample, non-incremental/32-bit wrapped input timestamps and
unchanged saved settings. Verify the integrated actual Windows owner on a natural
idle/screensaver cycle and actual input resume; diagnostic observations must not
synthesize input, alter the saver
timeout or introduce a second RGB owner. Verify black output state and controller
submission separately from unacknowledged physical hardware delivery.

Authorized verification scope change (2026-11-07): user requested "Just try to
fix it and we will verify with the logs next time" while actively using this PC.
Natural host idle/no-input/resume acceptance is removed from this release gate;
it remains explicitly unverified until a future real occurrence is reviewed.
Complete current regression/native-owner, packaging and delivery checks now.
Cancel the owned passive natural-cycle observer, retain its incomplete evidence,
and restore the original none lighting pause after the fixed delivery. The user's
"currently everything is off" confirms the temporary protection's physical
effect, not acceptance of the new automatic-rest policy. Do not attribute that
off state to the fix or claim natural-cycle verification was performed.

37. COMPLETE — R42/R43 complete correction and acceptance. Add one rest-state owner
    to existing source/output lifecycle and diagnostics, regression tests, real
    owner and preserved-state checks under the authorized verification change.
    Ambientd1de7eb4ea0b5b17db8fac65de813d87b4f75c77; CI42301506705 passed the
    recorded no-input Windows replay, actual power-request release/reacquisition,
    persistence/query/storage-failure and input-token cases. Candidate105940 had
    all141 files and loaded module verified, real control expiry, gamma, caption,
    wireless and unchanged settings checks. Original none pause restored. Native
    natural-cycle observer was cancelled at the user's instruction; no live
    natural-cycle acceptance claim. No current blockers or tracked deferrals.
38. COMPLETE — Single normal0.9.4 final release and delivery. Exact CI sources,
    package provenance, independent retrieval, installed/cold startup and loaded
    module checks, state preservation and required wireless availability. Preserve
    0.9.3 rollback, existing sign-in task/shortcut and cleanup guarantees.
    Published v1.1-office.0.9.4 at6dc070f63d9ca52de0328fe3c68c69bcde765af6.
    Independent asset download matched SHA256a9883ceb202a6d218d2a8431edfb67256b371ad4a7b416db73cc54138395e218;
    both assets/tag/source/normal publication verified. All141 installed files
    and actual loaded plugin matched. Existing sign-in task cold-started one
    headless owner107256 with result0 and unchanged Interactive/Limited/IgnoreNew/
    PT0S policy. Shortcut/root updated. Delivered controls/expiry, gamma, required
    wireless devices and settings/power preferences verified; original none pause
    restored. Cleanup applied182 members/671121970 bytes, no residuals. Prior0.9.3
    install/package preserved. R42/R43 satisfied under the explicit user scope
    change; no natural-cycle acceptance claim. Current blockers0/deferrals0.

## Unlock capture recovery (2026-11-07)

R44: Correct evidenced event-dependent recovery after unlock. Owner107256
received unlock at00:13:11.785Z, found no wallpaper through00:13:12.843Z,
and did not select it until00:13:22.806Z. First fresh frame followed at
00:13:26.267Z, including3.14 seconds recreating GPU resources and recompiling
unchanged shaders. While waiting for an eligible source, continue observation
on the existing output cadence without requiring an unrelated window event,
adding delays or churning unchanged source generations. Compile immutable shader
programs once per process; each capture retains its own device and image state.
Preserve R42: rest stays black, no stale image replay, fresh input when required
and a fresh captured frame before output. No Windows, Wallpaper Engine, Awake,
gamma, map, device or power preference changes.

R45: Verify event-free unavailable-to-available source recovery in the production
owner fixture, stable waiting diagnostics, actual fresh GPU capture across
independent capture states, and all rest/input regressions. Record real host
source/capture timing when available without locking the user's desktop,
synthesizing input or waiting for a manufactured idle cycle. Deliver one normal
versioned release with independently verified package, installed module, existing
startup and preserved settings. Physical wake latency remains subject to the
renderer making an eligible fresh source available; do not promise a fixed
deadline or call controller submission proof of wireless physical illumination.
The inactive Windows test desktop verifies discovery and an attempted native
capture; hosted WGC returns E_INVALIDARG there. Successful WGC creation/fresh
frames must instead pass twice on the actual installed interactive owner before
publication; retain that explicit boundary rather than treating the fixture as
proof of delivered images.

39. COMPLETE — R44/R45/R46 cohesive recovery correction and regression acceptance.
    Ambient0a9f4152e64d37a2645efd6b0d316fcd98aac8d4, CI42319811511 passed.
    Source readiness is observed without another event; unchanged waiting states
    retain their generation. Immutable shader programs are reused. Current-image
    span/center/tile/stretch/fit/fill positioning and production GPU output,
    manual pause, no-input black and fresh-image resume passed. Existing actual
    native request/lifecycle and GPU coverage passed. Inactive-desktop WGC
    limitation remains explicit; real frames belong to40. No blockers/deferrals.
40. COMPLETE — Single final release and installed delivery verification.
    v1.1-office.0.9.5 atb0e5a69fd01228df8167a9431cb7ddcfa9ca2d88; independent
    asset retrieval matches SHA256708b405d3d8667f50a487276d35f87232363005577ebe42e90825fe53bb3a13d.
    Negative installer/provenance checks and all146 installed members passed.
    Actual candidate/delivered owners submitted the static image before live
    frames and handoff; repeated fresh live capture measured444-758ms. These
    measurements are not natural unlock latency. Native module, preserved
    settings/gamma/wireless checks and existing sign-in task cold start passed:
    result0, one headless owner91040, Interactive/Limited/IgnoreNew/PT0S unchanged.
    Prior0.9.4 retained. No blockers/deferrals. User then stopped further live
    testing due disruption: no additional app/capture/wallpaper/lighting resets
    without a new request; review future normal-use logs instead.

R46 (user scope addition2026-11-07): Read the Windows desktop wallpaper image
first after a valid unlock/resume, using Wallpaper Engine's current Windows
override where configured, and submit its sampled colours before starting live
capture. Local Windows currently points to WallpaperEngineOverride_random*.jpg,
updated at00:33:30Z, with spanning enabled. Resolve the actual primary monitor
and Windows positioning through the supported read-only desktop-wallpaper API;
crop a spanning image to that monitor, preserving the existing region map,
processing and output settings. Switch to a fresh live frame as soon as one is
available. This explicitly permits a freshly read static wallpaper frame before
R42's fresh live frame; it does not permit replay of pre-rest screen imagery,
reading lock-screen imagery, or clearing the existing input/security/rest gate.
Keep wallpaper paths and pixels out of logs/packages. Report static-image versus
live-frame delivery separately, including unavailable/undecodable image failures.
Do not change Windows or Wallpaper Engine preferences. Add image positioning,
actual shader sampling, rest/paused-output and fresh-frame handoff coverage to39;
40 must verify the installed image-first path and live handoff before publication.

## Disabled-lighting capture lifecycle (2026-11-07)

R47: Disabling RGB lighting must release the live WGC capture session and its
GPU/preview resources, clear retained image input, and stop creating captures or
reading/sampling the wallpaper file while lighting stays disabled. Cover tray
lighting pauses, output pause and global ambience enabled=false. Re-enabling
lighting observes the existing rest/input gates and acquires fresh imagery.
Gamma/screen adjustment, Awake eligibility and native hardware ownership remain
independent. Pending preview requests must terminate with an explicit paused
state rather than silently restarting capture or waiting indefinitely.

R48: Preserve the startup-only static-image bridge: read the configured Windows
wallpaper file once, not through WGC, while the normal Wallpaper Engine pipeline
starts. Do not introduce a sustained/static-wallpaper capture session, repeating
polling reads, or a capture-duration timeout. The user's clarification refers to
this static bridge, not replacing normal animated RGB with frozen colours.

R49: No host lighting/capture experiments, screenshots or Computer Use for this
repair. Verify pause/re-enable/rest/preview and independent Awake/gamma behavior
on hosted Windows fixtures. Deliver one normal release, preserve current user
preferences, and activate it once through existing local startup/IPC scripts.
Observe installed status read-only, without toggling lighting or recovery tests.

Yellow-border isolation: user explicitly requested one stop. Ambilight PID91040
exited with capture_stop_complete02:55:24.857Z; user reported border remained.
Computer Use helper91732, created for this chat's settings operation, retained
capture after its UI closed. Node client reset did not close that helper; its
identity-checked stop at02:59:42Z removed the border, confirmed by the user.
Do not attribute this incident's border to Ambilight. Prefer app-owned controls;
no further Computer Use without an explicit request. Ambilight remained closed
until the verified final0.9.6 release was ready for its one normal activation.

41. COMPLETE — R47/R48/R49 cohesive lifecycle correction and hosted verification.
    Ambient054a6b95b25495a9e8b9d8228f1605c48757b4df, CI42332547954 passed.
    RGB/global pause releases capture/input and prevents source-generation or
    preview acquisition while disabled. Resume acquires fresh input; actual
    Windows Awake requests remain eligible during lighting pause. Existing
    gamma/rest/GPU/static-image coverage passed. Initial failed output fixture
    incorrectly reused pre-pause input; it now supplies a fresh post-resume row.
    No changes to the static file reader or WGC border policy. No blockers or
    deferrals; no additional architecture/refactoring work required.
42. COMPLETE — Final1.1-office.0.9.6 published normally at tag
    v1.1-office.0.9.6, source e39b30063eff7a91e8f5b0e8ea568c0a5d333875.
    Independent package retrieval matched SHA256
    6df47cfdbf820dc4073860313d1c9fd4bd191db5733ba054f230b8c42d988817;
    native/plugin provenance, all149 installed files and invalid-digest rejection
    verified. One existing sign-in task activation created owner70100; loaded
    executable/plugin paths and plugin hash matched0.9.6. Read-only IPC confirmed
    valid gamma, all required wireless devices and capture policy matching saved
    preferences. Private settings, screensaver and power plan hashes unchanged;
    startup remains Interactive/Limited/IgnoreNew/PT0S. No host feature
    experiments, screenshots, recovery requests or Computer Use.0.9.5 rollback
    retained. No blockers, tracked deferrals or required refactoring remain.
    Sanitized delivery receipt: office-validation/delivery-0.9.6.md.

## Global and per-device lighting intensity (2026-11-07)

R50: Add a global fullscreen lighting percentage shared by every app, not
per-app profiles. Default50%, range0..100%; multiply existing sampled brightness
and display-following gain only for a fullscreen application on the main display.
An ordinary maximized window does not trigger fullscreen dimming. Restore normal
intensity when fullscreen ends or the app moves off the main display. Preserve
Awake, gamma, rest/off gates, capture ownership and one-time static-file bridge.

R51: Provide a BetterTrumpet-style lighting mixer: top master percentage for all
mapped lights and one individual percentage/mute control per physical mapped
device, identified by stable device ID. Defaults100%, range0..100%; multiply
master * fullscreen factor * device factor. Muting preserves a useful prior level
for toggling back. Retain offline device settings and clearly show offline state;
reconnection uses the saved level. Do not add per-app rows or another RGB writer.
Persist only intended intensity changes atomically, guard against external file
edits and reject unknown devices/non-finite/out-of-range values before any write.
Do not silently overwrite unsaved topology/settings drafts. Calibration/identify
retain their reference colours; rest/disabled lighting still wins. Global mute
releases capture/input while keeping independent screen/Awake policies.

R52: Follow the supplied screenshot and inspected BetterTrumpet source:
FlyoutWindow.xaml/.xaml.cs, DeviceView.xaml, VolumeSlider.cs and FlyoutViewModel.cs.
Left-click the existing Ambilight tray icon opens a compact lighting flyout;
double-click and existing Open action still open the full panel, existing tray
menu actions remain. Include pin, collapse, keyboard-accessible sliders and
numeric percentages, icon mute/unmute, Escape and click-away dismissal unless
pinned. No sounds. Expose the same mixer from the main panel. User correction:
fullscreen intensity does not belong in the tray flyout. Put its one shared
control and actual active/inactive state in the main app's Output card. The
flyout contains only master and physical device levels. The original global-only
scope is superseded by the direct R57 request for per-app profiles in the main UI.

Design contract, revised by user feedback: retain BetterTrumpet's layout and
interactions while matching Ambilight's greenish theme. Native Qt, dark teal
body#081b18, header#10332c, border#28584e, light text#d4e6df and mint-green
slider/accent#45ddb0. Use existing Office Body fonts,15px device labels,
26px master percentage, visible focus. Base flyout width420 logical pixels,
12px rounded outline, 16px insets, 44px slider/mute hit targets, 72px device rows
with full names/tooltips. Content scrolls within available monitor work area;
anchor above/beside the tray and clamp within work area. Inspect app-owned hosted
renders at100/150/200% scale, expanded/collapsed and offline states. No host
desktop screenshots, Computer Use, synthetic fullscreen or lighting experiments.

R54: Modernize the existing tray context menu to match the greenish mixer palette:
rounded frame/hover rows, comfortable padding, legible existing app font, subtle
separators and coherent icons. Preserve Open, lighting/screen pause choices,
Awake options and Exit behavior, keyboard navigation and submenu semantics.
Include app-owned rendered menu evidence with the flyout acceptance checks.

R53: Verify the complete mixer UI -> production command -> saved preferences ->
native output path in hosted Windows tests: master/device/fullscreen multiplication,
normal restoration, offline reconnect, malformed input, stale external edits,
rapid slider updates, drafts and rest/pause. Release one normal0.9.7 package
after integrated acceptance; independently retrieve/hash it, verify installed
members/loaded plugin and one normal activation via existing startup task.
Preserve current settings except new authorized intensity preferences; retain0.9.6
rollback. Read-only host delivery verification only.

43. COMPLETE — R50/R51/R52/R54 integrated intensity policy, persisted commands
    and BetterTrumpet-style native mixer. Ambient497848b32682c1b523b78c34dda7a28ded59b3fc,
    hosted CI42399208049 passed. Actual sliders -> production command -> durable
    settings -> native output verified, including multiplication, normal restore,
    master mute/capture release, offline reconnect, malformed input and stale
    edits. Ordinary maximized/other-display windows preserve normal intensity;
    Awake/gamma/rest/identify remain independent. App-owned flyout/context-menu/
    Output-card renders reviewed at100/150/200%; green palette, rounded opaque
    surfaces, accessible hit targets and main-panel fullscreen placement verified.
    No host experiments. Shared persistence helper and one native mixer component
    serve current paths; no required refactoring, blockers or deferrals remain.
44. COMPLETE — R53 normal v1.1-office.0.9.7 published at source
    97ddebb62e52bf3b1fdfd692c9c4a0b74315794d. Independent downloaded ZIP matched
    SHA25632fe940b41b91478f20fdcb8402b1f8bf6dc1a49991ea371289f6a1cbc7d2b8c;
    all152 installed members and loaded plugin verified. One graceful old-owner
    exit and existing startup-task activation; read-only IPC confirmed intensity
    settings, all six devices online, valid gamma and expected capture policy.
    Existing settings, OS power/saver preferences and startup policy preserved;
    0.9.6 rollback retained. User confirmed working. Reviewed cleanup removed
    all55 temporary members,358963764 bytes; retained source-bound UI/log evidence.
    No blockers/deferrals or required refactoring. See delivery-0.9.7.md.

## Product-specific device icons (2026-11-07)

R55: User confirmed0.9.7 working and requested ImageGen in the next update for
proper icons resembling the actual products, replacing the generic physical
device symbols. Cover the six current IDs: Govee H6609 Gaming Light Strip G1,
Govee H8048 Gaming Light Bars Pro, Secretlab MAGRGB E72 desk lighting, Keychron
Q6 HE ISO full-size keyboard, Lenovo Legion Pro7 16IRX8H Gen8 (82WQ, read from
the host's model metadata), and Logitech G502 X PLUS. Use verified product
references; retain source URLs/hashes and exact generation prompts. Generate one
transparent, product-recognizable raster icon per device in a coherent miniature
style readable in the existing controller. No random category glyphs for these
known IDs. Keep the accepted green UI, row layout, mute controls and behavior.

R56: Embed/cache the selected icons in the native application by stable device
ID, independent of online status and display name. Verify all six distinct
resources, alpha/readability at actual widget/DPI sizes, real mute/slider behavior
and source-bound app-owned renders. Generate with built-in ImageGen as requested;
disclose each exact prompt and necessary reference inputs before calling it.
Do not access the desktop, run lighting experiments or recreate capture helpers.
The later direct R57 request authorizes its NuvioDV profile configuration only;
preserve unrelated lighting settings.
Release one normal0.9.8 after integrated icon and app-profile acceptance and independently verify the
published package and one normal installed handoff, preserving current preferences
and0.9.7 rollback.

45. COMPLETE — R55/R56 six manufacturer-referenced ImageGen assets embedded by
    stable ID at Ambient1311e0a50a7c52a31153d2f0f28e1de69eaa8242. Hosted Windows
    CI42402635913 passed all required production tests. Six distinct embedded
    hashes/transparent sources and40px miniatures verified against provenance;
    rename/offline identity and real mute/restore/slider paths passed. Reviewed
    actual app-owned renders at100/150/200%: recognizable complete products,
    accepted green layout/hit targets preserved. Bounded192px CPU image cache;
    no runtime download or external asset path. No blockers, deferrals or required
    refactoring. Final source-bound package delivery remains assigned to stage47.
R57: Additional direct user request during icon implementation: per-fullscreen-app
lighting profiles, including independent physical-device intensities. Normal
wallpaper uses normal master/device levels; a NuvioDV fullscreen profile can set
both Govee devices to30%. Edit profiles in the main application, retaining the
tray mixer's master/device scope. Match a deterministic app executable identity;
Identity is the case-folded Windows executable basename, deliberately covering
all instances and surviving version/install-path changes. Profile levels override
the shared fullscreen percentage for selected devices,
rather than multiplying30% by the existing50% default. Master/device adjustments
still apply. Unconfigured devices/apps retain the existing shared fullscreen
policy; exit fullscreen, switching apps or moving to another screen restores the
appropriate policy. Rest/disabled lighting and independent gamma/Awake win as
before. Persist profiles atomically with settings and guard drafts/external edits.
Verify production window identity -> profile selection -> native device output,
profile editing/persistence and restoration in hosted tests. Configure the actual
installed NuvioDV executable's H6609/H8048 profile to30%, preserving other choices.
No host fullscreen/lighting experiments. One combined final release only.

46. COMPLETE — R57 integrated native profile selection/settings/UI at Ambient
    4822d03a6a4989bdfeb2cd8c36fefbfaecc5c789, hosted CI42404653752 passed.
    Actual Windows fullscreen window -> executable -> saved profile verified;
    editor controls -> durable native command -> device output demonstrated.
    Govee30 overrides shared50 (not15), master/device multiplication, defaults,
    app/fullscreen/display restoration, restart, stale drafts, external edits,
    rest blackout and all-device mute/capture release passed. Actual profile UI
    reviewed at100/150/200%; existing visible vector controls reused with mint
    arrows, product icons and accessible names/hit targets. Main Output entry and
    cancel/draft behavior passed. No implementation blockers or required refactoring;
    shared OfficeInputs.h removes duplicate input behavior for these existing paths.
    Tracked delivery work: configuring the actual NuvioDV profile belongs to
    stage47's single normal installed handoff, after the combined release passes.
    Verify its durable/runtime H6609/H8048=30 readback and preservation of every
    unrelated preference there; stage46 acceptance uses the complete hosted app.
47. COMPLETE — R55-R57 normal v1.1-office.0.9.8 published at root/tag
    7de0a25990f40a4caec43c01373f234853fcf2d6 with Ambient4822d03a6a4989bdfeb2cd8c36fefbfaecc5c789.
    Independent GitHub metadata/tag/download/checksum matched ZIP SHA256
    bf1c2790a6c4f4581ae076bbd393e33c1581681c361d650aff89763061b1966d.
    All154 installed members and loaded plugin verified. One graceful0.9.7 exit
    and existing task activation; one headless0.9.8 owner. Tracked R57 delivery
    resolved: installed NuvioDV.exe profile durably/native-readback H6609/H8048=30,
    master100/default fullscreen50 and unrelated preferences preserved. Actual
    automatic screensaver was active during read-only verification: every mapped
    light black, capture absent; wireless devices/gamma valid. No host experiments.
    Startup policy and OS power/saver settings unchanged,0.9.7 rollback retained.
    Reviewed cleanup removed32 temporary members/395266650 bytes, no residuals.
    No remaining blockers, deferrals or required refactoring. See delivery-0.9.8.md.

## Collapsed tray anchoring (2026-11-07)

R58: User screenshot shows the collapsed mixer floating at the expanded panel's
old top edge. Retain the opening tray/button anchor and recompute position after
layout changes, so collapse and expansion preserve the same lower/right edge and
existing tray spacing. Reopening collapsed and normal snapshot refresh must keep
the panel attached; preserve work-area bounds, pinning, controls and all settings.
Verify actual production-widget geometry through collapse/expand/refresh/pin and
app-owned renders at100/150/200%. No host desktop access or lighting experiments.
Deliver one normal0.9.9 release, independently verify package and one installed
handoff, preserve current NuvioDV/device settings and0.9.8 rollback.

48. COMPLETE — R58 at Ambient2605c45fa9bf3a1a9866c36f87ff864c5a61bcdd,
    hosted Windows CI42406805010 passed. fit() now recomputes position from the
    opening anchor after sizing. Actual widget bounds expanded[380,97,420,625]
    and collapsed[380,553,420,169] share bottom/right[799,721]. Collapse, refresh,
    collapsed reopen, expansion and pinned resizing passed. App-owned100/150/200%
    renders reviewed; existing appearance/controls preserved. No blockers,
    deferrals or required refactoring; one shared fit path owns placement.
49. COMPLETE — R58 normal v1.1-office.0.9.9 published at root/tag
    d52586d912f41f9df3b2d69971fc6d66e6155cb6, Ambient2605c45fa9bf3a1a9866c36f87ff864c5a61bcdd.
    Independent metadata/tag/download/checksum matched ZIP SHA256
    427ab59aabb6955ac02fd908d2d458bfe728c0fec91fa7b2734b639917a99fd3.
    All156 installed files and loaded plugin verified. One graceful0.9.8 exit
    and existing task activation; saved app/profile/settings files and OS power/
    saver preferences unchanged. Wireless/gamma/read-only capture policy checks
    passed;0.9.8 rollback retained. Cleanup removed21 expendable members,
    394350275 bytes, no residuals. No blockers, deferrals or required refactoring.

## Frosted lighting widget (2026-11-08)

R59: Add background blur to the lighting flyout like the original BetterTrumpet
reference. Use native Windows background acrylic, retaining the green tint,
opaque/readable text, product icons, 420-DIP layout, rounded silhouette, controls
and corrected tray anchoring in expanded/collapsed/pinned/reopened states. Do not
blur the controls themselves. Respect Windows transparency/high-contrast choices
without changing them; retain the existing opaque green surface when effects are
disabled or unavailable. No screen sampling, CPU wallpaper blur, timer, extra RGB
writer or background resource while the flyout is hidden.
This supersedes the earlier opaque-background rule only while native acrylic is
active; the opaque fallback remains unchanged.

Implementation decision: follow BetterTrumpet4a76efd34a1aa38b1b006251cfa9e18be1b1604b,
FlyoutWindow.xaml/AccentPolicyLibrary.cs/App.xaml. Its transparent layered popup
uses ACCENT_ENABLE_ACRYLICBLURBEHIND with a70% tint. Qt6.8.3's Windows raster
backend likewise requires WS_EX_LAYERED for this existing translucent frameless
widget. Use that same narrowly scoped user32 accent policy instead of replacing
the Qt window/composition pipeline to use the newer non-layered DWM backdrop.
Apply/remove only on this owned HWND; reapply on show/pin/native preference changes.
Keep rounded clipping with native/DPI-aware widget mask and nonzero body alpha
for input hit testing. Native failures use the explicit opaque policy fallback.

Verify real native policy acceptance/lifecycle and compositor output against a
generated CI-owned background; app-owned widget renders alone do not prove OS blur.
WCA_ACCENT_POLICY cannot be retrieved with GetWindowCompositionAttribute: a hidden
owned-HWND ABI probe confirmed Set succeeds but Get fails withERROR_INVALID_PARAMETER
on the installed Windows11 as well. Record actual Set acceptance (not invented
readback), and prove both high-frequency blur and retained low-frequency background
colour with compositor pixels. This replaces an unsupported diagnostic method
while preserving the required observable blur.
Review expanded/collapsed100/150/200% renders, opacity/legibility, corner clipping,
pin/reopen/anchor and existing interaction checks. No user-desktop capture or
live lighting experiments. Final normal0.9.10 release, independent package/source/
hash verification, one installed handoff, preferences preserved and0.9.9 rollback.

50. COMPLETE — R59 native acrylic, transparency preference/lifecycle integration,
    real native compositor verification and existing widget/geometry acceptance.
    Ambient a95d7cf, successful hosted CI42421723208. Native composed pixels reduce
    stripe contrast61.0 to0.785 while retaining red/blue background fields; real
    Set acceptance, layered HWND, rounded mask, pin/hide/reopen and unchanged tray
    anchor passed. Reviewed native and100/150/200% widget renders; controls stay
    sharp, offscreen fallback remains opaque. Evidence: validation/20261108/acrylic.
    Closure assessment: one owned-HWND material lifecycle, no duplicate writer,
    timer or capture; no required refactoring, blockers or tracked deferrals.
R60: User also questions repeated access to
D:/Tools/OpenRGB/state-integration/office-ambience-status.json (exact filename
clarified by the user). Trace readers/writers and their current purpose after
unification; remove evidenced redundant continuous status I/O without breaking
required diagnostics, startup readiness or external consumers. Explain actual
purpose and resulting change. No invented maintenance file or unrelated schedule
change. Verify affected diagnostics/readiness and preserve useful failure logs.

51. COMPLETE — R60 status-file access investigation and required bounded
    correction, with affected reader/writer/readiness verification.
    Root cause: native status() atomically rewrites the complete report every
    second. Unified UI already uses in-process snapshots; no active external
    observer found. Keep one-second in-memory FPS measurement and ten-second
    health logs, publish disk checkpoints on semantic state changes only. Frame
    counters, input ticks, brightness/temperature ramps and timing samples do not
    trigger writes. Keep readiness/gamma/error/pause/source changes and requested
    preview-completion notifications. Manual frame observer and one-time legacy
    migration read authenticated live snapshots instead of stale file counters.
    Verify stable bytes across volatile progress, live IPC counters, semantic
    changes, publication failure/recovery and existing readiness/preview paths.
    CI42422813579 compiled and passed native blur; checkpoint fixture failed at
    construction because it omitted five devices required by fresh bootstrap.
    Corrected fixture inventory in bb7dba4 without weakening the production gate.
    Corrected source bb7dba4e52f01171c8edfb3131d616d0e6c0028a passed hosted
    CI42423239290: stable file bytes during counter/input/timing progress, fresh
    command snapshot/FPS, screen-ramp filtering, readiness/pause state selection,
    real pause/error checkpoint and failed-save recovery. Existing lifecycle,
    preview, runtime, UI and compositor checks pass. Hardware-free observer
    progress/owner-exit/identity checks and migration PowerShell parse passed.
    Closure assessment: existing owner remains sole state publisher; optional
    reader uses existing authenticated IPC, no new background job or transport.
    No blockers, deferrals or required refactoring. R59 is unchanged and its
    native compositor proof also passed in this exact combined source run.
52. COMPLETE — final0.9.10 release, independent retrieval, one installed
    handoff/read-only preservation checks and expendable-artifact cleanup.
    Normal published v1.1-office.0.9.10 points to1b2e552fa651551558934ffb79d804785011f6b0.
    Independently downloaded ZIP matches published SHA256
    9d9db8fa7f2380cbf30846c131efa0f7aaa7341b933d2c400c3cd0922f9424d0.
    All159 installed members verified; native owner163772/startUtcTicks
    639296897868668228 loads the exact0.9.10 module (SHA14780334518DA634E6B4B37BC2B6D3050F0FDDF4DD544E90EDE880C5547D7197).
    One graceful shutdown and one existing-task activation; startup/shortcut,
    headless single owner, wireless availability, gamma and capture policy pass.
    App/profile/settings and OS power/saver preferences preserved. Live output
    advanced35 frames while checkpoint bytes remained unchanged. Effective master
    100/shared fullscreen50, device levels100 and Nuvio Govee30 remain intact.
   0.9.9 rollback retained. Exact reviewed cleanup removed29 members/395529666
    bytes, no residuals. Delivery receipts: office-validation/delivery-0.9.10.md.
    Final reconciliation: R59/R60 satisfied; prior delivered requirements remain
    preserved. No blockers, tracked deferrals or required refactoring.

## First-open lighting widget corruption (2026-11-09)

R61: The first lighting-widget opening after it has been hidden must render the
whole current viewport correctly, without requiring a second opening. User's
150%-scale screenshot shows a630-pixel window with content cut off at420 pixels
and missing right-side controls/footer. Preserve native acrylic, rounded corners,
420-DIP width, tray attachment, scrolling, pin/collapse/reopen, device artwork,
settings and intensity behavior. No periodic repaint, arbitrary delay, automatic
reopen, desktop capture or live lighting/wallpaper experiments.

Investigation: installed0.9.10/bb7dba4 is unchanged. Read-only owned-HWND probe
finds630x935 physical pixels at144 DPI. Hidden setState skips fit(); showAt calls
show before fit(), while showEvent enables acrylic and clips the old rectangle.
Native tests repaint/collapse before compositor observation and only simulate
100/150/200% through image exports, missing native first-show presentation.
Resolve geometry/layout before showing; apply material to the final surface,
and verify the actual first queued paint rather than forcing a corrective repaint.
Keep DPI/surface lifecycle synchronized and no work while hidden.

53. COMPLETE — R61 source correction and native first-show regression
    checks, including real150% native composition, hidden inventory changes,
    first/reopen, pin/collapse and viewport/anchor preservation. Source inspection
    closes this stage; compiled acceptance is assigned to54.
    Source inspection: showAt binds QWindow screen, polishes/activates layouts
    and fits the hidden window before showEvent applies acrylic/clip. Hidden
    state refreshes do not run fit. Native tests observe actual Show geometry,
    queued paint coverage and composed right-slider/footer pixels, with hidden
    inventory changes and a hidden main-window owner. Separate real150% CTest
    writes isolated evidence. Existing geometry/material/interaction tests remain.
    Whole-scope source ready for validation: OfficeLightController.h,
    tests/office_window_tests.cpp and CMakeLists.txt; no known source gaps.
    Build/acceptance unexecuted at this boundary. Launch established hosted
    Office Windows workflow after committing this cohesive source. No separate
    local app launch, host capture or new gate/runtime required. No refactoring
    finding or tracked deferral; exact correctness remains stage54 acceptance.
54. COMPLETE — integrated hosted Windows validation of the whole source change;
    first composed pixels and native geometry/material evidence before any manual
    repaint, representative scale renders and existing interaction checks.
    Attempt42642784185/b38baa5 compiled but both native first-frame checks
    found geometry changing during first queued paint; no release/candidate
    activation. Existing offscreen and engine tests passed. Source correction:
    material transitions no longer replace header stylesheets (which invalidate
    fonts/layout); parent paint owns header tint without geometry mutations.
    Related first-frame assertion now reports exact prepared/settled rectangles.
    Cohesive failed-attempt correction ready for revalidation after inspection;
    source changes only OfficeLightController.h and the native diagnostic text.
    Attempt42643686778/ae38a54 disproved stylesheet replacement as the source of
    the size jump:100% prepared420x512 then623 high;150% prepared420x341 then623.
    These match QWidget::adjustSize's documented2/3-screen height cap exactly.
    Removed that speculative paint refactor. fit now derives chrome and capped
    viewport directly from layout size hints, activates final constraints and
    explicitly resizes before show, including collapse. No adjustSize remains
    in the flyout. Qt6.8.3 qwidget.cpp adjustedSize() confirms the mechanism.
    Original failed attempts/logs retained; cohesive geometry correction inspected
    and source ready for affected native/offscreen validation, same R61 scope.
    Attempt42644943318/1928244 compiled;100% retained a24px deferred height
    change, while150% passed geometry/right-slider but failed visible footer.
    Retained first native PNG shows an oversized viewport extending below the
    CI screen. The outer hidden layout was reading cached descendant hints;
    activate() on only outer/deviceRows does not measure nested QWidget layouts.
    Correction settles widget layouts bottom-up before natural measurement and
    again after assigning the bounded viewport. Material tint is painted without
    changing header stylesheet, eliminating layout mutation after preparation.
    This reconciles the two measured causes rather than retaining a workaround.
    First-frame diagnostics now retain child hint/constraint/bounds with failures.
    Same acceptance criteria; no timer, delay, automatic reopen or forced repaint.
    Whole cohesive source correction inspected and ready for revalidation.
    Source3588c395e11f8723fc8e1857e58b6f67b73a64b1 passed CI42646493749.
    First show and reopen keep identical prepared/presented bounds:420x623 at
    100%,420x473/630x710 physical at150% with bounded scrolling. First composed
    frames contain right-slider121 green pixels and footer272/529 text pixels;
    no manual repaint or second-open repair. Reviewed native PNGs at both scales.
    Existing widgets, pin/collapse/anchor and real acrylic compositor checks pass.
    Source-bound UI artifact13687627601 SHA114c76a19823108b6ea63c71e2013781a9d4fcfa556c97d000307e76fe36cb58.
    Closure assessment: one pre-show layout path; no periodic repaint, retry,
    arbitrary sleep, automatic reopen or hidden-background resource. Header tint
    stays paint state. No blockers, tracked deferrals or required refactoring.
55. COMPLETE — normal0.9.11 release, independent download/hash/source checks,
    one final installed handoff with preserved preferences and0.9.10 rollback,
    read-only installed verification and transactional scratch cleanup.
    Published v1.1-office.0.9.11/source cd2108e41486c281bdeb649ee0eef3d10321438c;
    independent download, tag and checksum match SHA256
    714dd391a34d2ee716a8736169ffbecba864d55a36de1e739a17dc2587fef066.
    All161 installed members read back; owner21712/start639298360023408409 loads
    plugin F22DAF58B1614ED0F865BC493C1D5C81628D6F667FB8712E98E285835F09B114.
    One graceful old-owner shutdown and one existing-task activation with result0.
    Wireless/gamma/current capture-policy and saved settings/OS preferences pass;
    effective master/device/fullscreen/app-profile levels match pre-handoff values.
    App settings hash8870C7B6149EECEE3761D0E6BEC60AF52132ACFF26549C0482D4853289B5846F.
    User-host widget was not opened/captured for testing.0.9.10 retained for rollback.
    Cleanup removed26 reviewed members/396331772 bytes, no residuals. Final
    reconciliation: R61 satisfied; no blockers/deferrals/refactoring required.
    Delivery receipt: office-validation/delivery-0.9.11.md.
56. COMPLETE — 0.9.12 QA and future-proofing (Claude Code takeover of the
    Codex thread). Requirements: (a) Govee H6609/H8048 recover their DreamView
    stream session without user action after network/firewall interruptions;
    (b) firewall/GlassWire rules survive releases: the active release runs from
    one stable executable path D:/Tools/OpenRGB/app (Activate-Release.ps1), with
    versioned releases kept for rollback; (c) caption drag/resize work even when a
    descendant widget owns a native HWND; (d) reviewer QA fixes (CPU: cached
    LightBulb process probe; capture retry; safe rebind; gamma crash baseline;
    socket/buffer bounds). Acceptance: CI green with the native-child caption test,
    published/independently verified package, installed at the stable path and
    started by the existing task, single owner ready, output-thread CPU below the
    0.9.11 sample, no live lighting experiments or Wallpaper Engine restarts.
    Result: all acceptance met (output thread 3.3% vs ~52%; 6/6 devices; task
    result 0 at the stable path). Remaining inferred: whether sends fail during
    firewall interruptions. Delivery receipt: office-validation/delivery-0.9.12.md.
57. IN PROGRESS — 0.9.13 Day/Night per-light night levels. Requirement (user,
    2026-11-11): lights currently follow the screen's night brightness (~85%);
    Govee lamps need a stronger night reduction (~50%), so each device gets its
    own gradual night level; the Screen page becomes "Day/Night". Decision: each
    light either follows the screen (default, unchanged) or has its own night
    level, fading 100%→level along the screen's sunrise/sunset transition curve
    and smoothing (cycle position 0→1); screen pauses return lights to day.
    Persisted as device_night_level; owner intensity command target "night".
    Acceptance: Ambient CI green with policy/owner/widget tests for the night
    position, gain, persistence, validation and the Lights tab; published and
    independently verified package; deployed to the stable path; single owner
    ready with settings preserved; no lighting experiments.
