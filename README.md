# HORIZON SIS — Hargeisa International School

A modern Django-based School Information System designed for local/offline operation on a Windows laptop.

## Included modules
- Overview dashboard and school statistics
- Student registration, search, pagination and editing
- Staff & Teachers in one combined module
- Classes and Subjects
- Daily Attendance records
- Exams and subject-level Results (supports ten or more subjects)
- Fees and payment balance tracking
- Timetable
- Reports with print support
- Parent accounts and a private parent portal
- Django administration, local SQLite database and database backup script

## Requirements
- Windows 10/11
- Python 3.10 or newer (Python 3.12 recommended)
- Internet is needed only for the first installation to download Django. After installation, the local system can run without internet.

## Quick start (Windows)
1. Extract the complete ZIP into a folder such as `C:\HorizonSIS`.
2. Install Python and enable **Add Python to PATH** during installation.
3. Double-click `run_windows.bat`.
4. On first run, answer `y` when asked to create the administrator account.
5. Open `http://127.0.0.1:8000` in Chrome or Edge.

Alternative commands from Command Prompt in the project folder:
```bat
py -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
python manage.py makemigrations core
python manage.py migrate
python manage.py seed_subjects
python manage.py createsuperuser
python manage.py runserver
```

## First setup
1. Sign in using the administrator username and password you created.
2. Add school classes from **Classes**.
3. Review/edit the ten starter subjects from **Subjects**.
4. Add staff and teachers.
5. Register students and assign each to a class.
6. Record attendance, exams, results and fee records.

## Parent portal setup
1. Open `/admin/` while signed in as a school administrator.
2. Under **Users**, create a separate login for each parent (do not share parent accounts).
3. Under **Parent profiles**, create a profile, select the matching User, and link only that parent's child/children.
4. The parent signs in at `/login/` and opens **Parent Portal**. The portal only displays students linked to that parent's profile.

## Backup
Run `backup_database.bat`. A timestamped copy of `db.sqlite3` is placed in the `backups` folder. Keep backups on a separate drive as well.

## Important deployment note
The included edition is a local school-office application. It works on the laptop without internet after installation. The Parent Portal is implemented with individual parent logins and access restrictions, but parents outside the school network cannot reach a laptop-only `127.0.0.1` address. To provide secure access from home, the system must be deployed to a secure hosting server with HTTPS, production settings, scheduled backups and a deliberate data-sync plan. Do not expose Django's development server directly to the public internet.

## Security and data
- Use strong unique passwords for staff and parents.
- Create one parent account per family and link only their children.
- Back up the database regularly.
- Before real student data is entered, configure a production SECRET_KEY, DEBUG=False, secure hosts/HTTPS and a proper deployment environment.

## Technology
Python · Django · SQLite · HTML · CSS · Responsive interface
## Team Members
- Asma Raapi
## how run
1. pip install -r requirements.txt
2. python manage.py migrate
3. python manage.py runserver
## features
- Student CRUD
- Search
-Form Validation