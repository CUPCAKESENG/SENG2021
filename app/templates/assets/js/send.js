let recipient = ''
let currency = ''
let amount = ''

function reset() {
	document.getElementById('select-user-text').innerHTML = 'Select'
	document.getElementById('select-currency-text').innerHTML = 'Select'
}

function setCurrency() {
	currency = 'AUD'
	document.getElementById('select-currency-text').innerHTML = 'AUD'
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
				elem = `<a class="dropdown-item" onclick="setUser()">${username}</a>\n`
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