param(
    [Parameter(Mandatory)][string]$InstallRoot,
    [Parameter(Mandatory)][string]$OutputDirectory,
    [string]$StateRoot = 'D:/Tools/OpenRGB/state-integration',
    [switch]$ExerciseEditor,
    [switch]$AllowUnavailable,
    [ValidateSet('1','1.5','2')][string]$ScaleFactor = '1'
)
$ErrorActionPreference = 'Stop'
if (Get-Process -Name OpenRGB -ErrorAction SilentlyContinue) { throw 'Stop the current owner before exporting the integrated application; never start two RGB writers.' }
if (Test-Path -LiteralPath $OutputDirectory) { throw 'Use a new exact export directory.' }
$null = & (Join-Path $PSScriptRoot 'Start-Office.ps1') -InstallRoot $InstallRoot -StateRoot $StateRoot -AllDevices -Ambience -ExportDirectory $OutputDirectory -ScaleFactor $ScaleFactor -ExerciseEditor:$ExerciseEditor -AllowUnavailable:$AllowUnavailable
$owner = Get-Content -LiteralPath (Join-Path $StateRoot 'owner.json') -Raw | ConvertFrom-Json
$process = Get-Process -Id $owner.pid -ErrorAction SilentlyContinue
if ($process) { $process.WaitForExit(); if ($process.ExitCode) { throw "Integrated application export failed: $($process.ExitCode)" } }
$record = Get-Content -LiteralPath (Join-Path $OutputDirectory 'panel-export.json') -Raw | ConvertFrom-Json
if ($record.devices -ne 6 -or $record.views.Count -ne 21) { throw 'Panel export did not cover all required views, including Help.' }
if (!$AllowUnavailable -and !$record.actual_preview) { throw 'No actual main display preview was rendered.' }
if ($ExerciseEditor -and !$record.editor_save_roundtrip) { throw 'The real editor save/restore did not pass.' }
$record | ConvertTo-Json -Depth 5
