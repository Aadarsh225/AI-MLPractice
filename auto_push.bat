@echo off
echo ================================
echo   Auto Pushing to GitHub
echo ================================
git add .
git commit -m "Daily learning update"
git push
echo ================================
echo   Push completed
echo ================================
pause
