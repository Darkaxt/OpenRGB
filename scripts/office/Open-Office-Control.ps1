param(
    [string]$InstallRoot = (Split-Path $PSScriptRoot),
    [string]$StateRoot = 'D:/Tools/OpenRGB/state-integration'
)
$ErrorActionPreference = 'Stop'
$launchMutex = [Threading.Mutex]::new($false, 'Local\OpenRGB.Office.OwnerLaunch')
$launchOwned = $false
try {
try { $launchOwned = $launchMutex.WaitOne() } catch [Threading.AbandonedMutexException] { $launchOwned = $true }
$exe = (Resolve-Path (Join-Path $InstallRoot 'OpenRGB.exe')).Path
$manifest = Get-Content -LiteralPath (Join-Path $InstallRoot 'installed-manifest.json') -Raw | ConvertFrom-Json
if ((Get-FileHash -LiteralPath $exe -Algorithm SHA256).Hash -ne $manifest.executableSha256) { throw 'Installed application changed.' }
if (!(Get-Process -Name OpenRGB -ErrorAction SilentlyContinue)) {
    $null = & (Join-Path $PSScriptRoot 'Start-Office.ps1') -InstallRoot $InstallRoot -StateRoot $StateRoot -AllDevices -Ambience
}
$owner = Get-Content -LiteralPath (Join-Path $StateRoot 'owner.json') -Raw | ConvertFrom-Json
$process = Get-Process -Id $owner.pid -ErrorAction Stop
if ($process.Path -ne $exe) { throw 'Another OpenRGB installation owns lighting; stop it before changing installations.' }
python -B (Join-Path $PSScriptRoot 'runtime_control.py') --pid $owner.pid --show --state $StateRoot
if ($LASTEXITCODE) { throw 'Could not activate the existing Office application.' }
} finally {
    if ($launchOwned) { $launchMutex.ReleaseMutex() }
    $launchMutex.Dispose()
}
