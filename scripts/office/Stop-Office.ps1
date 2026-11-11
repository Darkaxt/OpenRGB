param([Parameter(Mandatory)][string]$StateRoot,[string]$Python = 'D:/Tools/OpenRGB/python/Scripts/python.exe')
$ErrorActionPreference = 'Stop'
$owner = Get-Content -LiteralPath (Join-Path $StateRoot 'owner.json') -Raw | ConvertFrom-Json
if (Get-Process -Name SignalRgb -ErrorAction SilentlyContinue) { throw 'SignalRGB is running; do not release another writer.' }
$other = @(Get-Process -Name OpenRGB -ErrorAction SilentlyContinue | Where-Object Id -NE $owner.pid)
if ($other.Count) { throw 'Another OpenRGB instance is running; preserve it.' }
$process = Get-Process -Id $owner.pid -ErrorAction SilentlyContinue
if ($process) {
    if ($process.Path -ne $owner.executable -or $process.StartTime.ToUniversalTime().Ticks -ne $owner.startUtcTicks) { throw 'Process identity no longer matches this trial.' }
    if ($owner.graceful) {
        & $Python -B (Join-Path $PSScriptRoot 'runtime_control.py') --pid $process.Id --wait-exit --state $StateRoot
        if ($LASTEXITCODE) { throw 'Graceful stop request failed; process preserved.' }
    } else {
        Stop-Process -Id $process.Id
    }
    $process.WaitForExit()
}
$config = Get-Content -LiteralPath (Join-Path $StateRoot 'OpenRGB.json') -Raw | ConvertFrom-Json -AsHashtable
$udp = [Net.Sockets.UdpClient]::new()
try {
    $packet = [Text.Encoding]::UTF8.GetBytes('{"msg":{"cmd":"razer","data":{"pt":"uwABsQAL"}}}')
    foreach ($device in $config.GoveeDevices.devices) { $null = $udp.Send($packet, $packet.Length, $device.ip, 4003) }
} finally { $udp.Dispose() }
@{stopped=$owner.pid;stream_disable_sent=$true;hardware_acknowledged=$false} | ConvertTo-Json
