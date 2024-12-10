const form = document.getElementById('userForm');
const tableBody = document.querySelector('#userTable tbody');

// Update the URL to use the backend service name
const backendUrl = 'http://34.134.154.5:5000'; 

form.addEventListener('submit', async (event) => {
    event.preventDefault();
    const username = document.getElementById('username').value;
    const cellphone = document.getElementById('cellphone').value;

    const response = await fetch(`${backendUrl}/add_user`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, cellphone })
    });

    if (response.ok) {
        alert('User added successfully');
        loadUsers();
    } else {
        alert('Error adding user');
    }
});

async function loadUsers() {
    const response = await fetch(`${backendUrl}/users`);
    const users = await response.json();

    tableBody.innerHTML = '';
    users.forEach(user => {
        const row = document.createElement('tr');
        row.innerHTML = `<td>${user.username}</td><td>${user.cellphone}</td>`;
        tableBody.appendChild(row);
    });
}

// Load users on page load
window.onload = loadUsers;
