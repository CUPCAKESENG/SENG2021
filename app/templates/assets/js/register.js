let firstName = '';
let lastName = '';
let email = '';
let password = '';
let token = '';

function init() {
	let input_fields = ['first_name', 'last_name', 'email', 'password']

	input_fields.forEach(item => {
		reset(item)
	});	
}

function reset(input_field) {
	document.querySelector(`input[name="${input_field}"]`).value = '';
	if (document.querySelector(`input[name="${input_field}"]`).classList.contains('is_valid')) {
		document.querySelector(`input[name="${input_field}"]`).classList.remove('is_valid')
	}

	if (document.querySelector(`input[name="${input_field}"]`).classList.contains('is_invalid')) {
		document.querySelector(`input[name="${input_field}"]`).classList.remove('is_invalid')
	}

	if (document.querySelector(`input[name="${input_field}"]`).classList.contains('was_validated')) {
		document.querySelector(`input[name="${input_field}"]`).classList.remove('was_validated')
	}
}

function invalidate(input_field) {
	if (document.querySelector(`input[name="${input_field}"]`).classList.contains('is_valid')) {
		document.querySelector(`input[name="${input_field}"]`).classList.remove('is_valid')
	}

	var classes = ['is_invalid', 'was_validated']
	document.querySelector(`input[name="${input_field}"]`).classList.add(...classes)
}

function validate(input_field) {
	var classes = ['is_valid', 'was_validated']
	document.querySelector(`input[name="${input_field}"]`).classList.remove('is_invalid')

	document.querySelector(`input[name="${input_field}"]`).classList.add(...classes)
}

async function register() {
	// fetch('/test')
	// 	.then(function (response) {
	// 		return response.json();
	// 	}).then(function (text) {
	// 		console.log('GET response:');
	// 		console.log(text.message); 
	// 	});

	let input_fields = ['first_name', 'last_name', 'email', 'password']

	all_complete = true

	input_fields.forEach(item_name => {
		item = document.querySelector(`input[name="${item_name}"]`)
		if (item.classList.contains('is_invalid')) {
			all_complete = false;
		}
	});

	if (!all_complete) {
		alert('Please fill out all required fields');
		return
	}

	let registration_details = {
		email: email,
		firstname: firstName,
		lastname: lastName,
		password: password
	} 

	const response = await fetch("/register", {
		method: 'POST',
		headers: {'Content-Type': 'application/json'},
		body: JSON.stringify(registration_details)
	});

	if (response.status == 200) {
		response.json().then(data => {
			console.log(data);
			storeToken(data)
			window.location.href = '/index.html'
		});
	} else {
		let error_code = response.status
		let error_message = ''

		response.text().then(text => {
			const regex_message = /<p>(.+)<\/p>/
			error_message = text.match(regex_message)[1]
						
			console.log(error_message);
			document.cookie = `error-message=${error_code}_${error_message}; path=/; max-age=${60*60}; samesite=strict;`
			window.location.href = '/error.html'
		});
	}
}

function storeToken(data) {
	document.cookie = `token=${data.token}; path=/; max-age=${60 * 60}; samesite=strict;`
	console.log(document.cookie);
}

function getFirstName() {
	firstName = document.querySelector('input[name="first_name"]').value;

	if(firstName == '') {
		invalidate('first_name')
	} else {
		validate('first_name')
		console.log(firstName);
	}
}

function getLastName() {
	lastName = document.querySelector('input[name="last_name"]').value;
	
	if(lastName == '') {
		invalidate('last_name')
	} else {
		validate('last_name')
		console.log(lastName);
	}
}

function getEmail() {
	email = document.querySelector('input[name="email"]').value;

	if(email == '') {
		invalidate('email')
	} else {
		validate('email')
		console.log(email);
	}
}

function getPassword() {
	password = document.querySelector('input[name="password"]').value;

	if(password == '') {
		invalidate('password')
	} else {
		validate('password')
		console.log(password);
	}
}

document.addEventListener("DOMContentLoaded", () => {  
	window.onload = init
});