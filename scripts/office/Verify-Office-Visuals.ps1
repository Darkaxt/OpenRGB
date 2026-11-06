param(
    [Parameter(Mandatory)][string]$InstallRoot,
    [Parameter(Mandatory)][string]$OutputDirectory,
    [string]$StateRoot='D:/Tools/OpenRGB/state-integration'
)
$ErrorActionPreference='Stop'
if (Get-Process -Name OpenRGB -ErrorAction SilentlyContinue) { throw 'Stop the current owner through Stop-Office before rendering; no second RGB writer.' }
$results=@()
foreach ($scale in @('1','1.5','2')) {
    $directory=Join-Path $OutputDirectory ('scale-'+$scale)
    $null = & (Join-Path $PSScriptRoot 'Export-Office-Control.ps1') -InstallRoot $InstallRoot -OutputDirectory $directory -StateRoot $StateRoot -ExerciseEditor -ScaleFactor $scale
    $record=Get-Content -LiteralPath (Join-Path $directory 'panel-export.json') -Raw | ConvertFrom-Json
    if ($record.screen_cycle_views.Count -ne 5 -or $record.screen_views.Count -ne 4 -or $record.caption_controls.Count -ne 3) { throw 'Visual export omitted a required cycle state, Screen tab or caption control.' }
    foreach ($button in $record.caption_controls) {
        if ($button.width -ne 46 -or $button.height -ne 48 -or $button.y -ne 0 -or ($button.x+$button.width) -gt 1440) { throw 'Integrated caption control geometry escaped the 48-DIP header.' }
        $expected=if ($button.name -eq 'windowMaximize') { 9 } else { 1 }
        if ($button.hit -ne $expected) { throw 'Caption hit target does not preserve Windows snap/client interaction.' }
    }
    $results+=@{scale=$scale;views=$record.views.Count;screen_tabs=$record.screen_views.Count;cycle_states=$record.screen_cycle_views.Count;editor_restored=$record.editor_save_roundtrip;actual_preview=$record.actual_preview;caption_controls=$record.caption_controls}
}
$results | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath (Join-Path $OutputDirectory 'visual-verification.json')
$results | ConvertTo-Json -Depth 5
