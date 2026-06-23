<div align="center">

# 📋 Smart Task Management System

**A modern, real-time task management application built with Flask, PostgreSQL, and WebSockets.**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Socket.IO](https://img.shields.io/badge/Socket.IO-010101?style=for-the-badge&logo=socket.io&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)

</div>

---

## ✨ Features

- ✅ **User Authentication** — Secure registration and login with password hashing
- ✅ **Real-time Task Management** — Create, read, update, and delete tasks with live WebSocket updates
- ✅ **Task Analytics** — Track completion rates, pending tasks, and productivity metrics
- ✅ **Live Dashboard** — Real-time analytics with task statistics
- ✅ **Responsive Design** — Mobile-friendly UI with Tailwind CSS and Material Design
- ✅ **WebSocket Integration** — Real-time updates across all connected clients
- ✅ **Task Prioritization** — Set task priority (Low, Medium, High)
- ✅ **Task Status Tracking** — Monitor task progress (Pending, In Progress, Done)

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Flask, Flask-SQLAlchemy, Flask-SocketIO |
| **Database** | PostgreSQL with psycopg2 |
| **Frontend** | HTML5, Vanilla JavaScript, Tailwind CSS, Material Symbols |
| **Real-time** | Socket.IO |
| **Analytics** | Pandas, NumPy |

---

## 📦 Prerequisites

- Python 3.8+
- PostgreSQL 12+
- pip (Python package manager)

---

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/soudasMukherjee/smart-task-manager.git
cd smart-task-manager
```

### 2. Create a Python Virtual Environment
```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows (PowerShell):**
```bash
.\venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```bash
.\venv\Scripts\activate.bat
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Set Up Environment Variables
```bash
cp .env.example .env
```

Then edit `.env` and configure:
- `DATABASE_URL` — PostgreSQL connection string
- `SECRET_KEY` — Change to a random secure key for production
- `SOCKETIO_CORS_ALLOWED_ORIGINS` — Allowed origins for WebSocket connections

**Example `.env`:**
```env
DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/smart_task_db
SECRET_KEY=your-secret-key-here
SOCKETIO_CORS_ALLOWED_ORIGINS=*
FLASK_ENV=development
```

### 6. Create the PostgreSQL Database
```bash
createdb smart_task_db
```

Or using `psql`:
```sql
CREATE DATABASE smart_task_db;
```

### 7. Run the Application
```bash
python app.py
```

The application will start at `http://localhost:5000`

---

## 📖 Usage

**1. Register a New Account** — Navigate to `http://localhost:5000/register`, enter username, email, and password, then click "Create Account."

**2. Login** — Navigate to `http://localhost:5000/`, enter your username and password, then click "Sign In."

**3. Dashboard** — View real-time analytics, task statistics, and productivity metrics.

**4. Manage Tasks** — Go to the Tasks page to add, update, or delete tasks, set priority/status, and track completion percentage in real time.

---

## 🔌 API Endpoints

### Authentication
| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/register` | Register new user |
| `POST` | `/api/login` | Login user |
| `POST` | `/api/logout` | Logout user |

### Tasks
| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/tasks` | Get all user tasks |
| `POST` | `/api/tasks` | Create new task |
| `PUT` | `/api/tasks/<id>` | Update task |
| `DELETE` | `/api/tasks/<id>` | Delete task |
| `GET` | `/api/analytics` | Get task analytics |

---

## 📁 Project Structure

```
smart-task-manager/
├── app.py                  # Flask app factory and entry point
├── config.py               # Configuration management
├── requirements.txt        # Python dependencies
├── .env.example             # Example environment variables
├── database/
│   └── db.py                # SQLAlchemy database instance
├── models/
│   ├── user.py               # User model with authentication
│   └── task.py               # Task model
├── routes/
│   ├── auth_routes.py         # Authentication endpoints
│   ├── task_routes.py         # Task management endpoints
│   └── web_pages.py           # Web page routes
├── websocket/
│   ├── __init__.py
│   └── socket_events.py       # WebSocket event handlers
├── analytics/
│   └── task_analytics.py      # Analytics computation
├── static/
│   ├── css/
│   │   └── styles.css         # Custom CSS
│   └── js/
│       ├── auth.js            # Authentication JavaScript
│       ├── tasks.js           # Tasks management JavaScript
│       └── websocket.js       # WebSocket client
└── templates/
    ├── login.html           # Login page
    ├── register.html        # Registration page
    ├── dashboard.html       # Dashboard with analytics
    └── my_tasks.html         # Tasks management page
```

---

## 🩹 Troubleshooting

**Database Connection Error**
- Ensure PostgreSQL is running
- Check that the database exists: `createdb smart_task_db`
- Verify `DATABASE_URL` in `.env` is correct

**Module Not Found**
- Ensure virtual environment is activated
- Run `pip install -r requirements.txt` again

**WebSocket Connection Failed**
- Check that the Flask-SocketIO server is running
- Verify `SOCKETIO_CORS_ALLOWED_ORIGINS` in config.py

---

## 🔮 Future Enhancements

- Task categories/tags
- Task due dates and reminders
- Team collaboration features
- Email notifications
- Task templates
- Advanced filtering and search
- Dark mode toggle
- Mobile app

---

## 📄 License

MIT License — feel free to use and modify.

## 💬 Support

For issues or questions, please open an issue in the repository.
For issues or questions, please create an issue in the repository.


