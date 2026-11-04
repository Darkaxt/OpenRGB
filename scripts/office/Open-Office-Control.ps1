param(
    [string]$InstallRoot = (Split-Path $PSScriptRoot),
    [string]$StateRoot = 'D:/Tools/OpenRGB/state-integration'
)
$ErrorActionPreference = 'Stop'
$exe = (Resolve-Path (Join-Path $InstallRoot 'OfficeControl.exe')).Path
$manifest = Get-Content -LiteralPath (Join-Path $InstallRoot 'plugins/installed-plugin.json') -Raw | ConvertFrom-Json
if ((Get-FileHash -LiteralPath $exe -Algorithm SHA256).Hash -ne $manifest.panelSha256) { throw 'Installed control panel changed.' }
if ((Get-FileHash -LiteralPath (Join-Path $InstallRoot 'Qt6Network.dll') -Algorithm SHA256).Hash -ne $manifest.networkSha256) { throw 'Installed panel network library changed.' }
$runtimeTemp = Join-Path $StateRoot 'runtime-temp'
New-Item -ItemType Directory -Path $runtimeTemp -Force | Out-Null
$start = [Diagnostics.ProcessStartInfo]::new($exe)
$start.UseShellExecute = $false
$start.WorkingDirectory = $StateRoot
$start.ArgumentList.Add('--state')
$start.ArgumentList.Add($StateRoot)
$start.Environment['TEMP'] = $runtimeTemp
$start.Environment['TMP'] = $runtimeTemp
# This is the explicitly requested interactive product window, not desktop input.
$process = [Diagnostics.Process]::Start($start)
@{pid=$process.Id;executable=$exe;lightingWriter=$false} | ConvertTo-Json
