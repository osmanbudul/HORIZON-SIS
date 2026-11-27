# HORIZON SIS — Team Collaboration Plan (Stage 1)

## Important: current application structure is preserved

The current working Django application remains in `core/`. This is intentional.
The current models, views, forms, URLs, templates, static files, settings and
management commands have NOT been moved or rewritten in this Stage 1 package.

Moving Django model/view files into new apps without updating imports,
`INSTALLED_APPS`, URL routing and migrations can break the running system.
Stage 1 therefore prepares clear ownership boundaries without changing runtime
behavior. The actual Django app split is Stage 2 and must be tested separately.

## Team ownership

| Member | Responsibility | Current source area to study |
|---|---|---|
| Student 1 — Manager | Integration, architecture, review, testing, README and GitHub administration | `config/`, integration decisions, project root |
| Student 2 | Student registration, search and editing | Student sections in `core/models.py`, `core/forms.py`, `core/views.py`, `core/urls.py` |
| Student 3 | Attendance records and attendance reporting | Attendance sections in the same `core/` files |
| Student 4 | Classes, subjects, exams and results | Academic sections in the same `core/` files |
| Student 5 | Fees, payments and balances | Finance sections in the same `core/` files |
| Student 6 | Staff, timetable and parent portal | Staff/timetable/parent sections in the same `core/` files |

## File ownership rule for Stage 1

Because the current system is a single Django app, several features share the
same Python files. Students must NOT independently edit the same shared file
at the same time.

Before coding, the Manager assigns one feature task at a time and coordinates
changes to shared files. Prefer separate templates, static assets, tests and
documentation for independent work. The Manager integrates changes to shared
Python files and checks for conflicts.

## Proposed Stage 2 Django app layout

This is the target layout, not an implemented move in Stage 1:

- `apps/core/` — dashboard and shared integration
- `apps/students/` — student records
- `apps/attendance/` — attendance
- `apps/academics/` — classes, subjects, exams and results
- `apps/finance/` — fees and payments
- `apps/staff/` — staff and teachers
- `apps/parents/` — parent accounts and portal
- `apps/timetable/` — timetable

Stage 2 must also update imports, `INSTALLED_APPS`, URL includes, templates,
admin registration, management commands and migrations. Do not delete the old
`core/` app until the new layout passes checks and the database is verified.

## GitHub collaboration rules

1. `main` is the stable branch. Do not push unfinished work directly to it.
2. Each student works on their own feature branch.
3. Each student makes at least three meaningful commits for their own work.
4. Each student opens a Pull Request.
5. The Manager reviews the changed files and tests the feature before merging.
6. Do not commit `db.sqlite3`, `.env`, virtual environments, passwords or backups.
7. Keep the original project backup outside the Git repository.

Suggested branches:
- Manager: `feature/manager`
- Student 2: `feature/students`
- Student 3: `feature/attendance`
- Student 4: `feature/academics`
- Student 5: `feature/finance`
- Student 6: `feature/parents-staff-timetable`

## Pre-GitHub checklist

- [ ] Confirm the project starts on the Manager's computer.
- [ ] Keep a separate copy of the working database.
- [ ] Confirm no real student data or passwords are included in the repository.
- [ ] Review `.gitignore`.
- [ ] Complete Stage 2 refactoring and test it before the first team push.
- [ ] Add the real names and GitHub usernames of all six students.
