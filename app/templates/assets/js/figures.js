const line_chart = new Chart(document.getElementById('revenue-chart'), {
	"type":"line",
	"data": {
		"labels":[],
		"datasets":[{"label":"Earnings","fill":true,"data":[],"backgroundColor":"rgba(78, 115, 223, 0.05)","borderColor":"rgba(78, 115, 223, 1)"}]
		},
	"options": {
		"responsive":true,
		"maintainAspectRatio":false,
		"legend": {"display":false,"labels":{"fontStyle":"normal"}},
		"title": {"fontStyle":"normal"},
		"scales": {"xAxes":[{"gridLines":{"color":"rgb(234, 236, 244)","zeroLineColor":"rgb(234, 236, 244)","drawBorder":false,"drawTicks":false,"borderDash":["2"],"zeroLineBorderDash":["2"],"drawOnChartArea":false},"ticks":{"fontColor":"#858796","fontStyle":"normal","padding":20}}],"yAxes":[{"gridLines":{"color":"rgb(234, 236, 244)","zeroLineColor":"rgb(234, 236, 244)","drawBorder":false,"drawTicks":false,"borderDash":["2"],"zeroLineBorderDash":["2"]},"ticks":{"fontColor":"#858796","fontStyle":"normal","padding":20}}]}
	}
});

const pie_chart = new Chart(document.getElementById('share-chart'), {
	"type":"doughnut",
	"data": {
		"labels":[],
		"datasets":[{
			"label":"",
			"backgroundColor":["#4e73df","#1cc88a","#36b9cc","rgb(218,131,0)"],
			"borderColor":["#ffffff","#ffffff","#ffffff","#ffffff"],
			"data":[]
		}]
	},
	"options":{
		"maintainAspectRatio":false,
		"legend":{"display":true, "position":"bottom","labels":{"fontStyle":"normal"}},"title":{"fontStyle":"normal"}
	}
});

function getDate() {
	var today = new Date();
	var dd = String(today.getDate()).padStart(2, '0');
	var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
	var yyyy = today.getFullYear();

	today = mm + '/' + dd + '/' + yyyy;
	return today
}

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
			let today = 0;
			let total = 0;
			let currency = '';
			let labels = [];
			let values = [];
			let contributors = {}

			for (const invoice of data) {
				total = total + parseFloat(invoice[5])

				if (invoice[2].includes(getDate())) {
					today = today + parseFloat(invoice[5])
				}

				formatted_date = invoice[2].split(',')[0].slice(0,-5) + ' -' + invoice[2].split(',')[1].slice(0,-7)

				labels.push(formatted_date)

				if (values.length === 0) {
					values.push(parseFloat(invoice[5]))
				} else {
					let cumulative = parseFloat(invoice[5]) + values.at(-1);
					values.push(cumulative)
				}
				currency = invoice[4]

				if (invoice[6] in contributors) {
					contributors[invoice[6]] += parseFloat(invoice[5])
				} else {
					contributors[invoice[6]] = parseFloat(invoice[5])
				}
			}

			let pie_labels = []
			let pie_data = []

			for (const [key, value] of Object.entries(contributors)) {
				pie_labels.push(key)
				pie_data.push((value / total).toFixed(2))
			}

			pie_chart.data.labels = pie_labels
			pie_chart.data.datasets[0].data = pie_data

			document.getElementById('earnings-today').innerHTML = `${currency} ${today.toFixed(2)}`
			document.getElementById('earnings-total').innerHTML = `${currency} ${total.toFixed(2)}`
			document.getElementById('total-invoices').innerHTML = data.length;

			line_chart.data.labels = labels
			line_chart.data.datasets[0].data = values
			line_chart.update()
			pie_chart.update()
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
});