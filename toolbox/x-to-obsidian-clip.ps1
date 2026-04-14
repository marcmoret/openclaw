param(
    [Parameter(Mandatory = $true)]
    [string]$Url,
    [string]$Profile = 'openclaw',
    [int]$WaitAfterOpenMs = 2000,
    [int]$WaitAfterFocusMs = 500
)

$ErrorActionPreference = 'Stop'

$configPath = 'C:\Users\marco\.openclaw\openclaw.json'
$config = Get-Content $configPath -Raw | ConvertFrom-Json
$token = $config.gateway.auth.token
$headers = @{ Authorization = "Bearer $token"; 'Content-Type' = 'application/json' }
$base = 'http://127.0.0.1:18791/'

function Invoke-BrowserJson {
    param(
        [string]$Path,
        [string]$Method = 'GET',
        [object]$Body = $null
    )
    $params = @{
        Uri = $base + $Path
        Method = $Method
        Headers = $headers
    }
    if ($null -ne $Body) {
        $params.Body = ($Body | ConvertTo-Json -Compress)
    }
    Invoke-RestMethod @params
}

Write-Host "[x-to-obsidian-clip] opening $Url"
$opened = Invoke-BrowserJson -Path "tabs/open?profile=$Profile" -Method 'POST' -Body @{ url = $Url }
Start-Sleep -Milliseconds $WaitAfterOpenMs

$targetId = $opened.targetId
if (-not $targetId) {
    throw 'No targetId returned from browser open.'
}

Write-Host "[x-to-obsidian-clip] focusing $targetId"
openclaw browser --browser-profile $Profile focus $targetId | Out-Host
Start-Sleep -Milliseconds $WaitAfterFocusMs

Write-Host '[x-to-obsidian-clip] sending Alt+Shift+O via OS-level SendKeys'
powershell -ExecutionPolicy Bypass -File 'C:\Users\marco\.openclaw\workspace\toolbox\send-alt-shift-o.ps1' | Out-Host

Write-Host '[x-to-obsidian-clip] done'
