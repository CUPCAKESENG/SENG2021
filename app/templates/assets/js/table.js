function refresh() {
	getData()
}

async function getData() {
	const response = await fetch(`/user/graph?token=${getCookie('token')}`, {
		method: 'GET',
		headers: {'Content-Type': 'application/json'},
	});

	if (response.status == 200) {
		response.json().then(data => {
			if (data.length === 0) {
				document.getElementById('no-invoices').classList.remove('d-none')
				return
			}

			let invoice_list = ''

			for (const invoice of data) {
				let complete = `\n<tr>
				<td>
					<img class="rounded-circle me-2" width="30" height="30" src="assets/img/avatars/person.png">
					<a href='/invoice/${invoice[0]}'>${invoice[0]}</a>
				</td>
				<td>${invoice[6]}</td>
				<td>${invoice[1]} bytes</td>
				<td>${invoice[2]}<br></td>
				<td>${invoice[3]}<br></td>
				<td>${invoice[4]} ${invoice[5]}</td>
				</tr>`;

				invoice_list = invoice_list + complete
			}
			
			document.getElementById('invoices').innerHTML = invoice_list

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

document.addEventListener("DOMContentLoaded", () => {  
	window.onload = getData
	setName()
});