# Smart Task Manager - Architecture Overview

## Project Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Web Browser (Client)                     │
│  ┌──────────────────────────────────────────────────────┐   │
│  │          HTML/CSS/JavaScript (UI Layer)              │   │
│  │  - Login/Register Pages                             │   │
│  │  - Dashboard with Analytics                         │   │
│  │  - Task Management Interface                        │   │
│  └──────────────────────────────────────────────────────┘   │
│                    ↕ HTTP + WebSocket                        │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                   Flask Web Server (Port 5000)               │
│  ┌──────────────────────────────────────────────────────┐   │
│  │              Application Layer                       │   │
│  │  ┌────────────────────────────────────────────────┐  │   │
│  │  │        Routes (auth_routes, task_routes)      │  │   │
│  │  │  - POST /api/register  - User registration    │  │   │
│  │  │  - POST /api/login     - User authentication  │  │   │
│  │  │  - GET  /api/tasks     - Fetch user tasks     │  │   │
│  │  │  - POST /api/tasks     - Create task          │  │   │
│  │  │  - PUT  /api/tasks/:id - Update task          │  │   │
│  │  │  - DELETE /api/tasks/id - Delete task         │  │   │
│  │  │  - GET  /api/analytics - Get analytics        │  │   │
│  │  └────────────────────────────────────────────────┘  │   │
│  │                                                       │   │
│  │  ┌────────────────────────────────────────────────┐  │   │
│  │  │     WebSocket Events (socket_events.py)       │  │   │
│  │  │  - on_connect    - User joins room            │  │   │
│  │  │  - on_disconnect - User leaves room           │  │   │
│  │  │  - Emit events (task_added, task_updated...)  │  │   │
│  │  └────────────────────────────────────────────────┘  │   │
│  │                                                       │   │
│  │  ┌────────────────────────────────────────────────┐  │   │
│  │  │        Business Logic (analytics.py)          │  │   │
│  │  │  - compute_analytics(tasks)                   │  │   │
│  │  └────────────────────────────────────────────────┘  │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│               Data Layer (PostgreSQL Database)               │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  SQLAlchemy ORM (database/db.py)                    │   │
│  │  ┌────────────────┐      ┌────────────────┐        │   │
│  │  │  Users Table   │      │   Tasks Table  │        │   │
│  │  │ - id (PK)      │  ←→  │ - id (PK)      │        │   │
│  │  │ - username     │      │ - user_id (FK)│        │   │
│  │  │ - email        │      │ - title        │        │   │
│  │  │ - password_hash│      │ - description  │        │   │
│  │  │ - created_at   │      │ - priority     │        │   │
│  │  │ - tasks[]      │      │ - status       │        │   │
│  │  │                │      │ - created_at   │        │   │
│  │  │                │      │ - updated_at   │        │   │
│  │  └────────────────┘      └────────────────┘        │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

## Data Flow

### 1. User Registration Flow
```
Browser                          Flask Server               Database
   │                                 │                         │
   ├─ POST /api/register ────────→  │                         │
   │  (username, email, password)    │                         │
   │                                 ├─ Hash password          │
   │                                 ├─ Create User object    │
   │                                 ├─ INSERT into users ──→ │
   │                                 │                         │
   │                              ✓ ←─ 201 Created            │
   ← ─ {user_id, message} ────────┤                          │
```

### 2. Task Creation with WebSocket
```
Browser (Window 1)      Flask Server         Database      Browser (Window 2)
       │                     │                   │               │
       ├─ POST /api/tasks ──→│                   │               │
       │                     ├─ Validate task    │               │
       │                     ├─ INSERT task ────→│               │
       │                  ✓ ←─ 201 Created       │               │
       ←─ {task} ─────────┤                     │               │
       │                     ├─ Emit via WS ─────────────────→  │
       │                     │ (task_added event)               │
       │                     │                   │    ← Receive │
       │                     │                   │    ← Update UI│
```

### 3. Real-Time Analytics Update
```
Task Updated (any browser)          Flask Server            All Connected Browsers
         │                               │                          │
         ├─ PUT /api/tasks/:id ────────→│                          │
         │                              ├─ UPDATE task ───→ DB    │
         │                           ✓ ←─ 200 OK                  │
         ←─ {task} ─────────────────┤                            │
         │                           ├─ Emit task_updated ───────→│
         │                           │  (to room user_{id})       │
         │                           │                   ← All connected
         │                           │                   ← clients update
```

## Technology Stack Details

### Frontend Stack
- **HTML5**: Semantic markup with Tailwind CSS
- **CSS**: Tailwind CSS + Custom Material Design colors
- **JavaScript**: Vanilla ES6+ (no frameworks for simplicity)
- **Socket.IO Client**: Real-time WebSocket communication
- **Material Symbols**: Google Material Design icons

### Backend Stack
- **Framework**: Flask 3.0.3
- **ORM**: SQLAlchemy with Flask-SQLAlchemy
- **Real-time**: Flask-SocketIO with Socket.IO
- **Security**: Werkzeug for password hashing
- **CORS**: Flask-CORS for cross-origin requests
- **Database Driver**: psycopg2 for PostgreSQL

