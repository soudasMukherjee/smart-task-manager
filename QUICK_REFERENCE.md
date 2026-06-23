# Smart Task Manager - Quick Reference Card

## 🚀 START HERE

### Windows
```bash
.\run.bat
# Then visit http://localhost:5000
```

### Linux/Mac
```bash
chmod +x run.sh
./run.sh
# Then visit http://localhost:5000
```

---

## 📝 First Time Setup

1. **Clone/Download** the project
2. **Run startup script** (`run.bat` or `run.sh`)
3. **Configure `.env`** with database URL
4. **Visit** `http://localhost:5000`
5. **Register** a new account
6. **Start** managing tasks!

---

## 🔗 Important URLs

| Page | URL |
|------|-----|
| Login | `http://localhost:5000` |
| Register | `http://localhost:5000/register` |
| Dashboard | `http://localhost:5000/dashboard` |
| Tasks | `http://localhost:5000/my_tasks` |

---

## 📚 Documentation Files

| File | Purpose |
|------|---------|
| `README.md` | Full project overview |
| `QUICK_START.md` | Setup guide |
| `DATABASE_SETUP.md` | Database config |
| `TESTING_GUIDE.md` | Testing scenarios |
| `ARCHITECTURE.md` | Technical design |
| `DEPLOYMENT.md` | Production deploy |
| `PROJECT_COMPLETION.md` | Completion status |

---

## 💻 Useful Commands

### Development
```bash
# Activate virtual environment
source venv/bin/activate      # Linux/Mac
.\venv\Scripts\activate.bat   # Windows

# Install dependencies
pip install -r requirements.txt

# Run app
python app.py

# Access app
# Visit http://localhost:5000
```

### Database
```bash
# Create database
createdb smart_task_db

# Connect to database
psql -U postgres smart_task_db

# Reset database
dropdb smart_task_db
createdb smart_task_db
```

### Testing
```bash
# Register user
curl -X POST http://localhost:5000/api/register \
  -H "Content-Type: application/json" \
  -d '{"username":"test","email":"test@example.com","password":"pass"}'

# Create task
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Task","priority":"High","status":"Pending"}' \
  -b cookies.txt
```

---

## ⚙️ Configuration

### Environment Variables (`.env`)
```
DATABASE_URL=postgresql+psycopg2://postgres:password@localhost:5432/smart_task_db
SECRET_KEY=dev-secret-key
SOCKETIO_CORS_ALLOWED_ORIGINS=*
FLASK_ENV=development
```

### Port Configuration
- Default: `5000`
- To change: Edit last line of `app.py`

---

## 📊 API Endpoints

### Authentication
```
POST   /api/register        # Register user
POST   /api/login           # Login user
POST   /api/logout          # Logout user
```

### Tasks
```
GET    /api/tasks           # Get all tasks
POST   /api/tasks           # Create task
PUT    /api/tasks/{id}      # Update task
DELETE /api/tasks/{id}      # Delete task
GET    /api/analytics       # Get analytics
```

---

## 🧪 Quick Test Workflow

1. **Register** at `/register`
2. **Login** at `/`
3. **Create tasks** on dashboard or tasks page
4. **Update status** to see analytics change
5. **Open two windows** to see real-time sync
6. **Logout** when done

---

## 🆘 Troubleshooting

| Issue | Solution |
|-------|----------|
| Port 5000 already in use | Change port in `app.py` |
| Database connection error | Verify PostgreSQL running, check `.env` |
| Module not found | Run `pip install -r requirements.txt` |
| WebSocket not connecting | Check browser console (F12) |
| Can't login | Verify username (not email) in login form |

---

## 📁 Project Structure

```
smart-task-manager/
├── app.py                  # Main Flask app
├── config.py              # Configuration
├── requirements.txt       # Dependencies
├── .env.example          # Config template
├── run.bat/run.sh        # Startup scripts
├── database/             # Database
├── models/               # Data models
├── routes/               # API routes
├── websocket/            # Real-time
├── analytics/            # Analytics
├── static/               # CSS/JS
└── templates/            # HTML pages
```

---

## 🔐 Security Tips

- ✅ Change `SECRET_KEY` in production
- ✅ Use strong passwords
- ✅ Enable HTTPS in production
- ✅ Keep dependencies updated
- ✅ Use `.env` for secrets
- ✅ Don't commit `.env` to Git

---

## 📈 Features

- User authentication
- Task management (CRUD)
- Real-time updates (WebSocket)
- Analytics dashboard
- Responsive design
- Multi-window sync
- Secure password hashing

---

## 🎯 Common Tasks

### Create a Task
1. Go to Tasks page
2. Fill in title (required)
3. Add description (optional)
4. Select priority
5. Click "Add Task"

### Update Task Status
1. Find task in table
2. Click status dropdown
3. Select new status
4. Analytics update in real-time

### Delete a Task
1. Find task in table
2. Click "Delete" button
3. Task removed immediately

### View Analytics
1. Go to Dashboard
2. See metrics cards:
   - Total Tasks
   - Completion %
   - Pending Tasks
   - Completed Tasks

---

## 🚀 Production Deployment

```bash
# See DEPLOYMENT.md for full instructions

# Quick summary:
1. Install Gunicorn: pip install gunicorn
2. Configure Nginx
3. Set up PostgreSQL
4. Enable SSL
5. Configure firewall
6. Start Gunicorn service
```

---

## 📞 Need Help?

1. Check **QUICK_START.md** for setup issues
2. Check **DATABASE_SETUP.md** for database issues
3. Check **TESTING_GUIDE.md** for testing
4. Check **DEPLOYMENT.md** for production issues
5. Check browser console (F12) for JavaScript errors

---

## ✅ Verification

Everything working?
- [ ] App starts without errors
- [ ] Can register and login
- [ ] Can create tasks
- [ ] Tasks update in real-time
- [ ] Analytics show correctly
- [ ] UI is responsive
- [ ] Logout works

All checked? **You're ready to go!** 🎉

---

## 💡 Pro Tips

- Open 2 browser windows to see real-time sync
- Use browser DevTools (F12) to monitor network
- Check logs with: `tail -f logs/app.log`
- Backup database regularly
- Test features before deploying to production

---

Last Updated: 2026-06-07
Version: 1.0.0 (Complete & Ready)
