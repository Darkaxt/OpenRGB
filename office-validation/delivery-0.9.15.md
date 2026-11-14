# Delivery 1.1-office.0.9.15 (supersedes 0.9.14)

HDR screen dimming and Corsair K95 RGB Platinum support (spec stage 58).

## Sources

- Native unchanged at 11c227f (CI 42951578725); release tag v1.1-office.0.9.15 →
  973e31c0af0c594549e383d037796f928d48a2c1 (office scripts enable the optional
  "Corsair K95 RGB PLATINUM" detector).
- Ambient b7f8ca1cd46d233e4633d9cb0a9e23f8c2998480, CI 43647531586 green
  (0.9.14 used f19b6f1, CI 43646258613).

## Packages

- https://github.com/Darkaxt/OpenRGB/releases/tag/v1.1-office.0.9.15
  `5c1e84541178030ae16d51b725a1254d87bbb34b8b19c6fccd8d971b076fd75d`
- https://github.com/Darkaxt/OpenRGB/releases/tag/v1.1-office.0.9.14 (superseded)
  `ddba480cbbfbb0ff98994c98660599821991ba3cfa473499774f496fe380a8b1`

check_package passed with 165 members, native source unchanged. Each release asset
was downloaded independently and its hash matched.

## Installation

- 0.9.14 installed; owner 10612 was stopped gracefully. In
  state-integration/OpenRGB.json, "Corsair K95 RGB PLATINUM" was changed from false
  to true by text replacement while the owner was stopped.
- After activation the task returned 0 and state was ready (PID 61860). The K95 was
  added (journal device_added, Corsair). The screen error was "Windows rejected the
  HDR SDR content brightness".
- Diagnosis by writing the current levels back unchanged (no visible change): the
  AW3423DWF returned 0; the built-in laptop panel returned 50 (ERROR_NOT_SUPPORTED).
- 0.9.15 leaves such panels unchanged. It was installed and activated, and the task
  returned 0 and state ready.

## Post-deploy checks

- Single owner PID 56960 at D:/Tools/OpenRGB/app/OpenRGB.exe. The plugin hash
  matches its manifest. active-release.json reads 0.9.15.
- Layout: Logitech, Keychron, Legion, H6609, H8048, Secretlab, Corsair.
- Online: Logitech, Legion and Corsair. The office devices are offline at home, as
  expected.
- Screen: gamma_valid true, no error, hdr_displays 1, hdr_fixed_displays 1. The
  screen pause is still "forever" (set before this work), so the SDR white is at
  its baseline, 340 nits.

No lighting experiment or Wallpaper Engine restart occurred. The Corsair map is in
memory until the user saves the topology.
