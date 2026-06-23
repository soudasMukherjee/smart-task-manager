# Database Setup Instructions

## Prerequisites
- PostgreSQL 12 or higher installed
- psql command-line tool available
- PostgreSQL server running

## Quick Setup

### Windows

#### 1. Open PostgreSQL Command Line
```bash
# Using psql with default user (postgres)
psql -U postgres
```

#### 2. Create Database
```sql
CREATE DATABASE smart_task_db;
```

#### 3. Exit psql
```
\q
```

### macOS/Linux

```bash
# Create database
createdb smart_task_db

# Verify it was created
psql -l
```

## Verify Database

```bash
# Connect to the database
psql -U postgres smart_task_db

# List tables (should be empty on first run)
\dt

# Exit
\q
```

## Flask Will Auto-Create Tables

When you run `python app.py` for the first time, Flask-SQLAlchemy will:
1. Connect to the database specified in `DATABASE_URL`
2. Create all tables defined in the models (users, tasks)
3. Initialize the schema

## Database Reset (if needed)

**WARNING: This will delete all data!**

```bash
# Connect to PostgreSQL
psql -U postgres

# Drop the database
DROP DATABASE smart_task_db;

# Recreate it
CREATE DATABASE smart_task_db;

# Exit
\q
```

## Connection String Format

PostgreSQL connection strings follow this format:
```
postgresql+psycopg2://username:password@host:port/database
```

Example `.env` values:
```
# Default local setup
DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/smart_task_db

# With different password
DATABASE_URL=postgresql+psycopg2://postgres:mypassword@localhost:5432/smart_task_db

# Remote server
DATABASE_URL=postgresql+psycopg2://user:pass@remote-host.com:5432/smart_task_db
```

## Verify Connection

Update your `.env` and run:
```python
python
>>> from app import app, db
>>> with app.app_context():
...     db.create_all()
...     print("Tables created successfully!")
```

If successful, you'll see "Tables created successfully!" and the tables will be created in PostgreSQL.

## View Tables in Database

```bash
psql -U postgres smart_task_db

# List all tables
\dt

# Describe users table
\d users

# Describe tasks table
\d tasks

# Query data
SELECT * FROM users;
SELECT * FROM tasks;
```

## Troubleshooting

### "FATAL: Ident authentication failed for user 'postgres'"
**Solution**: Edit `postgresql.conf` or use password auth:
```bash
psql -U postgres -h localhost smart_task_db
```

### "Database does not exist"
**Solution**: Create it:
```bash
createdb smart_task_db
```

### "Connection refused"
**Solution**: PostgreSQL server isn't running
- Windows: Start PostgreSQL service
- macOS: `brew services start postgresql`
- Linux: `sudo service postgresql start`

### "Password authentication failed"
**Solution**: Check your password in `.env` and PostgreSQL user password

## Backup Database

```bash
# Backup
pg_dump smart_task_db > backup.sql

# Restore
psql smart_task_db < backup.sql
```

## Delete All User Data

If you want to clear all data while keeping the database:
```bash
psql -U postgres smart_task_db

DELETE FROM tasks;
DELETE FROM users;
```
