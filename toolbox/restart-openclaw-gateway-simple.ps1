$ErrorActionPreference = 'Continue'

$gatewayRoot = 'C:\Users\marco\.openclaw'
$runner = 'C:\Users\marco\.openclaw\workspace\toolbox\restart-openclaw-gateway-runner.ps1'

Write-Host '[restart-openclaw-gateway-simple] Opening a new PowerShell window for manual-style restart...'
Start-Process -FilePath 'powershell.exe' -ArgumentList @(
    '-NoExit',
    '-ExecutionPolicy', 'Bypass',
    '-File', $runner
) -WorkingDirectory $gatewayRoot
