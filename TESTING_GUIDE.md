# Smart Task Manager - Testing Guide

## Pre-Testing Checklist

- [ ] PostgreSQL server running
- [ ] `.env` file configured with correct database URL
- [ ] Virtual environment created and activated
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Database created (`createdb smart_task_db`)
- [ ] Flask app started (`python app.py`)

## Unit Testing Scenarios

### 1. User Registration

**Test Case 1.1: Valid Registration**
- Navigate to `http://localhost:5000/register`
- Enter:
  - Username: `testuser1`
  - Email: `test1@example.com`
  - Password: `password123`
- Click "Create Account"
- ✅ Expected: Redirect to login page
- ✅ Verify: User can login with these credentials

**Test Case 1.2: Duplicate Username**
- Try to register with existing username
- ✅ Expected: Error message "Username or email already exists"

**Test Case 1.3: Duplicate Email**
- Try to register with existing email
- ✅ Expected: Error message "Username or email already exists"

**Test Case 1.4: Empty Fields**
- Try to register with empty fields
- ✅ Expected: Browser validation prevents submission

**Test Case 1.5: Invalid Email Format**
- Register with invalid email
- ✅ Expected: Browser prevents submission

---

### 2. User Login

**Test Case 2.1: Valid Login**
- Navigate to `http://localhost:5000`
- Enter correct username and password
- Click "Sign In"
- ✅ Expected: Redirect to dashboard

**Test Case 2.2: Invalid Credentials**
- Enter wrong password
- ✅ Expected: Error message "Invalid credentials"

**Test Case 2.3: Non-existent User**
- Enter username that doesn't exist
- ✅ Expected: Error message "Invalid credentials"

**Test Case 2.4: Empty Username**
- Try to submit without username
- ✅ Expected: Browser validation prevents submission

---

### 3. Task Management

**Test Case 3.1: Create Task**
- Login successfully
- Go to Tasks page
- Fill in:
  - Title: "Complete project report"
  - Description: "Finish Q3 report"
  - Priority: "High"
  - Status: "Pending"
- Click "Add Task"
- ✅ Expected: Task appears in task list
- ✅ Expected: Analytics update in real-time

**Test Case 3.2: Create Task Without Description**
- Create task with empty description
- ✅ Expected: Task created successfully with empty description

**Test Case 3.3: Create Task Without Title**
- Try to create task without title
- ✅ Expected: Error message "title is required"

**Test Case 3.4: Update Task Status**
- Click status dropdown for a task
- Change to "In Progress"
- ✅ Expected: Task status updates immediately
- ✅ Expected: Analytics update

**Test Case 3.5: Delete Task**
- Click delete button on a task
- ✅ Expected: Task removed from list
- ✅ Expected: Analytics update

**Test Case 3.6: Multiple Tasks**
- Create 5+ tasks with different priorities and statuses
- ✅ Expected: All tasks display correctly
- ✅ Expected: Analytics show correct totals

---

### 4. Analytics

**Test Case 4.1: Total Tasks Count**
- Create 3 tasks
- ✅ Expected: "Total Tasks" shows 3

**Test Case 4.2: Completion Percentage**
- Create 4 tasks
- Mark 2 as "Done"
- ✅ Expected: "Completion %" shows 50%

**Test Case 4.3: Pending Tasks**
- Create 5 tasks:
  - 2 marked as "Done"
  - 1 marked as "In Progress"
  - 2 marked as "Pending"
- ✅ Expected: "Pending" shows 2

**Test Case 4.4: Completed Tasks**
- From above scenario
- ✅ Expected: "Completed" shows 2

**Test Case 4.5: Empty Tasks**
- Delete all tasks
- ✅ Expected: All analytics show 0
- ✅ Expected: Completion % shows 0%

---

### 5. WebSocket Real-Time Updates

**Test Case 5.1: Real-Time Task Addition**
- Open app in two browser windows (user logged in both)
- Window A: Add a new task
- ✅ Expected: Task appears in Window B without refresh

**Test Case 5.2: Real-Time Status Update**
- Window A: Update task status
- ✅ Expected: Change appears in Window B immediately
- ✅ Expected: Analytics update in both windows

**Test Case 5.3: Real-Time Task Deletion**
- Window A: Delete a task
- ✅ Expected: Task disappears from Window B immediately
- ✅ Expected: Analytics update

---

### 6. Session & Authentication

**Test Case 6.1: Logout**
- Click logout button
- ✅ Expected: Redirect to login page
- ✅ Expected: Cannot access dashboard without login

**Test Case 6.2: Session Persistence**
- Login, create a task
- Refresh page
- ✅ Expected: Still logged in
- ✅ Expected: Task still there

**Test Case 6.3: Unauthorized Access**
- Open dev tools, delete session cookie
- Try to access `/dashboard`
- ✅ Expected: Redirect to login

**Test Case 6.4: API Without Auth**
- Use curl without credentials:
  ```bash
  curl http://localhost:5000/api/tasks
  ```
- ✅ Expected: 401 error "Unauthorized"

---

### 7. Form Validation

**Test Case 7.1: Task Title Validation**
- Try to create task with whitespace-only title
- ✅ Expected: Error message

