<<<<<<< HEAD
# smart-task-manager
=======
# Smart Task Management System

A modern, real-time task management application built with Flask, PostgreSQL, and WebSockets.

## Features

- ✅ **User Authentication** - Secure registration and login with password hashing
- ✅ **Real-time Task Management** - Create, read, update, and delete tasks with live WebSocket updates
- ✅ **Task Analytics** - Track completion rates, pending tasks, and productivity metrics
- ✅ **Live Dashboard** - Real-time analytics with task statistics
- ✅ **Responsive Design** - Mobile-friendly UI with Tailwind CSS and Material Design
- ✅ **WebSocket Integration** - Real-time updates across all connected clients
- ✅ **Task Prioritization** - Set task priority (Low, Medium, High)
- ✅ **Task Status Tracking** - Monitor task progress (Pending, In Progress, Done)

## Tech Stack

- **Backend**: Flask, Flask-SQLAlchemy, Flask-SocketIO
- **Database**: PostgreSQL with psycopg2
- **Frontend**: HTML5, Vanilla JavaScript, Tailwind CSS, Material Symbols
- **Real-time**: Socket.IO
- **Analytics**: Pandas, NumPy

## Prerequisites

- Python 3.8+
- PostgreSQL 12+
- pip (Python package manager)

## Installation & Setup

### 1. Clone or Download the Repository
```bash
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
- `DATABASE_URL` - PostgreSQL connection string
- `SECRET_KEY` - Change to a random secure key for production
- `SOCKETIO_CORS_ALLOWED_ORIGINS` - Allowed origins for WebSocket connections

**Example `.env`:**
```
DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/smart_task_db
SECRET_KEY=your-secret-key-here
SOCKETIO_CORS_ALLOWED_ORIGINS=*
FLASK_ENV=development
```

### 6. Create PostgreSQL Database
```bash
# Connect to PostgreSQL and create the database
createdb smart_task_db
```

Or using psql:
```sql
CREATE DATABASE smart_task_db;
```

### 7. Run the Application
```bash
python app.py
```

The application will start at `http://localhost:5000`

## Usage

### 1. Register a New Account
- Navigate to `http://localhost:5000/register`
- Enter username, email, and password
- Click "Create Account"

### 2. Login
- Navigate to `http://localhost:5000/`
- Enter your username and password
- Click "Sign In"

### 3. Dashboard
- View real-time analytics and task statistics
- See your task momentum and productivity metrics

### 4. Manage Tasks
- Go to the Tasks page to manage all your tasks
- Add new tasks with title, description, priority, and status
- Update task status with real-time WebSocket updates
- Delete tasks as needed
- View completion percentage and task analytics

## API Endpoints

### Authentication
- `POST /api/register` - Register new user
- `POST /api/login` - Login user
- `POST /api/logout` - Logout user

### Tasks
- `GET /api/tasks` - Get all user tasks
- `POST /api/tasks` - Create new task
- `PUT /api/tasks/<id>` - Update task
- `DELETE /api/tasks/<id>` - Delete task
- `GET /api/analytics` - Get task analytics

## Project Structure

```
smart-task-manager/
├── app.py                 # Flask app factory and entry point
├── config.py             # Configuration management
├── requirements.txt      # Python dependencies
├── .env.example         # Example environment variables
├── database/
│   └── db.py            # SQLAlchemy database instance
├── models/
│   ├── user.py          # User model with authentication
│   └── task.py          # Task model
├── routes/
│   ├── auth_routes.py   # Authentication endpoints
│   ├── task_routes.py   # Task management endpoints
│   └── web_pages.py     # Web page routes
├── websocket/
│   ├── __init__.py
│   └── socket_events.py # WebSocket event handlers
├── analytics/
│   └── task_analytics.py # Analytics computation
├── static/
│   ├── css/
│   │   └── styles.css   # Custom CSS
│   └── js/
│       ├── auth.js      # Authentication JavaScript
│       ├── tasks.js     # Tasks management JavaScript
│       └── websocket.js # WebSocket client
└── templates/
    ├── login.html       # Login page
    ├── register.html    # Registration page
    ├── dashboard.html   # Dashboard with analytics
    └── my_tasks.html    # Tasks management page
```

## Troubleshooting

### Database Connection Error
- Ensure PostgreSQL is running
- Check that the database exists: `createdb smart_task_db`
- Verify `DATABASE_URL` in `.env` is correct

### Module Not Found
- Ensure virtual environment is activated
- Run `pip install -r requirements.txt` again

### WebSocket Connection Failed
- Check that the Flask-SocketIO server is running
- Verify `SOCKETIO_CORS_ALLOWED_ORIGINS` in config.py

## Future Enhancements

- Task categories/tags
- Task due dates and reminders
- Team collaboration features
- Email notifications
- Task templates
- Advanced filtering and search
- Dark mode toggle
- Mobile app

## License

MIT License - Feel free to use and modify

## Support

For issues or questions, please create an issue in the repository.

>>>>>>> e817af6 (Initial commit)
