@echo off
cd/d "D:\10k Coders"
git add .
git commit -m "Auto update %date% %time%"
git push origin main
pause
