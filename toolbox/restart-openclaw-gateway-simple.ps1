$ErrorActionPreference = 'Continue'

$gatewayRoot = 'C:\Users\marco\.openclaw'
$gatewayCmd = Join-Path $gatewayRoot 'gateway.cmd'
$workspaceRoot = 'C:\Users\marco\.openclaw\workspace'
$taskFile = Join-Path $workspaceRoot 'TASKS.md'
$wtExe = (Get-Command 'wt.exe' -ErrorAction SilentlyContinue).Source
if (-not $wtExe) {
    $wtExe = (Get-Command 'wt' -ErrorAction SilentlyContinue).Source
}

Write-Host '[restart-openclaw-gateway-simple] Force-stopping node.exe and chrome.exe...'
Start-Process -FilePath 'taskkill.exe' -ArgumentList '/IM','node.exe','/F' -WindowStyle Hidden -Wait -NoNewWindow -ErrorAction SilentlyContinue
Start-Process -FilePath 'taskkill.exe' -ArgumentList '/IM','chrome.exe','/F' -WindowStyle Hidden -Wait -NoNewWindow -ErrorAction SilentlyContinue

Write-Host '[restart-openclaw-gateway-simple] Force-closing stale cmd.exe / Windows Terminal windows that launched OpenClaw...'
Get-CimInstance Win32_Process -ErrorAction SilentlyContinue |
    Where-Object {
        ($_.Name -eq 'cmd.exe' -and $_.CommandLine -and $_.CommandLine -match [regex]::Escape($gatewayCmd)) -or
        ($_.Name -match 'WindowsTerminal|wt.exe' -and $_.CommandLine -and ($_.CommandLine -match 'openclaw gateway run' -or $_.CommandLine -match [regex]::Escape($gatewayCmd)))
    } |
    ForEach-Object {
        try {
            Start-Process -FilePath 'taskkill.exe' -ArgumentList '/PID', $_.ProcessId, '/T', '/F' -WindowStyle Hidden -Wait -NoNewWindow -ErrorAction SilentlyContinue
        } catch {}
    }

Write-Host '[restart-openclaw-gateway-simple] Waiting 10 seconds...'
Start-Sleep -Seconds 10

if ($wtExe) {
    Write-Host "[restart-openclaw-gateway-simple] Launching OpenClaw in Windows Terminal via openclaw gateway run"
    $title = 'OpenClaw Gateway'
    $startupNote = "After reconnect: 1) read TASKS.md first ($taskFile) 2) automatically continue the active browser task and report back."
    Start-Process -FilePath $wtExe -ArgumentList @(
        'new-tab',
        '--title', $title,
        '--startingDirectory', $gatewayRoot,
        'powershell.exe',
        '-NoExit',
        '-Command',
        "Write-Host '$startupNote'; openclaw gateway run"
    ) -WorkingDirectory $gatewayRoot
} else {
    Write-Host "[restart-openclaw-gateway-simple] Windows Terminal not found, launching fallback $gatewayCmd"
    Start-Process -FilePath $gatewayCmd -WorkingDirectory $gatewayRoot
}
