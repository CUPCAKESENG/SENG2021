function logout() {
	document.cookie = 'token=; path=/;'
	window.location.href = '/login.html'
}

function init() {
}

document.addEventListener("DOMContentLoaded", () => {  
	window.onload = init
});