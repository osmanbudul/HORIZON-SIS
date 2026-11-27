@echo off
cd /d "%~dp0"
if not exist venv\Scripts\python.exe (
  echo Creating Python virtual environment...
  py -m venv venv
  if errorlevel 1 python -m venv venv
)
call venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py makemigrations core
python manage.py migrate
python manage.py seed_subjects
if not exist db.sqlite3 echo Database initialization complete.
echo.
echo Create your school administrator account if this is the first run:
echo   python manage.py createsuperuser
echo.
set /p CREATEADMIN=Do you need to create the administrator now? (y/n):
if /I "%CREATEADMIN%"=="y" python manage.py createsuperuser
 echo.
echo Starting HORIZON SIS at http://127.0.0.1:8000
python manage.py runserver
pause
