param(
    [Parameter(Mandatory)][string]$Release,
    [string]$StableRoot = 'D:/Tools/OpenRGB/app'
)
# Copies a verified release into one stable executable path. Firewall and
# network-monitor rules key applications by executable path, so every release
# runs as the same application. Versioned release folders remain for rollback.
$ErrorActionPreference = 'Stop'
$releasePath = (Resolve-Path -LiteralPath $Release).Path
$stable = [IO.Path]::GetFullPath($StableRoot)
$staging = "$stable.staging"
$previous = "$stable.previous"
$stableExe = [IO.Path]::GetFullPath((Join-Path $stable 'OpenRGB.exe'))
$running = @(Get-Process -Name OpenRGB -ErrorAction SilentlyContinue | Where-Object { $_.Path -and [IO.Path]::GetFullPath($_.Path) -eq $stableExe })
if ($running.Count) { throw 'Stop the owner running from the stable path before activating another release.' }
$manifest = Get-Content -LiteralPath (Join-Path $releasePath 'installed-manifest.json') -Raw | ConvertFrom-Json
function Test-Tree([string]$Root) {
    foreach ($entry in $manifest.files.PSObject.Properties) {
        $file = Join-Path $Root $entry.Name
        if (!(Test-Path -LiteralPath $file -PathType Leaf) -or (Get-FileHash -LiteralPath $file -Algorithm SHA256).Hash -ne $entry.Value) {
            throw "Release member differs from its installed manifest: $($entry.Name)"
        }
    }
}
Test-Tree $releasePath
if (Test-Path -LiteralPath $staging) { Remove-Item -LiteralPath $staging -Recurse -Force }
Copy-Item -LiteralPath $releasePath -Destination $staging -Recurse
Test-Tree $staging
@{release=$releasePath;version=$manifest.version;source=$manifest.source;executableSha256=$manifest.executableSha256;activatedUtc=[DateTime]::UtcNow.ToString('o')} |
    ConvertTo-Json | Set-Content -LiteralPath (Join-Path $staging 'active-release.json')
if (Test-Path -LiteralPath $stable) {
    if (Test-Path -LiteralPath $previous) { Remove-Item -LiteralPath $previous -Recurse -Force }
    Rename-Item -LiteralPath $stable -NewName (Split-Path -Leaf $previous)
}
Rename-Item -LiteralPath $staging -NewName (Split-Path -Leaf $stable)
Test-Tree $stable
[pscustomobject]@{stable=$stable;release=$releasePath;version=$manifest.version;verifiedMembers=@($manifest.files.PSObject.Properties).Count} | ConvertTo-Json