**Test Case 7.2: Priority Validation**
- Try to submit form with invalid priority
- ✅ Expected: Error message "Invalid priority"

**Test Case 7.3: Status Validation**
- Try to submit form with invalid status
- ✅ Expected: Error message "Invalid status"

---

### 8. Responsive Design

**Test Case 8.1: Mobile View (< 768px)**
- Open app on mobile or use device emulation
- ✅ Expected: Single column layout
- ✅ Expected: All elements accessible
- ✅ Expected: Buttons have adequate touch targets

**Test Case 8.2: Tablet View (768px - 1024px)**
- ✅ Expected: Responsive layout
- ✅ Expected: Tasks table scrolls horizontally if needed

**Test Case 8.3: Desktop View (> 1024px)**
- ✅ Expected: Full layout with optimal spacing

---

### 9. Error Handling

**Test Case 9.1: Database Connection Error**
- Stop PostgreSQL server
- Try to create a task
- ✅ Expected: Appropriate error message or graceful failure

**Test Case 9.2: Network Error**
- Open dev tools, set network to offline
- Try to create task
- ✅ Expected: Network error shown

**Test Case 9.3: WebSocket Disconnection**
- Disconnect from internet
- ✅ Expected: App continues to function (offline mode)
- ✅ Expected: WebSocket reconnects when online

---

## Browser DevTools Testing

### Check Console
1. Open DevTools (F12)
2. Go to Console tab
3. ✅ Expected: No JavaScript errors
4. ✅ Expected: See "connected" message from Socket.IO

### Check Network Tab
1. Open Network tab
2. Create a task
3. ✅ Expected: POST to `/api/tasks` shows 201 status
4. ✅ Expected: GET `/api/tasks` shows 200 status
5. ✅ Expected: WebSocket frame shows data transfer

### Check Performance
1. Open Performance tab
2. Record while using app
3. ✅ Expected: Page load time < 3 seconds
4. ✅ Expected: Task creation < 500ms

---

## API Testing (cURL Examples)

### 1. Register
```bash
curl -X POST http://localhost:5000/api/register \
  -H "Content-Type: application/json" \
  -d '{"username":"apiuser","email":"api@test.com","password":"pass123"}' \
  -v -c cookies.txt
```
✅ Expected: 201 status with user_id

### 2. Login
```bash
curl -X POST http://localhost:5000/api/login \
  -H "Content-Type: application/json" \
  -d '{"username":"apiuser","password":"pass123"}' \
  -c cookies.txt -v
```
✅ Expected: 200 status

### 3. Get Tasks (without auth)
```bash
curl http://localhost:5000/api/tasks -v
```
✅ Expected: 401 "Unauthorized"

### 4. Get Tasks (with auth)
```bash
curl http://localhost:5000/api/tasks \
  -b cookies.txt -v
```
✅ Expected: 200 status with tasks array

### 5. Create Task
```bash
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"API Task","description":"Created via API","priority":"High","status":"Pending"}' \
  -b cookies.txt -v
```
✅ Expected: 201 status with task object

### 6. Update Task
```bash
curl -X PUT http://localhost:5000/api/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"status":"Done"}' \
  -b cookies.txt -v
```
✅ Expected: 200 status

### 7. Delete Task
```bash
curl -X DELETE http://localhost:5000/api/tasks/1 \
  -b cookies.txt -v
```
✅ Expected: 200 status

### 8. Get Analytics
```bash
curl http://localhost:5000/api/analytics \
  -b cookies.txt -v
```
✅ Expected: 200 status with analytics data

---

## Performance Testing

### Load Testing
1. Create 100+ tasks in the database
2. Navigate to tasks page
3. ✅ Expected: Page loads in reasonable time
4. ✅ Expected: No UI freezing

### Memory Testing
1. Keep app open for 30+ minutes
2. Monitor browser memory usage
3. ✅ Expected: No significant memory leaks

---

## Security Testing

### 1. SQL Injection
- Try to create task with title: `'; DROP TABLE tasks; --`
- ✅ Expected: Task created normally (SQL safely escaped)

### 2. XSS Attack
- Try to create task with title: `<script>alert('XSS')</script>`
- ✅ Expected: Script doesn't execute (HTML escaped)

### 3. CSRF Protection
- ✅ Expected: Session-based authentication works
- ✅ Expected: Cross-site requests properly authenticated

---

## Test Results Summary Template

```markdown
## Test Run: [DATE]
- Tester: [NAME]
- Environment: [OS/Browser]
- Status: [PASS/PARTIAL/FAIL]

### Passed Tests
- [ ] User Registration: PASS
- [ ] User Login: PASS
- [ ] Task CRUD: PASS
- [ ] WebSocket Updates: PASS
- [ ] Analytics: PASS
- [ ] Responsive Design: PASS

### Failed Tests
- None

### Issues Found
- None

### Notes
- Everything working as expected
```

---

## Continuous Testing Checklist

After each deployment:
- [ ] Verify database connection
- [ ] Test user registration
- [ ] Test user login
- [ ] Create and manage tasks
- [ ] Check real-time updates in two windows
- [ ] Verify analytics accuracy
- [ ] Check browser console for errors
- [ ] Verify responsive design
- [ ] Test logout functionality
- [ ] Check API health via curl
