async function apiJSON(url, options = {}) {
  const res = await fetch(url, {
    ...options,
    credentials: 'include',
    headers: {
      'Content-Type': 'application/json',
      ...(options.headers || {})
    }
  });
  const data = await res.json().catch(() => ({}));
  if (!res.ok) throw new Error(data.error || 'Request failed');
  return data;
}

function setError(msg) {
  const box = document.getElementById('errorBox');
  if (!box) return;
  if (!msg) {
    box.style.display = 'none';
    box.textContent = '';
    return;
  }
  box.textContent = msg;
  box.style.display = 'block';
}

function renderTasks(tasks) {
  const tbody = document.getElementById('tasksTbody');
  tbody.innerHTML = '';

  for (const t of tasks) {
    const tr = document.createElement('tr');

    tr.innerHTML = `
      <td>${t.title}</td>
      <td>${t.priority}</td>
      <td>
        <select data-task-id="${t.id}" class="statusSelect">
          <option ${t.status === 'Pending' ? 'selected' : ''}>Pending</option>
          <option ${t.status === 'In Progress' ? 'selected' : ''}>In Progress</option>
          <option ${t.status === 'Done' ? 'selected' : ''}>Done</option>
        </select>
      </td>
      <td>${new Date(t.created_at).toLocaleString()}</td>
      <td>
        <button class="btn btn-danger" data-del="${t.id}">Delete</button>
      </td>
    `;

    tbody.appendChild(tr);
  }

  tbody.querySelectorAll('.statusSelect').forEach(sel => {
    sel.addEventListener('change', async (e) => {
      const taskId = Number(e.target.getAttribute('data-task-id'));
      const status = e.target.value;
      await apiJSON(`/api/tasks/${taskId}`, {
        method: 'PUT',
        body: JSON.stringify({ status })
      });
      await loadTasks();
      await loadAnalytics();
      setError('');
    });
  });

  tbody.querySelectorAll('button[data-del]').forEach(btn => {
    btn.addEventListener('click', async () => {
      const taskId = Number(btn.getAttribute('data-del'));
      await apiJSON(`/api/tasks/${taskId}`, { method: 'DELETE' });
      await loadTasks();
      await loadAnalytics();
      setError('');
    });
  });
}

async function loadTasks() {
  const data = await apiJSON('/api/tasks', { method: 'GET' });
  renderTasks(data.tasks);
}

async function loadAnalytics() {
  const a = await apiJSON('/api/analytics', { method: 'GET' });
  document.getElementById('totalTasks').textContent = a.total_tasks;
  document.getElementById('completedTasks').textContent = a.completed_tasks;
  document.getElementById('pendingTasks').textContent = a.pending_tasks;
  document.getElementById('completionPct').textContent = `${a.completion_percentage}%`;
}

// Add Task
const taskForm = document.getElementById('taskForm');
if (taskForm) {
  taskForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    try {
      setError('');
      const form = new FormData(taskForm);
      const payload = {
        title: form.get('title'),
        description: form.get('description'),
        priority: form.get('priority'),
        status: form.get('status')
      };
      await apiJSON('/api/tasks', {
        method: 'POST',
        body: JSON.stringify(payload)
      });
      taskForm.reset();
      await loadTasks();
      await loadAnalytics();
    } catch (err) {
      setError(err.message);
    }
  });
}

// Initial load
loadTasks().catch(err => setError(err.message));
loadAnalytics().catch(err => setError(err.message));

