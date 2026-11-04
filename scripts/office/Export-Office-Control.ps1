param(
    [Parameter(Mandatory)][string]$InstallRoot,
    [Parameter(Mandatory)][string]$OutputDirectory,
    [string]$StateRoot = 'D:/Tools/OpenRGB/state-integration',
    [switch]$ExerciseEditor
)
$ErrorActionPreference = 'Stop'
$exe = (Resolve-Path (Join-Path $InstallRoot 'OfficeControl.exe')).Path
$manifest = Get-Content -LiteralPath (Join-Path $InstallRoot 'plugins/installed-plugin.json') -Raw | ConvertFrom-Json
if ((Get-FileHash -LiteralPath $exe -Algorithm SHA256).Hash -ne $manifest.panelSha256) { throw 'Installed control panel changed.' }
if ((Get-FileHash -LiteralPath (Join-Path $InstallRoot 'platforms/qoffscreen.dll') -Algorithm SHA256).Hash -ne $manifest.offscreenSha256) { throw 'Offscreen rendering platform changed.' }
if (Test-Path -LiteralPath $OutputDirectory) { throw 'Use a new exact export directory.' }
$start = [Diagnostics.ProcessStartInfo]::new($exe)
$start.UseShellExecute = $false
$start.CreateNoWindow = $true
$start.WorkingDirectory = $StateRoot
foreach ($argument in @('--state',$StateRoot,'--export-views',$OutputDirectory)) { $start.ArgumentList.Add($argument) }
if ($ExerciseEditor) { $start.ArgumentList.Add('--exercise-editor') }
$start.Environment['QT_QPA_PLATFORM'] = 'offscreen'
$start.Environment['TEMP'] = Join-Path $StateRoot 'runtime-temp'
$start.Environment['TMP'] = Join-Path $StateRoot 'runtime-temp'
$process = [Diagnostics.Process]::Start($start)
$process.WaitForExit()
if ($process.ExitCode) { throw "Native panel export failed: $($process.ExitCode)" }
$record = Get-Content -LiteralPath (Join-Path $OutputDirectory 'panel-export.json') -Raw | ConvertFrom-Json
if ($record.devices -ne 6 -or $record.views.Count -ne 12) { throw 'Panel export did not cover all required views.' }
if ($ExerciseEditor -and !$record.editor_save_roundtrip) { throw 'The real editor save/restore did not pass.' }
$record | ConvertTo-Json -Depth 5
