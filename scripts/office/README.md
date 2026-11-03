# OpenRGB office Govee trial

This package controls H6609 (20 zones) and H8048 (two 10-zone bars) using Govee
LAN control. It does not capture wallpaper or install an ambience plugin. No
desktop UI, elevated driver, startup task or account is required.

Use Windows PowerShell 7 and Python 3.11 or later. Install the pinned SDK client
from `requirements.txt` into a dedicated Python environment.

## Prepare and start

1. Exit SignalRGB so it cannot compete for the Govee devices. Its settings,
   custom plugins and accepted layouts are preserved.
2. Prepare a **new** state directory using the shipped detector inventory:

   ```powershell
   python govee_trial.py prepare --detectors detectors.json --config D:/Tools/OpenRGB/state --strip-ip STRIP_IP --bars-ip BARS_IP
   ```

   Replace the two IP placeholders with your device addresses. The configuration
   enables only the Govee detector. Keep private addresses and logs out of Git.
3. The installation process creates `installed-manifest.json`, containing the
   executable SHA256 from the verified package. Start with:

   ```powershell
   pwsh -NoProfile -File Start-Office.ps1 -InstallRoot D:/Tools/OpenRGB/releases/1.1-office.0.1.0 -StateRoot D:/Tools/OpenRGB/state
   ```

   The server binds `127.0.0.1:6742`. Native logs and `owner.json` are in the state
   directory. No boot configuration is changed. A reported PID is launch
   evidence; `inventory` establishes SDK readiness and the expected device set.

## Check the lights

```powershell
python govee_trial.py inventory
python govee_trial.py solid
python govee_trial.py pattern
python govee_trial.py stream --frames 1800 --fps 15
```

`solid` sets the monitor strip red and both bars blue. `pattern` assigns the strip
3 red, 7 green, 4 blue and 6 yellow zones; the bars get 10 red and 10 blue zones.
These follow the accepted approximate perimeter split. Physical orientation
needs visual confirmation. `stream` sends two minutes at 15 frames/second.
Logs distinguish SDK completion and UDP writes from hardware acknowledgement,
which the Govee streaming protocol does not provide.

## Stop and return to SignalRGB

```powershell
pwsh -NoProfile -File Stop-Office.ps1 -StateRoot D:/Tools/OpenRGB/state
```

The stop command checks the recorded process ID, executable and start time,
stops only that trial process, waits for exit, then releases streaming on the two
configured addresses. Reopen SignalRGB normally to restore its lighting output.
Do not run both writers simultaneously. The original SignalRGB Govee addon and
its settings are preserved. The installed addon is currently the stock version;
the separately retained SignalRGB stream-refresh fix has not been reinstalled by
this trial.

## Verification scope

`check_wire.py` runs the actual built executable against simulated LAN peers and
verifies SDK enumeration, twenty distinct RGB values, the B0 checksum and idle
frame retention without another B1 enable. This does not replace real-device
discovery, visual colour confirmation or a sustained real stream test.
