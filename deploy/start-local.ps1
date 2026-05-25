# 本地 Windows 一键启动（无 Docker 时使用）
# 用法: powershell -ExecutionPolicy Bypass -File deploy/start-local.ps1

$Root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $Root

if (-not (Test-Path ".env")) {
    Copy-Item ".env.example" ".env"
    $secret = -join ((48..57) + (97..102) | Get-Random -Count 64 | ForEach-Object { [char]$_ })
    (Get-Content ".env") -replace "change-me-to-a-random-string", $secret | Set-Content ".env"
    Write-Host "已创建 .env"
}

pip install -r requirements.txt -q
$env:FLASK_DEBUG = "0"
Start-Process python -ArgumentList "run.py" -WorkingDirectory $Root -WindowStyle Hidden
Start-Sleep -Seconds 2

Write-Host ""
Write-Host "考试系统已启动:"
Write-Host "  http://127.0.0.1:5000/"
Write-Host "  http://localhost:5000/"
Write-Host "  教师后台: http://127.0.0.1:5000/teacher"
