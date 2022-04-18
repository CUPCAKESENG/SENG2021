function getCookie(name) {
	let value = `; ${document.cookie}`;
	console.log(value);
	let parts = value.split(`; ${name}=`);
	if (parts.length === 2) return parts.pop().split(';').shift();
}

function init() {
	if (getCookie('token') == '') {
		window.location.href = '/login.html'
	}
}

document.addEventListener("DOMContentLoaded", () => {  
	window.onload = init
});