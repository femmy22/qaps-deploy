// This file allows each shape to send POST requests to the back-end when taking tests
// calculate is only called on the last test of the evaluation
// newData is called every time a new shape is entered through the front-end

export function calculate(testSessionId) {
	const testSessionData = { session: testSessionId };
	const token = sessionStorage.getItem('Security Token');
	//const URL = 'http://localhost:5000/calculate';
		const URL = 'http://ec2-18-215-156-148.compute-1.amazonaws.com/api/calculate';  // AWS server
	fetch(URL, {
		method: 'POST',
		headers: {
			Accept: 'application/json',
			'Content-Type': 'application/json',
			Authorization: `Bearer ${token}`,
		},
		body: JSON.stringify(testSessionData),
	})
		.then((response) => response.json())
		.catch((error) => {
			console.log(error);
		});
}

export async function newData(shapeData) {
	const token = sessionStorage.getItem('Security Token');
	// Sending POST request to URL
	//const URL = 'http://localhost:5000/new-data';
	 	const URL = 'http://ec2-18-215-156-148.compute-1.amazonaws.com/api/new-data';  // AWS server

	// Send shape data to back-end. Wait to make sure nothing went wrong
	// Makes sure the component that calls this function is informed of any errors
	try {
		const response = await fetch(URL, {
			method: 'POST',
			headers: {
				Accept: 'application/json',
				'Content-Type': 'application/json',
				Authorization: `Bearer ${token}`,
			},
			body: JSON.stringify(shapeData),
		});

		await response.json();
	} catch (error) {
		console.log(error);
		return 'Error';
	}

	// This is where the order of test shapes can be determined
	switch (shapeData.shape) {
		case 'Circle':
			return '/new-evaluation/double-line';
		case 'Double Line':
			return '/new-evaluation/triple-line';
		case 'Triple Line':
			return '/new-evaluation/square';
		case 'Square':
			return '/new-evaluation/single-line';
		case 'Single Line':
			return '/new-evaluation/vertical-line';
		case 'Vertical Line':
			return '/new-evaluation/mini-vertical-lines';
		case 'Mini Vertical Lines':
			return '/new-evaluation/unsymmetrical-lines';
		case 'Unsymmetrical Lines':
			return '/new-evaluation/plus-sign';
		case 'Plus Sign':
			return '/new-evaluation/triangle';
		case 'Triangle': // Make sure the last shape is the only one to calculate
			// calculate(shapeData.session);
			// return '/';
		    return '/report/report';
		default:
			return '/report';
	}
}
