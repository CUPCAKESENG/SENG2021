let recipient = ''
let currency = ''
let amount = ''

function reset() {
	document.getElementById('select-user-text').innerHTML = 'Select'
	document.getElementById('select-currency-text').innerHTML = 'Select'
	document.getElementById('invoice-file').value = ''
	document.querySelector('input[name="amount"]').value = ''
}

function setCurrency() {
	currency = 'AUD'
	document.getElementById('select-currency-text').innerHTML = 'AUD'
}

function setUser(username) {
	recipient = username
	document.getElementById('select-user-text').innerHTML = username
}

function setAmount() {
	amount = document.querySelector('input[name="amount"]').value;
	
	console.log(amount);
}

async function sendInvoice() {
    let token = getCookie('token');
	let output_format = 0
    let formData = new FormData();
    let invoice = document.getElementById("invoice-file").files[0];      
         
    formData.append("invoice", invoice);
    formData.append("token", JSON.stringify(token)); 
	formData.append("output_format", output_format);

    let response = await fetch('/invoice/receive', {
		method: "POST",
		body: formData
	});
	
	if (response.status == 200) {
		console.log('HTTP response code:', response.status); 
	}
}

async function getNames() {
	const response = await fetch(`/user/list?token=${getCookie('token')}`, {
		method: 'GET',
		headers: {'Content-Type': 'application/json'},
	});

	if (response.status == 200) {
		response.json().then(data => {
			users = ''

			for (const username of data.usernames) {
				elem = `<a class="dropdown-item" id="${username}" onclick="setUser(this.id)">${username}</a>\n`
				users += elem
			}

			document.getElementById('select-user').innerHTML = users
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

window.onload = reset
getNames()