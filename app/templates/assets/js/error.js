function getCookie(name) {
	let value = `; ${document.cookie}`;
	console.log(value);
	let parts = value.split(`; ${name}=`);
	if (parts.length === 2) return parts.pop().split(';').shift();
}

function showErrorMessage() {
	let error_type = getCookie('error-message')
	let error_info = error_type.split('_')
	
	document.getElementById('replace').innerHTML = `Error ${error_info[0]}:<br>${error_info[1]}`
	
	let redirect_login = ['This email is already registered. Please login or register a different email.', 'Incorrect password, please try again.']

	if (redirect_login.includes(error_info[1])) {
		document.getElementById('try_again').href = '/login.html'
	} else {
		document.getElementById('try_again').href = '/register.html'
	}

}

window.onload = showErrorMessage()