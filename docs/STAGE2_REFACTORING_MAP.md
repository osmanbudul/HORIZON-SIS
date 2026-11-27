# HORIZON SIS — Stage 2 Refactoring Map

## Current structure observed in the supplied ZIP

- `config/settings.py` — Django settings; currently installs the `core` app.
- `config/urls.py` — includes `core.urls`.
- `core/models.py` — shared models for classes, subjects, students, staff,
  parents, attendance, exams, results, fees, payments and timetable.
- `core/views.py` — dashboard and feature views.
- `core/forms.py` — feature forms.
- `core/urls.py` — application routes.
- `core/templates/` — existing templates.
- `core/static/core/` — existing CSS.
- `core/management/commands/seed_subjects.py` — subject seeding command.

## Safe migration sequence

1. Create a separate development copy and back up the live SQLite database.
2. Record the current URL list and take screenshots of working pages.
3. Run baseline Django checks and test the existing pages.
4. Decide model ownership and cross-app relationships before moving models.
5. Create destination apps and move one small feature at a time.
6. Update imports, app configuration, admin, forms, views, URL routing,
   templates, context processors and management commands.
7. Generate and inspect migrations. Do not delete or replace the live database.
8. Test against a COPY of the database first.
9. Verify login, permissions, CRUD operations, reports, parent portal and
   payment calculations.
10. Only after all tests pass, prepare the GitHub team repository.

## Important database note

The supplied ZIP does not contain `db.sqlite3`. The database currently used
by the running server must be backed up separately from the actual project
folder. Do not run destructive migration commands against the live database.
