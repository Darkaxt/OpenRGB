param(
    [string]$InstallRoot = (Split-Path $PSScriptRoot),
    [string]$StateRoot = 'D:/Tools/OpenRGB/state-integration'
)
$ErrorActionPreference = 'Stop'
$exe = (Resolve-Path (Join-Path $InstallRoot 'OfficeControl.exe')).Path
$manifest = Get-Content -LiteralPath (Join-Path $InstallRoot 'plugins/installed-plugin.json') -Raw | ConvertFrom-Json
if ((Get-FileHash -LiteralPath $exe -Algorithm SHA256).Hash -ne $manifest.panelSha256) { throw 'Installed control panel changed.' }
if ((Get-FileHash -LiteralPath (Join-Path $InstallRoot 'Qt6Network.dll') -Algorithm SHA256).Hash -ne $manifest.networkSha256) { throw 'Installed panel network library changed.' }
$startOwner = $true
$preferences = Join-Path $StateRoot 'office-panel.json'
if (Test-Path -LiteralPath $preferences) {
    $panelOptions = Get-Content -LiteralPath $preferences -Raw | ConvertFrom-Json
    if ($null -ne $panelOptions.start_owner) { $startOwner = [bool]$panelOptions.start_owner }
}
if ($startOwner -and !(Get-Process -Name OpenRGB -ErrorAction SilentlyContinue)) {
    $null = & (Join-Path $PSScriptRoot 'Start-Office.ps1') -InstallRoot $InstallRoot -StateRoot $StateRoot -AllDevices -Ambience
    $owner = Get-Content -LiteralPath (Join-Path $StateRoot 'owner.json') -Raw | ConvertFrom-Json
    python -B (Join-Path $PSScriptRoot 'runtime_control.py') --pid $owner.pid --wait-ready --state $StateRoot
    if ($LASTEXITCODE) { throw 'The lighting owner exited before readiness.' }
    python -B (Join-Path $PSScriptRoot 'office_control.py') --state $StateRoot --wait-ready $owner.pid
    if ($LASTEXITCODE) { throw 'The lighting control endpoint was not published.' }
}
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
