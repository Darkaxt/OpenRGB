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

27. ACTIVE — Implement R26 through native output and panel controls, focused
    regression tests and live validation of gamma reads/static-input dimming,
    unchanged baseline/topology, test/rest behavior and resource use. Read-only
    probe observes primary DISPLAY2 at 0.86073 with linear equal-channel ramps.
    Remaining blocker: integrated feature and acceptance checks not yet complete.
    No tracked deferrals.
28. NOT STARTED — Deliver verified 0.7.5 after stage 27: normal release download
    and installed-payload verification, sole-owner/startup/shortcut activation,
    preserved settings and transactional retirement of obsolete binaries/scratch.
    No tracked deferrals.

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
