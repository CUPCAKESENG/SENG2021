function getCookie(name) {
	let value = `; ${document.cookie}`;
	console.log(value);
	let parts = value.split(`; ${name}=`);
	if (parts.length === 2) return parts.pop().split(';').shift();
}

function checkLoggedIn() {
	if (getCookie('token') == '') {
		window.location.href = '/login.html'
	}
}

checkLoggedIn()