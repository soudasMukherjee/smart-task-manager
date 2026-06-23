async function postJSON(url, payload) {
  const res = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
    credentials: 'include'
  });
  const data = await res.json().catch(() => ({}));
  if (!res.ok) throw new Error(data.error || 'Request failed');
  return data;
}

function showError(msg) {
  const el = document.getElementById('error');
  if (!el) return;
  el.textContent = msg;
  el.style.display = 'block';
}

// Login
const loginForm = document.getElementById('loginForm');
if (loginForm) {
  loginForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    try {
      showError('');
      const form = new FormData(loginForm);
      const payload = {
        username: form.get('username'),
        password: form.get('password')
      };
      await postJSON('/api/login', payload);
      window.location.href = '/dashboard';
    } catch (err) {
      showError(err.message);
    }
  });
}

// Register
const registerForm = document.getElementById('registerForm');
if (registerForm) {
  registerForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    try {
      showError('');
      const form = new FormData(registerForm);
      const payload = {
        username: form.get('username'),
        email: form.get('email'),
        password: form.get('password')
      };
      await postJSON('/api/register', payload);
      window.location.href = '/';
    } catch (err) {
      showError(err.message);
    }
  });
}

// Logout button
const logoutBtn = document.getElementById('logoutBtn');
if (logoutBtn) {
  logoutBtn.addEventListener('click', async () => {
    await fetch('/api/logout', { method: 'POST', credentials: 'include' });
    window.location.href = '/';
  });
}

