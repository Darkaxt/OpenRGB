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
- I2: Verify each real device's colours and addressable regions, ordinary keyboard
  and mouse input, stable sustained output and bounded CPU/memory use. Reuse the
  Govee evidence where code/configuration and relevant runtime behavior are unchanged.
  No speculative firmware flashing or onboard-profile resets are needed by this scope.
- I3: Preserve existing SignalRGB configuration, plugins, device settings and
  recovery material. Only one active lighting writer per device. G HUB is an
  authorized fallback for mouse button/DPI functions; preserve its saved profile
  and its disabled launch-at-login state. On 2026-11-04 the user authorized recovering
  G HUB after OpenRGB's devices are wired; restore its required service on demand
  if needed rather than restoring automatic boot. Do not recreate its input functions
  merely to avoid that fallback. Verify any required coexistence rather than assume it.
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

1. Device integration — ACTIVE (I1-I3).
   Govee support and physical acceptance already verified in the baseline release.
   Remaining acceptance blockers: live support/control of Secretlab, Keychron,
   Legion and G502; preservation of input/profile behavior; integrated device set,
   sustained output/resource verification and rollback. These are internal gaps
   under investigation, not external impediments. No tracked deferrals.
   Candidate 2e6d3a8e passed native CI run 41733515534, including Govee idle-frame
   preservation and a simulated 48-zone NL72S2 null-metadata/HTTP/UDP regression.
   Native changes are diagnostic candidates, not physical acceptance. Run 41735201548
   builds 66db218b with graceful headless teardown. Next: inspect six real devices
   using E:/Temp/openrgb-integration-20261104/Inspect-NativeDevices.ps1 (single CLI
   scan with original Govee process restored in finally), then activate the verified
   shutdown-capable candidate for colour/input/sustained checks. G HUB recovery is
   authorized after lighting is wired; its saved profile remains unchanged.
   The CLI scan exposed short HIDAPI topology replies and delayed VIA echoes;
   correlated GET-only probes reproduced both. Fixed in 7947db2c; CI 41736410371
   passed, including native graceful teardown. Downloaded artifact SHA256
   8fbb329f3588cf6671150174670c5c5243a60094d1223bf41864ec106045afe6 matched
   GitHub's digest; 46 installed members read back at the task-owned candidate
   D:/Tools/OpenRGB/releases/candidate-integration-7947db2c. Next action is
   E:/Temp/openrgb-integration-20261104/Activate-Integration.ps1: verified-owner
   baseline stop, native readiness, strict six-controller inventory and colours;
   failure restores the Govee baseline. This remains intermediate testing.
2. Main-monitor ambience — NOT STARTED (A1-A3).
   Requires stage 1's integrated device set. Capture/source switching, temporal
   smoothing, wallpaper refresh, layout and real end-to-end acceptance belong here.
3. Final delivery — NOT STARTED (D1).
   Requires stages 1 and 2 complete. Package/publish/download/install readback and
   final reconciliation close this stage; the overall request stays active until then.

The former LG built-in LED investigation remains parked; Govee is the installed
monitor-lighting alternative. The unrelated VLC screenshots belong to another chat.
Canonical OpenRGB source: D:/Projects/OpenRGB; preserve current path bindings.
New disposable work: E:/Temp/openrgb-integration-20261104. Native build scratch,
if required, uses D:/Temp/openrgb-integration-build-20261104 for I/O; prefer hosted
compilation to avoid host load. Keep runtime state separate under D:/Tools/OpenRGB.
