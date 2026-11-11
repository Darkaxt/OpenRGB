param(
    [Parameter(Mandatory)][string]$InstallRoot,
    [Parameter(Mandatory)][string]$StateRoot,
    [string]$Python = 'D:/Tools/OpenRGB/python/Scripts/python.exe'
)
$ErrorActionPreference = 'Stop'
# The existing scripts verify exact owner identity, hashes and exclusive writer
# state. Wait for native exit/readiness rather than sleeping or launching twice.
& (Join-Path $PSScriptRoot 'Stop-Office.ps1') -StateRoot $StateRoot -Python $Python
if ($LASTEXITCODE) { throw 'The previous lighting owner did not stop.' }
& (Join-Path $PSScriptRoot 'Start-Office.ps1') -InstallRoot $InstallRoot -StateRoot $StateRoot -AllDevices -Ambience
if ($LASTEXITCODE) { throw 'The replacement owner did not start.' }
$owner = Get-Content -LiteralPath (Join-Path $StateRoot 'owner.json') -Raw | ConvertFrom-Json
& $Python -B (Join-Path $PSScriptRoot 'runtime_control.py') --pid $owner.pid --wait-ready --state $StateRoot
if ($LASTEXITCODE) { throw 'The replacement owner exited before native readiness.' }
& $Python -B (Join-Path $PSScriptRoot 'office_control.py') --state $StateRoot --wait-ready $owner.pid
if ($LASTEXITCODE) { throw 'The replacement control endpoint was not published.' }
