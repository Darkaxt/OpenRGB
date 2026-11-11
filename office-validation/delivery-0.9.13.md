# Office Ambilight 1.1-office.0.9.13 delivery

Normal release: https://github.com/Darkaxt/OpenRGB/releases/tag/v1.1-office.0.9.13

## Feature

Per-light night levels (spec stage 57). The Screen page is now Day/Night, with a
new Lights tab. Each light either follows the screen (the default) or fades to its
own night level, using the screen's cycle position and smoothing. The setting is
stored as `device_night_level`.

## Sources and CI

Release source/tag a2976a43f5112cab1cf8d865c5c21d63211682c0. Native code is unchanged
at 11c227f (CI 42951578725). Ambient 5ce052f76ecf2858de09bcf6edd8e09e8641e14c, Windows
CI 43024946602, succeeded.

The first Ambient run (43024110582 for 2bf87bc) failed one new owner assertion. That
lifecycle fixture disables display following, so the fallback expectation was wrong
for it. 5ce052f enables following around that check; the product code is unchanged.

The CI tests cover:
- the night position along the cycle;
- the gain at weights 0, 0.5 and 1;
- the fallback to display brightness;
- unchanged followers;
- validation, persistence and restart survival;
- clearing a level by setting it to null;
- the Lights tab (5 tabs, row load, follow toggle and slider dispatch).

## Package

Package SHA256, which matches both the independent download and the GitHub digest:

`2dc7a8a7389f9c7b1747473b6b8e0c51fc52201602e05a09fedcdbed1d80edb7`

check_package passed with 164 members and native source unchanged. The package is
retained in `D:/Tools/OpenRGB/packages`.

## Installation

Installed at `D:/Tools/OpenRGB/releases/1.1-office.0.9.13` (164 members verified).

There was one graceful stop of 0.9.12 (PID 44360, stream disable sent). Activate-Release
put the new release in the stable path `D:/Tools/OpenRGB/app`. The prior copy is kept as
`app.previous`, and active-release.json reads 0.9.13. The existing task returned result 0
with state ready.

## Post-deploy checks

- One owner, PID 46232, runs from `D:/Tools/OpenRGB/app/OpenRGB.exe` in session 1.
- owner_start reports build 5ce052f.
- The plugin hash matches its manifest.
- The settings hash is unchanged (1b60516c…f8). `device_night_level` is empty, so all
  lights still follow the screen.
- 6/6 devices online, capture active, about 15 fps, no errors.

Deployment was during the day, with night position 0. The screen cycle was auto-paused
for a fullscreen application. Screen pauses return lights with their own level to full
brightness, the same as the existing follow-screen behaviour.

No lighting experiment or Wallpaper Engine restart occurred. The user sets the Govee
levels in the Lights tab.
