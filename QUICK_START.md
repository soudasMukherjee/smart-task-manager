# Smart Task Manager - Quick Start Guide

## 🚀 Quick Start (Windows)

### Option 1: Using the Run Script (Recommended)
1. Open PowerShell or CMD in the project directory
2. Run: `.\run.bat`
3. Follow the prompts to set up and start the server
4. Visit `http://localhost:5000`

### Option 2: Manual Setup
1. Create and activate virtual environment:
   ```
   python -m venv venv
   .\venv\Scripts\activate.bat
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create `.env` file and configure database:
   ```
   copy .env.example .env
   ```

4. Edit `.env` with your PostgreSQL connection:
   ```
   DATABASE_URL=postgresql+psycopg2://postgres:password@localhost:5432/smart_task_db
   ```

5. Create the database in PostgreSQL:
   ```
   createdb smart_task_db
   ```

6. Run the app:
   ```
   python app.py
   ```

7. Open browser: `http://localhost:5000`

## 🚀 Quick Start (macOS/Linux)

1. Run setup script:
   ```
   chmod +x run.sh
   ./run.sh
   ```

Or manually:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python3 app.py
```

## 📝 Testing Workflow

### 1. Register New User
- Go to `http://localhost:5000/register`
- Create account with username, email, and password
- Click "Create Account"

### 2. Login
- Return to `http://localhost:5000`
- Enter credentials
- Click "Sign In"

### 3. Dashboard
- View real-time analytics
- See task momentum chart
- View urgent tasks

### 4. Task Management
- Click "Tasks" in bottom navigation
- Add a new task with:
  - Title (required)
  - Description (optional)
  - Priority (Low/Medium/High)
  - Status (Pending/In Progress/Done)
- Create multiple tasks to see analytics update in real-time
- Update task status - changes appear instantly via WebSocket
- Delete tasks

### 5. Real-time Updates
- Open the app in two browser windows side-by-side
- Update a task in one window
- Watch it update in real-time in the other window (WebSocket working!)

## 🔧 Troubleshooting

### Port Already in Use
If port 5000 is in use, modify app.py:
```python
socketio.run(app, host="0.0.0.0", port=5001, debug=True)
```

### PostgreSQL Not Found
```bash
# Windows - Install PostgreSQL from: https://www.postgresql.org/download/windows/
# macOS: brew install postgresql@14
# Linux: sudo apt-get install postgresql
```

### Database Connection Error
1. Verify PostgreSQL is running
2. Check database exists: `psql -l`
3. Create if needed: `createdb smart_task_db`
4. Verify credentials in `.env`

### Module Import Errors
```bash
pip install --upgrade -r requirements.txt
```

### WebSocket Not Connecting
1. Check browser console for errors (F12)
2. Verify Socket.IO server is running
3. Check CORS settings in config.py

## 📊 Key Features to Test

- ✅ User registration with unique username/email validation
- ✅ Secure login with password hashing
- ✅ Task CRUD operations
- ✅ Real-time task updates via WebSocket
- ✅ Analytics dashboard with live statistics
- ✅ Task prioritization (Low/Medium/High)
- ✅ Task status tracking (Pending/In Progress/Done)
- ✅ Completion percentage tracking
- ✅ Responsive mobile-friendly UI
- ✅ Logout functionality

## 🎯 API Testing with cURL or Postman

### Register
```bash
curl -X POST http://localhost:5000/api/register \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","email":"test@example.com","password":"password123"}' \
  -c cookies.txt
```

### Login
```bash
curl -X POST http://localhost:5000/api/login \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","password":"password123"}' \
  -c cookies.txt
```

### Get Tasks
```bash
curl -X GET http://localhost:5000/api/tasks \
  -b cookies.txt
```

### Create Task
```bash
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"My Task","description":"Task details","priority":"High","status":"Pending"}' \
  -b cookies.txt
```

### Get Analytics
```bash
curl -X GET http://localhost:5000/api/analytics \
  -b cookies.txt
```

## 📱 Browser DevTools Tips

### Check Network Tab
- Verify API calls are successful (200/201 status)
- Monitor WebSocket connections
- See real-time data flowing

### Check Console Tab
- Look for JavaScript errors
- Verify Socket.IO connection messages
- Debug API response data

### Check Application Tab
- View session cookies
- Monitor local storage
- Track WebSocket frames

## 🎨 Customization

### Change App Colors
Edit `templates/` files and modify Tailwind color variables in the `<script id="tailwind-config">` section

### Change Port
Edit `app.py` last line:
```python
socketio.run(app, host="0.0.0.0", port=8000, debug=True)
```

### Change Database
Update `DATABASE_URL` in `.env` to point to different PostgreSQL instance

## ✨ Next Steps

After verifying everything works:
1. Deploy to production server
2. Set up proper environment variables
3. Configure database backups
4. Enable HTTPS/SSL
5. Set up monitoring and logging
6. Add more features (categories, due dates, notifications)
