// Serves as the page that will display any previously created records

import { useRef, useState, useContext, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { RecordStorage } from '../../App';
import Dropdown from 'react-dropdown';
import 'react-dropdown/style.css';
import Modal from '../../components/modal/Modal';
import RecordTable from './RecordTable';
import classes from './Records.module.css';

function Records(props) {
	const tableInputRef = useRef();
	const sessionIdInputRef = useRef();
	const storage = useContext(RecordStorage);
	const [tableRender, updateTableRender] = useState(false);
	const [dataDisplay, updateDataDisplay] = useState();
	const tableOptions = ['score', 'test', 'rawData', 'measurement', 'difference']; // All tables that we want to allow access to
	const defaultTable = tableOptions[0];

	// Updates the record table component that goes in this component based off the selected column header based off how it was sorted
	const sortDataHandler = (sortedData) => {
		props.storeRecords(sortedData); // Tells React to keep track of the most recent record table state for instant table loading.
		updateDataDisplay(sortedData);
	};

	// Get the table the user requested
	function submitHandler(event) {
		event.preventDefault();

		let enteredTable = tableInputRef.current.state.selected.value;
		if (enteredTable === undefined) {
			enteredTable = tableInputRef.current.props.value;
		}
		let enteredSessionId = sessionIdInputRef.current.value;

		const dataBaseQuery = {
		table: enteredTable,
		shape: 'Any',
		session: enteredSessionId,
		};
		const token = sessionStorage.getItem('Security Token');
		const testSessionData = {session: enteredSessionId };

		if (enteredTable === 'difference') {
			if (!enteredSessionId) {
				// You can add validation here to require a session ID when 'difference' is selected
				alert('Session ID is required for the "difference" table.');
				return;
			} 
			else {
				//const URL = 'http://localhost:5000/difference';
				const URL = 'http://ec2-34-224-180-254.compute-1.amazonaws.com/api/difference';  // AWS server
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
				.then((data) => {
					data.table = enteredTable;

					const dataObject = {
						table: data.table,
						records: data,
					};
					props.storeRecords(dataObject);
					updateDataDisplay(dataObject);
					updateTableRender(true);
				});
			}
			
		} else {
			// Sending POST request to URL
			//const URL = 'http://localhost:5000/get-data';
			const URL = 'http://ec2-34-224-180-254.compute-1.amazonaws.com/api/new-data';  // AWS server
	
			fetch(URL, {
				method: 'POST',
				headers: {
					Accept: 'application/json',
					'Content-Type': 'application/json',
					Authorization: `Bearer ${token}`,
				},
				body: JSON.stringify(dataBaseQuery),
			})
				.then((response) => response.json())
				.then((data) => {
					data.table = enteredTable;
					// Removing -1s from table; changing them to 0s
					for (let i = 0; i < data.length; i++) {
						for (let j = 1; j < data[i].length; j++) {
							if (data[i][j] < 0) {
								data[i][j] = 0;
								if (data.table === 'score') data[i][10] += 1;
							}
						}
					}
	
					const dataObject = {
						table: data.table,
						records: data,
					};
					props.storeRecords(dataObject);
					updateDataDisplay(dataObject);
					updateTableRender(true);
				});
		}
	}

	// 	let enteredSessionId = sessionIdInputRef.current.value;

	// 	const dataBaseQuery = {
	// 		table: enteredTable,
	// 		shape: 'Any',
	// 		session: enteredSessionId,
	// 	};
	// 	const token = sessionStorage.getItem('Security Token');

	// 	// Sending POST request to URL
	// 	const URL = 'http://localhost:5000/get-data';
	// 	// 	const URL = 'http://3.238.55.170:5000/get-data';  // AWS server

	// 	fetch(URL, {
	// 		method: 'POST',
	// 		headers: {
	// 			Accept: 'application/json',
	// 			'Content-Type': 'application/json',
	// 			Authorization: `Bearer ${token}`,
	// 		},
	// 		body: JSON.stringify(dataBaseQuery),
	// 	})
	// 		.then((response) => response.json())
	// 		.then((data) => {
	// 			data.table = enteredTable;
	// 			// Removing -1s from table; changing them to 0s
	// 			for (let i = 0; i < data.length; i++) {
	// 				for (let j = 1; j < data[i].length; j++) {
	// 					if (data[i][j] < 0) {
	// 						data[i][j] = 0;
	// 						if (data.table === 'score') data[i][10] += 1;
	// 					}
	// 				}
	// 			}

	// 			const dataObject = {
	// 				table: data.table,
	// 				records: data,
	// 			};
	// 			props.storeRecords(dataObject);
	// 			updateDataDisplay(dataObject);
	// 			updateTableRender(true);
	// 		});
	// }

	// Display previously searched table if not first time searching in the current session.
	useEffect(() => {
		if (storage.records !== undefined) {
			if (dataDisplay === undefined) {
				updateDataDisplay(storage.records);
			} else {
				updateDataDisplay(dataDisplay);
			}
			updateTableRender(true);
		}
	}, [storage, dataDisplay]);

	/**
	 * The basic layout of the JSX below:
	 * Return to homepage
	 * Choose table
	 * Specify session ID if desired (recommended; LOT of data if not specified)
	 * Get table specified
	 * <The Record Table> - This is its own component which will be explained in its file.
	 */
	return (
		<Modal>
			{tableRender ? (
				<form className={classes.withTable} onSubmit={submitHandler}>
					<Link className={classes.link} to="/">
						Return to Homepage
					</Link>
					<div>
						<label htmlFor="table">Choose a Table</label>
						<Dropdown
							id="table"
							options={tableOptions}
							value={defaultTable}
							ref={tableInputRef}
						/>
						<div className={classes.formElements}>
							<label htmlFor="sessionID">Session ID</label>
							<input
								id="sessionID"
								type="text"
								placeholder="(Optional)"
								ref={sessionIdInputRef}
							/>
						</div>
					</div>
					<button className={classes.search}>Search Data</button>
				</form>
			) : (
				<form className={classes.withoutTable} onSubmit={submitHandler}>
					<Link className={classes.link} to="/">
						Return to Homepage
					</Link>
					<div className={classes.formElements}>
						<label htmlFor="table">Choose a Table</label>
						<Dropdown
							id="table"
							options={tableOptions}
							value={defaultTable}
							ref={tableInputRef}
						/>
					</div>
					<div className={classes.formElements}>
						<label htmlFor="sessionID">Session ID</label>
						<input
							id="sessionID"
							type="text"
							placeholder="(Optional)"
							ref={sessionIdInputRef}
						/>
					</div>
					<button className={classes.search}>Search Data</button>
				</form>
			)}

			{tableRender ? (
				<RecordTable data={dataDisplay} onDataSort={sortDataHandler} />
			) : null}
		</Modal>
	);
}

export default Records;
