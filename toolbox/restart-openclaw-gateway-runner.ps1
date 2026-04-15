$ErrorActionPreference = 'Continue'

$taskFile = 'C:\Users\marco\.openclaw\workspace\TASKS.md'

Write-Host '[restart-openclaw-gateway-simple] 1/3 openclaw gateway stop'
& openclaw gateway stop

Write-Host '[restart-openclaw-gateway-simple] 2/3 waiting 10 seconds'
Start-Sleep -Seconds 10

Write-Host '[restart-openclaw-gateway-simple] 3/3 openclaw gateway run'
& openclaw gateway run

Write-Host ''
Write-Host ('After reconnect: read {0} first, then continue the active task.' -f $taskFile)
