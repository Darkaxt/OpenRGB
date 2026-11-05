param([Parameter(Mandatory)][string]$QtRoot, [Parameter(Mandatory)][string]$BuildRoot)
$ErrorActionPreference = 'Stop'
$sourceRoot = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
$vswhere = Join-Path ${env:ProgramFiles(x86)} 'Microsoft Visual Studio/Installer/vswhere.exe'
$vs = & $vswhere -latest -products '*' -requires Microsoft.VisualStudio.Component.VC.Tools.x86.x64 -property installationPath
if (!$vs) { throw 'MSVC x64 compiler not found.' }
Import-Module (Join-Path $vs 'Common7/Tools/Microsoft.VisualStudio.DevShell.dll')
Enter-VsDevShell -VsInstallPath $vs -DevCmdArguments '-arch=x64 -host_arch=x64' -SkipAutomaticLocation
$env:PATH = (Join-Path $QtRoot 'bin') + ';' + $env:PATH
New-Item -ItemType Directory -Path $BuildRoot -Force | Out-Null
$jomZip = Join-Path $BuildRoot 'jom.zip'
$jomUrl = 'https://download.qt.io/official_releases/jom/jom_1_1_4.zip'
Invoke-WebRequest -Uri $jomUrl -OutFile $jomZip
$expected = ((Invoke-WebRequest -Uri ($jomUrl + '.sha256')).Content.Trim() -split '\s+')[0]
if ((Get-FileHash -LiteralPath $jomZip -Algorithm SHA256).Hash -ne $expected) { throw 'jom checksum mismatch.' }
Expand-Archive -LiteralPath $jomZip -DestinationPath (Join-Path $BuildRoot 'jom')
Push-Location $BuildRoot
try {
    & (Join-Path $QtRoot 'bin/qmake.exe') (Join-Path $sourceRoot 'OpenRGB.pro') CONFIG-=debug_and_release CONFIG+=release OFFICE_VERSION=office.0.8.0
    if ($LASTEXITCODE) { throw "qmake failed: $LASTEXITCODE" }
    & (Join-Path $BuildRoot 'jom/jom.exe') -j2
    if ($LASTEXITCODE) { throw "build failed: $LASTEXITCODE" }
    & (Join-Path $QtRoot 'bin/windeployqt.exe') --release --no-translations --no-opengl-sw --no-system-d3d-compiler --no-network (Join-Path $BuildRoot 'release/OpenRGB.exe')
    if ($LASTEXITCODE) { throw "windeployqt failed: $LASTEXITCODE" }
    foreach ($name in @('Qt6Core5Compat.dll','Qt6OpenGL.dll')) {
        Copy-Item -LiteralPath (Join-Path $QtRoot "bin/$name") -Destination (Join-Path $BuildRoot 'release')
    }
    Copy-Item -LiteralPath (Join-Path $sourceRoot 'LICENSE') -Destination (Join-Path $BuildRoot 'release')
    Copy-Item -LiteralPath (Join-Path $sourceRoot 'office-govee-specification.md') -Destination (Join-Path $BuildRoot 'release')
    Copy-Item -LiteralPath (Join-Path $sourceRoot 'office-integration-specification.md') -Destination (Join-Path $BuildRoot 'release')
    Copy-Item -LiteralPath $PSScriptRoot -Destination (Join-Path $BuildRoot 'release/office') -Recurse
    $commit = & git -C $sourceRoot rev-parse HEAD
    @{version='1.1-office.0.8.0';source=$commit;upstream='8f3ee202f7abe171e26372cfdc53256593d03ff3'} | ConvertTo-Json | Set-Content -LiteralPath (Join-Path $BuildRoot 'release/office-build.json')
    python (Join-Path $PSScriptRoot 'govee_trial.py') detectors --source $sourceRoot --output (Join-Path $BuildRoot 'release/office/detectors.json')
    if ($LASTEXITCODE) { throw 'Detector inventory failed.' }
} finally { Pop-Location }
