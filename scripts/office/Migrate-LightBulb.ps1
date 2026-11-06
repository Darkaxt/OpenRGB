param(
    [Parameter(Mandatory)][ValidateSet('Capture','Retire','RestoreStartup')][string]$Mode,
    [string]$StateRoot='D:/Tools/OpenRGB/state-integration',
    [string]$InstallRoot='D:/Tools/OpenRGB/releases/1.1-office.0.9.0'
)
$ErrorActionPreference='Stop'
$runKey='HKCU:\Software\Microsoft\Windows\CurrentVersion\Run'
$sourceSettings=Join-Path $env:APPDATA 'LightBulb/Settings.json'
$recordPath=Join-Path $StateRoot 'office-screen-migration.json'
$existing=(Get-ItemProperty -LiteralPath $runKey -Name LightBulb -ErrorAction SilentlyContinue).LightBulb
if($Mode -eq 'Capture') {
    if(Test-Path -LiteralPath $recordPath){throw 'Preserve the existing screen migration/rollback record.'}
    $settingsHash=(Get-FileHash -LiteralPath $sourceSettings -Algorithm SHA256).Hash
    $record=@{schema='office.screen-migration.v1';captured_at=[DateTimeOffset]::UtcNow.ToString('o');source_settings=$sourceSettings;source_settings_sha256=$settingsHash;original_startup=$existing;rollback='Stop the integrated Office owner gracefully (restores original gamma), run this script with RestoreStartup, then launch the preserved standalone LightBulb executable; Office 0.8.0 package remains retained.'}
    $record | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath $recordPath -Encoding utf8
    Get-Content -LiteralPath $recordPath -Raw
    exit
}
$record=Get-Content -LiteralPath $recordPath -Raw | ConvertFrom-Json
if($record.schema -ne 'office.screen-migration.v1'){throw 'Unknown migration record.'}
if($Mode -eq 'Retire') {
    if(Get-Process -Name LightBulb -ErrorAction SilentlyContinue){throw 'Standalone LightBulb is still running; exit it gracefully through its own tray first.'}
    $owner=Get-Content -LiteralPath (Join-Path $StateRoot 'owner.json') -Raw | ConvertFrom-Json
    $process=Get-Process -Id $owner.pid -ErrorAction Stop
    if($process.Path -ne (Join-Path $InstallRoot 'OpenRGB.exe')){throw 'Verified final Office release is not the active owner.'}
    $manifest=Get-Content -LiteralPath (Join-Path $InstallRoot 'installed-manifest.json') -Raw | ConvertFrom-Json
    if($manifest.version -ne '1.1-office.0.9.0'){throw 'Expected the completed 0.9.0 release.'}
    $status=Get-Content -LiteralPath (Join-Path $StateRoot 'office-ambience-status.json') -Raw | ConvertFrom-Json
    if(!$status.screen.managed -or !$status.screen.gamma_valid){throw 'Integrated gamma ownership/readback has not passed.'}
    if($existing -ne $record.original_startup){throw 'Standalone LightBulb startup binding changed after capture; preserve it.'}
    if((Get-FileHash -LiteralPath $sourceSettings -Algorithm SHA256).Hash -ne $record.source_settings_sha256){throw 'Original LightBulb settings changed after migration capture.'}
    if($null -ne $existing){Remove-ItemProperty -LiteralPath $runKey -Name LightBulb}
    if((Get-ItemProperty -LiteralPath $runKey -Name LightBulb -ErrorAction SilentlyContinue).LightBulb){throw 'Standalone startup retirement did not read back.'}
    @{standalone_startup_retired=$true;standalone_process_absent=$true;source_settings_preserved=$true;source_application_retained=$true;owner=$owner.pid;rollback_record=$recordPath} | ConvertTo-Json
} else {
    if(Get-Process -Name OpenRGB -ErrorAction SilentlyContinue){throw 'Stop the integrated owner gracefully before restoring standalone ownership.'}
    if($existing -and $existing -ne $record.original_startup){throw 'Preserve the changed startup binding.'}
    if($record.original_startup){Set-ItemProperty -LiteralPath $runKey -Name LightBulb -Value $record.original_startup}
    $saved=(Get-ItemProperty -LiteralPath $runKey -Name LightBulb -ErrorAction SilentlyContinue).LightBulb
    if($saved -ne $record.original_startup){throw 'Startup restoration readback differs.'}
    @{startup_restored=$true;application_started=$false;rollback_record=$recordPath}|ConvertTo-Json
}