### Database
- **PostgreSQL 12+**: Relational database
- **Tables**: users, tasks
- **Relationships**: One-to-Many (User → Tasks)

### Analytics
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical operations
- **pytz**: Timezone handling

## Key Design Decisions

### 1. Session-Based Authentication
- Uses Flask sessions instead of JWT
- Pros: Simpler implementation, CSRF protection included
- Cons: Server-side session storage

### 2. WebSocket Rooms
- Each user has a dedicated WebSocket room: `user_{user_id}`
- Tasks updates only sent to the specific user
- Scalable for multi-user scenarios

### 3. Real-Time Updates
- Three event types: `task_added`, `task_updated`, `task_deleted`
- Immediate UI refresh without page reload
- Maintains data consistency across tabs/windows

### 4. Responsive Design
- Mobile-first approach
- Tailwind CSS breakpoints
- Touch-friendly UI elements

## API Request/Response Examples

### Successful Response
```json
{
  "tasks": [
    {
      "id": 1,
      "title": "Complete project",
      "description": "Finish Q3 report",
      "priority": "High",
      "status": "Pending",
      "created_at": "2024-06-07T10:30:00"
    }
  ]
}
```

### Error Response
```json
{
  "error": "Unauthorized"
}
```

## Security Measures

### 1. Password Security
- Passwords hashed using `werkzeug.security.generate_password_hash`
- SHA512 with salt
- Verified using `check_password_hash`

### 2. Session Management
- Sessions stored server-side
- Session IDs stored in HTTP-only cookies
- Auto-invalidated on logout

### 3. Input Validation
- All user inputs validated and sanitized
- SQL injection protected via SQLAlchemy ORM
- XSS protection via HTML escaping

### 4. CORS
- Configurable CORS origins
- Credentials required for cross-origin requests

## Performance Considerations

### 1. Database Indexing
- Unique index on `users.username`
- Unique index on `users.email`
- Foreign key index on `tasks.user_id`

### 2. Query Optimization
- Eager loading of relationships
- Filtering at database level
- Pagination support (can be added)

### 3. WebSocket Efficiency
- Room-based broadcasting (only relevant users receive updates)
- JSON serialization for compact data transfer
- Connection pooling for database

## Scalability Path

### Short Term (1-3 months)
- Add task categories/tags
- Implement task due dates
- Add email notifications

### Medium Term (3-6 months)
- Team collaboration features
- Task comments and mentions
- Advanced filtering and search
- Analytics dashboard with charts

### Long Term (6+ months)
- Mobile apps (iOS/Android)
- Integration with calendars
- API for third-party apps
- Advanced scheduling and automation

## Deployment Considerations

### Development
- Single-threaded Flask dev server
- SQLite or local PostgreSQL
- CORS: * (all origins)

### Staging
- Gunicorn with multiple workers
- Separate PostgreSQL database
- CORS: specific origins

### Production
- Nginx reverse proxy
- Gunicorn with load balancing
- PostgreSQL with backups
- HTTPS/SSL
- Environment-based configuration
- Health checks and monitoring
- Error tracking (Sentry)
- Logging aggregation (ELK stack)

## Monitoring & Logging

### Key Metrics to Monitor
- Page load time
- API response time
- WebSocket connection count
- Database query time
- Error rate
- User session count

### Recommended Tools
- New Relic or DataDog for APM
- ELK Stack for logging
- Prometheus for metrics
- Grafana for visualization

## Code Organization

```
smart-task-manager/
├── app.py              # Flask app factory
├── config.py           # Configuration
├── requirements.txt    # Dependencies
├── database/
│   └── db.py          # SQLAlchemy instance
├── models/
│   ├── user.py        # User model
│   └── task.py        # Task model
├── routes/
│   ├── auth_routes.py # Auth API endpoints
│   ├── task_routes.py # Task API endpoints
│   └── web_pages.py   # Page routes
├── websocket/
│   └── socket_events.py # WebSocket handlers
├── analytics/
│   └── task_analytics.py # Analytics logic
├── static/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       ├── auth.js
│       ├── tasks.js
│       └── websocket.js
└── templates/
    ├── login.html
    ├── register.html
    ├── dashboard.html
    └── my_tasks.html
```

## Testing Strategy

### Unit Tests
- Model validation
- Analytics computation
- Password hashing

### Integration Tests
- API endpoints
- Database operations
- WebSocket events

### End-to-End Tests
- User flows
- Real-time updates
- Error scenarios

## Future Enhancements

1. **Database**: Add Redis for caching and session storage
2. **API**: Add REST API versioning and pagination
3. **Frontend**: Add React/Vue for more interactive UI
4. **Authentication**: OAuth2/SSO integration
5. **Analytics**: Advanced charts and reports
6. **Infrastructure**: Docker containerization
7. **DevOps**: CI/CD pipeline with GitHub Actions
