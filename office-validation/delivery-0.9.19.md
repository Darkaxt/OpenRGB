# Delivery 1.1-office.0.9.19

Tray light mixer lists available devices only (spec stage 61).

## Sources

- Native unchanged at 11c227f (CI 42951578725); tag v1.1-office.0.9.19 → e764efb0c3464906b3a8566f948b700386b4dc26.
- Ambient b57f4da86079a9039b07d0a347d63d293c3dc15b, CI 43656501294 green.
- CI includes a widget test: a row is hidden while disconnected, keeps its level, returns on reconnect and hides again.

## Package

- https://github.com/Darkaxt/OpenRGB/releases/tag/v1.1-office.0.9.19
- SHA-256 `bc1618aae8bfe73b0c4f9eb9d7d8dee9e11633c1bd7066d992a1986f599c4176`
- check_package passed with 168 members.
- The release asset was downloaded independently and its hash matched.

## Checks

- Installed and activated at the stable path. The task returned 0 and state ready.
- Owner PID 23600 was still running after 90 s, with no "Ambience plugin failed" in the native log.
- The plugin hash matches its manifest.
- Screen valid, with no error.

Not verified: the rendered tray (no desktop capture).

No lighting experiment or Wallpaper Engine restart occurred.
