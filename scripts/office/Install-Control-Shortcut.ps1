param(
    [Parameter(Mandatory)][string]$InstallRoot,
    [string]$StateRoot = 'D:/Tools/OpenRGB/state-integration'
)
$ErrorActionPreference = 'Stop'
$launcher = (Resolve-Path (Join-Path $InstallRoot 'office/Open-Office-Control.ps1')).Path
$powershell = (Get-Command pwsh -ErrorAction Stop).Source
$path = Join-Path ([Environment]::GetFolderPath('Desktop')) 'Office Ambilight.lnk'
$shell = New-Object -ComObject WScript.Shell
if (Test-Path -LiteralPath $path) {
    $existing = $shell.CreateShortcut($path)
    if ($existing.Description -ne 'Native OpenRGB Office Ambilight control panel') { throw 'Preserve the unrelated shortcut at this name.' }
}
$shortcut = $shell.CreateShortcut($path)
$shortcut.TargetPath = $powershell
$shortcut.Arguments = '-NoProfile -WindowStyle Hidden -File "' + $launcher + '" -InstallRoot "' + $InstallRoot + '" -StateRoot "' + $StateRoot + '"'
$shortcut.WorkingDirectory = $StateRoot
$shortcut.IconLocation = (Join-Path $InstallRoot 'OpenRGB.exe') + ',0'
$shortcut.Description = 'Native OpenRGB Office Ambilight control panel'
$shortcut.Save()
$saved = $shell.CreateShortcut($path)
if ($saved.TargetPath -ne $powershell -or $saved.Arguments -ne $shortcut.Arguments) { throw 'Shortcut readback differs.' }
@{shortcut=$path;launcher=$launcher;readbackVerified=$true;startupTaskInstalled=$false} | ConvertTo-Json
