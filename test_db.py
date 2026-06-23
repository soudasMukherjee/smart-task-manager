import psycopg2
import sys

passwords = ['', 'postgres', '123456', 'password', 'admin', 'postgres123']

for pwd in passwords:
    try:
        conn = psycopg2.connect(
            host='localhost',
            user='postgres',
            password=pwd,
            database='postgres'
        )
        print(f'✅ SUCCESS: PostgreSQL password is: {repr(pwd)}')
        
        # Try to create database
        conn.autocommit = True
        cur = conn.cursor()
        
        try:
            cur.execute('SELECT 1 FROM pg_database WHERE datname = %s', ('smart_task_db',))
            if not cur.fetchone():
                cur.execute('CREATE DATABASE smart_task_db')
                print('✅ Database created successfully')
            else:
                print('✅ Database already exists')
        except Exception as db_err:
            print(f'Database creation error: {db_err}')
        
        cur.close()
        conn.close()
        sys.exit(0)
    except Exception as e:
        pass

print('❌ Could not connect to PostgreSQL with default passwords')
print('⚠️  Please enter your PostgreSQL password in .env file')
