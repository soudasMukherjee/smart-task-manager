// Socket.IO client for live updates
const socket = io({
  withCredentials: true
});

function refreshAll() {
  // tasks.js defines these globally after load
  if (typeof loadTasks === 'function') loadTasks().catch(() => {});
  if (typeof loadAnalytics === 'function') loadAnalytics().catch(() => {});
}

socket.on('connect', () => {
  // Optional: could emit a join event if server requires it
});

socket.on('task_added', () => refreshAll());
socket.on('task_updated', () => refreshAll());
socket.on('task_deleted', () => refreshAll());

