$repoPath = "D:\InSynBio-AI-Research\Antibody_Engineer_Suite\therasik-web-clone"

Write-Host "正在进入网站目录..." -ForegroundColor Cyan
cd $repoPath

Write-Host "1. 拉取最新版本 (Git Pull)..." -ForegroundColor Cyan
git pull origin main

Write-Host "2. 添加修改 (Git Add)..." -ForegroundColor Cyan
git add .

Write-Host "3. 提交修改 (Git Commit)..." -ForegroundColor Cyan
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
git commit -m "Website Update: $timestamp"

Write-Host "4. 推送到 GitHub (Git Push)..." -ForegroundColor Cyan
git push origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host "`n✅ 成功！网页正在后台自动更新，请等待 1-2 分钟后访问 www.therasik.com" -ForegroundColor Green
} else {
    Write-Host "`n❌ 出错，请检查网络或 Git 配置。" -ForegroundColor Red
}

Write-Host "`n按任意键退出..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
