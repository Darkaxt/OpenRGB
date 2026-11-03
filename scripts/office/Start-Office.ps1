param(
    [Parameter(Mandatory)][string]$InstallRoot,
    [Parameter(Mandatory)][string]$StateRoot,
    [switch]$AllDevices
)
$ErrorActionPreference = 'Stop'
if (Get-Process -Name SignalRgb,OpenRGB -ErrorAction SilentlyContinue) { throw 'Exit SignalRGB/OpenRGB before starting this exclusive Govee trial.' }
$exe = (Resolve-Path (Join-Path $InstallRoot 'OpenRGB.exe')).Path
$manifest = Get-Content -LiteralPath (Join-Path $InstallRoot 'installed-manifest.json') -Raw | ConvertFrom-Json
if ((Get-FileHash -LiteralPath $exe -Algorithm SHA256).Hash -ne $manifest.executableSha256) { throw 'Installed OpenRGB executable changed.' }
$config = Get-Content -LiteralPath (Join-Path $StateRoot 'OpenRGB.json') -Raw | ConvertFrom-Json -AsHashtable
$enabled = @($config.Detectors.detectors.Keys | Where-Object { $config.Detectors.detectors[$_] })
if ($AllDevices) {
    $expected = @('Govee','Nanoleaf','Keychron RGB QMK/ZMK Keyboard','Lenovo Legion 7 Gen 8','Logitech HID++ 2.0')
    if (@(Compare-Object $expected $enabled -CaseSensitive).Count) { throw 'Expected the five office detectors only.' }
    if ($config.NanoleafDevices.devices.Count -ne 1 -or $config.NanoleafDevices.devices[0].zone_count -ne 48) { throw 'Expected the 48-section Secretlab strip.' }
} elseif ($enabled.Count -ne 1 -or $enabled[0] -cne 'Govee') { throw 'Expected Govee-only detection.' }
if ($config.GoveeDevices.devices.Count -ne 2) { throw 'Expected exactly two configured Govee devices.' }
$runtimeTemp = Join-Path $StateRoot 'runtime-temp'
New-Item -ItemType Directory -Path $runtimeTemp -Force | Out-Null
$start = [Diagnostics.ProcessStartInfo]::new($exe)
$start.UseShellExecute = $false
$start.CreateNoWindow = $true
$start.WorkingDirectory = $StateRoot
foreach ($arg in @('--config',$StateRoot,'--noautoconnect','--server','--server-host','127.0.0.1','--loglevel','info')) { $start.ArgumentList.Add($arg) }
$start.Environment['TEMP'] = $runtimeTemp
$start.Environment['TMP'] = $runtimeTemp
if ($AllDevices) { $start.Environment['OPENRGB_OFFICE_SHUTDOWN'] = '1' }
$process = [Diagnostics.Process]::Start($start)
@{pid=$process.Id;startUtcTicks=$process.StartTime.ToUniversalTime().Ticks;executable=$exe;graceful=[bool]$AllDevices} | ConvertTo-Json | Set-Content -LiteralPath (Join-Path $StateRoot 'owner.json')
[pscustomobject]@{pid=$process.Id;executable=$exe;configuration=$StateRoot;headless=$true} | ConvertTo-Json
