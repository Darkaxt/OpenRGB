# Delivery 1.1-office.0.9.18 (0.9.17 withdrawn)

Disconnected devices are shown in gray (spec stage 60).

## 0.9.17: failed and withdrawn

- Ambient 43f1534 (CI 43651869634). Package `1cdf5de0736d1bb70ed86d054e117f0902d96776a0563143a8104d742f9910f5`.
- Deployed; owner 25512 reported ready, then stopped gracefully about 16 s after start.
- Native log: "Ambience plugin failed: [json.exception.type_error.306] cannot use value() with null".
- Cause: Json::value() was called on the panel's null state before the first snapshot.
- The first delivery record for 0.9.17 claimed success before the process check, and was replaced by this file.
- Rolled back to 0.9.16 (owner 59204). The release is marked prerelease with a "Withdrawn" notice.

## 0.9.18

- Native unchanged at 11c227f (CI 42951578725); tag v1.1-office.0.9.18 → fb5d15f25eb5ac78c29980c3191ec5d5f3a4328f.
- Ambient 66146d480a73ad59e7655bfe0869b44a4e4ddfcf, CI 43652943620 green.
- https://github.com/Darkaxt/OpenRGB/releases/tag/v1.1-office.0.9.18
- SHA-256 `7df0488879ae337bc4fa1de9452980747b0d38cc41349c50c7f71ab2aac67057`
- check_package passed with 168 members. The release asset was downloaded independently and its hash matched.

## Checks

- Installed and activated at the stable path. The task returned 0 and state ready.
- Owner PID 47708 was still running after 90 s, with no plugin failure in the native log.
- The plugin hash matches its manifest.
- The saved seven-device topology loaded.
- Online devices: Logitech, Legion and Corsair.
- Screen valid, with no error.

Not verified: the rendered gray text (no desktop capture).

No lighting experiment or Wallpaper Engine restart occurred.
