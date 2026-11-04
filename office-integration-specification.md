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
- A2: Use an existing public OpenRGB ambience plugin where it satisfies the behavior,
  and reuse verified capture code where needed. Keep the last valid image during
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
2. Main-monitor ambience — ACTIVE (A1-A3).
   Stage 1's integrated device set is available. Capture/source switching, temporal
   smoothing, wallpaper refresh, layout and real end-to-end acceptance remain required.
   Next: inspect the public OpenRGB ambience plugins and the existing proven
   capture/source-selection implementation before selecting the smallest integration.
3. Final delivery — NOT STARTED (D1).
   Requires stages 1 and 2 complete. Package/publish/download/install readback and
   final reconciliation close this stage; the overall request stays active until then.

The former LG built-in LED investigation remains parked; Govee is the installed
monitor-lighting alternative. The unrelated VLC screenshots belong to another chat.
Canonical OpenRGB source: D:/Projects/OpenRGB; preserve current path bindings.
New disposable work: E:/Temp/openrgb-integration-20261104. Native build scratch,
if required, uses D:/Temp/openrgb-integration-build-20261104 for I/O; prefer hosted
compilation to avoid host load. Keep runtime state separate under D:/Tools/OpenRGB.
