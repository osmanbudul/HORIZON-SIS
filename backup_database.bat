@echo off
cd /d "%~dp0"
if not exist backups mkdir backups
for /f %%i in ('powershell -NoProfile -Command "Get-Date -Format yyyyMMdd_HHmmss"') do set STAMP=%%i
if exist db.sqlite3 copy db.sqlite3 "backups\horizon_sis_%STAMP%.sqlite3"
echo Database backup saved in the backups folder.
pause
