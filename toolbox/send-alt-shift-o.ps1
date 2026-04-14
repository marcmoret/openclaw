Start-Sleep -Milliseconds 300
$wshell = New-Object -ComObject WScript.Shell
$null = $wshell.SendKeys('%+o')
Write-Output 'sent Alt+Shift+O via WScript.Shell.SendKeys'
