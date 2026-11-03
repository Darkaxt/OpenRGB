param(
    [Parameter(Mandatory)][string]$InstallRoot,
    [Parameter(Mandatory)][string]$StateRoot
)
$ErrorActionPreference = 'Stop'
if (Get-Process -Name SignalRgb,OpenRGB -ErrorAction SilentlyContinue) { throw 'Exit SignalRGB/OpenRGB before starting this exclusive Govee trial.' }
$exe = (Resolve-Path (Join-Path $InstallRoot 'OpenRGB.exe')).Path
$manifest = Get-Content -LiteralPath (Join-Path $InstallRoot 'installed-manifest.json') -Raw | ConvertFrom-Json
if ((Get-FileHash -LiteralPath $exe -Algorithm SHA256).Hash -ne $manifest.executableSha256) { throw 'Installed OpenRGB executable changed.' }
$config = Get-Content -LiteralPath (Join-Path $StateRoot 'OpenRGB.json') -Raw | ConvertFrom-Json -AsHashtable
$enabled = @($config.Detectors.detectors.Keys | Where-Object { $config.Detectors.detectors[$_] })
if ($enabled.Count -ne 1 -or $enabled[0] -cne 'Govee') { throw 'Expected Govee-only detection.' }
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
$process = [Diagnostics.Process]::Start($start)
@{pid=$process.Id;startUtcTicks=$process.StartTime.ToUniversalTime().Ticks;executable=$exe} | ConvertTo-Json | Set-Content -LiteralPath (Join-Path $StateRoot 'owner.json')
[pscustomobject]@{pid=$process.Id;executable=$exe;configuration=$StateRoot;headless=$true} | ConvertTo-Json
