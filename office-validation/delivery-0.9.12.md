# Office Ambilight 1.1-office.0.9.12 delivery

Normal release: https://github.com/Darkaxt/OpenRGB/releases/tag/v1.1-office.0.9.12

Release source/tag 473d91e2af521c1d6b12aeea82540e5ebb333a14 (native code 11c227f,
Windows CI run 42951578725 success). Ambient 34fe4fa, Windows CI run 42952624525
success, including the new native-child caption hit-test. Published as a normal
non-draft/non-prerelease. An independent download matches both the checksum
sidecar and the GitHub asset digest:

`eb3aa0ed4c5f1f368faf774dbd437fe5b64bfc296b7a8e857f201d183baa28e2`

The package is kept at
`D:/Tools/OpenRGB/packages/OpenRGB-1.1-office.0.9.12-windows-x64.zip` (163 members;
check_package passed). It is installed at `D:/Tools/OpenRGB/releases/1.1-office.0.9.12`.

## Stable executable path

Activate-Release.ps1 copied the release into `D:/Tools/OpenRGB/app`. All 163
members were verified. `automation/startup.json` install_root and the desktop
control shortcut now point at the stable root, and both read back correctly.
Firewall/GlassWire rules that are keyed on `D:/Tools/OpenRGB/app/OpenRGB.exe`
will survive future releases. GlassWire may ask once for this new path.
Versioned releases (0.9.11, 0.9.12) are kept for rollback through Activate-Release.

## Activation

There was one graceful stop of the 0.9.11 owner (PID 13548; stream disable sent).

The first task activation failed with result 1 and no owner started. The cause
was the machine-local network wait added to `automation/Start-AtLogon.ps1`: it
parsed OpenRGB.json without `-AsHashtable`, and that file holds keys that differ
only in case. After this was corrected, the existing task returned 0 with state
ready. The result is a single owner, PID 44360, at `D:/Tools/OpenRGB/app/OpenRGB.exe`,
in interactive session 1. The journal owner_start entry records build 34fe4fa.

## Runtime checks (read-only)

- Plugin DLL hash matches installed-plugin.json.
- The application settings hash is unchanged:
  `1b60516c717aefc590bffdbdc33187b74a99891f87416983aeb488ba6eb178f8`.
- 6/6 devices online, capture active on DISPLAY2, output about 15 fps, no controller error.
- CPU (10 s sample): the output thread (3496) used 3.3% of a core and the whole
  process 9.8%. The 0.9.11 output-thread sample was about 52%.

## Remaining uncertainty

Stream re-entry after a failed send, together with the re-assert on rest exit
and on Recover, addresses the Govee session loss. It has not been proven that
sends actually fail during GlassWire/firewall interruptions. Natural use will
confirm it. Recover / resume lighting is the manual path. Why the main window's
central widget became a native child is unknown; the caption filter handles it
either way.

No lighting experiment, user desktop capture or Wallpaper Engine restart occurred.
