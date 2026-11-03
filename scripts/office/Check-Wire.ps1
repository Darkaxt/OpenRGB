param([Parameter(Mandatory)][string]$Executable, [Parameter(Mandatory)][string]$Work)
$ErrorActionPreference = 'Stop'
python -m pip install --disable-pip-version-check -r (Join-Path $PSScriptRoot 'requirements.txt')
if ($LASTEXITCODE) { throw 'SDK client installation failed.' }
python (Join-Path $PSScriptRoot 'check_wire.py') --exe $Executable --source (Join-Path $PSScriptRoot '../..') --work $Work
if ($LASTEXITCODE) { throw 'SDK/UDP verification failed.' }
