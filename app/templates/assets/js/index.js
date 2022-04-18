function logout() {
	document.cookie = 'token=; path=/;'
	window.location.href = '/login.html'
}

function getCookie(name) {
	let value = `; ${document.cookie}`;
	console.log(value);
	let parts = value.split(`; ${name}=`);
	if (parts.length === 2) return parts.pop().split(';').shift();
}

async function setName() {
	const response = await fetch(`/user/name?token=${getCookie('token')}`, {
		method: 'GET',
		headers: {'Content-Type': 'application/json'},
	});
	
	response.json().then(data => {
		document.getElementById('username').innerHTML = data.name;
		document.getElementById('username').classList.remove('d-none')
	});
}

function init() {
	setName()
}

document.addEventListener("DOMContentLoaded", () => {  
	window.onload = init
});