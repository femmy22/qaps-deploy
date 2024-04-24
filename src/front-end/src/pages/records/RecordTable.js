// Makes up the largest portion of the records page.
// Made as a separate component due to large amount of content

import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import classes from './Records.module.css';

function RecordTable(props) {
	const { data, onDataSort } = props;
	const [noRecords, noRecordsConfirmed] = useState(null);
	const [lastToggle, updateToggle] = useState(null); // Keeps track of which column was sorted last
	const navigate = useNavigate();

	// Navigates to the Redraw component based on the shape that was selected from the table
	// This can not be done through the score table as there are no individual shapes in that table
	const viewRecord = (sessionId, shape) => async () => {
		const shapeData = {
			table: 'rawData',
			shape: shape,
			session: sessionId,
		};

		const token = sessionStorage.getItem('Security Token');
		// Sending POST request to URL
		//const URL = 'http://localhost:5000/get-data';
		const URL = 'http://ec2-34-224-180-254.compute-1.amazonaws.com/api/get-data';  // AWS server

		// Ask back-end for raw data based on the shape and session ID
		const response = await fetch(URL, {
			method: 'POST',
			headers: {
				Accept: 'application/json',
				'Content-Type': 'application/json',
				Authorization: `Bearer ${token}`,
			},
			body: JSON.stringify(shapeData),
		});

		const rawData = await response.json();

		// Navigate to redrawing page with props of the returned
		navigate('/redraw', { state: { data: rawData } });
	};

	// onClick function for sorting score table
	const sortByHeader = (header) => {
		let index = 1;
		let isNumber = true;
		switch (header) {
			case 'Session ID':
				index = 0;
				isNumber = false;
				break;
			case 'Total Score':
				index = 10;
				break;
			case 'Straightness':
				index = 1;
				break;
			case 'Equilaterality':
				index = 2;
				break;
			case 'Alignment':
				index = 3;
				break;
			case 'Roundness':
				index = 4;
				break;
			case 'Closure':
				index = 5;
				break;
			case 'Spacing':
				index = 6;
				break;
			case 'Line Ratio':
				index = 7;
				break;
			case 'Bisection':
				index = 8;
				break;
			case 'Bisection Angle':
				index = 9;
				break;
			case 'Score':
				index = 3;
				break;
			case 'Shape':
				index = 1;
				isNumber = false;
				break;
			case 'Dimension':
				index = 2;
				isNumber = false;
				break;
			case 'Width':
				index = 5;
				break;
			case 'Height':
				index = 6;
				break;
			default:
				console.log('No Column chosen: ' + header);
		}

		const dataCopy = [...data.records]; // Make copy of the current table data

		// Toggle logic swaps greatest-least and least-greatest sorting when selecting any specific column consecutively
		if (lastToggle === header) {
			if (isNumber) {
				dataCopy.sort((a, b) => a[index] - b[index]); // Sorts numbers
			} else {
				dataCopy.sort((a, b) => b[index].localeCompare(a[index])); // Sorts strings
			}
			updateToggle(null);
		} else {
			if (isNumber) {
				dataCopy.sort((a, b) => b[index] - a[index]); // Sorts numbers
			} else {
				dataCopy.sort((a, b) => a[index].localeCompare(b[index])); // Sorts strings
			}
			updateToggle(header);
		}

		const dataObject = {
			table: data.table,
			records: dataCopy,
		};
		onDataSort(dataObject); // Tell the record page to re-render the recordtable now that the data has been sorted.
	};

	/**
	 * Don't show anything if no search was made yet
	 * Otherwise, each of the sections that check for "data.table === '<score/test/rawData/measurement>'" do the same thing but for their respective table.
	 * Basically they make a table, makes sure column headers are clickable if column is sortable (all columns except some columns in rawData).
	 * Rows are populated with whatever the back-end returns from the database query based on the parameters selected Records.js.
	 * The .maps() method maps out each single piece of data to the correct column of each row.
	 * Excluding the score table, each row is clickable which will take the user to the redraw page for their chosen shape to be redrawn.
	 */
	if (data.length !== 0) {
		// If grabbing from the score table
		if (data.table === 'score') {
			// score table display
			return (
				<div className={classes.limitY}>
					<div className={classes.limitX}>
						<table>
							<thead>
								<tr>
									<th
										className={classes.clickableRecord}
										onClick={() => sortByHeader('Session ID')}
									>
										Session ID
									</th>
									<th
										className={classes.clickableRecord}
										onClick={() => sortByHeader('Total Score')}
									>
										Total Score
									</th>
									<th
										className={classes.clickableRecord}
										onClick={() => sortByHeader('Straightness')}
									>
										Straightness
									</th>
									<th
										className={classes.clickableRecord}
										onClick={() => sortByHeader('Equilaterality')}
									>
										Equilaterality
									</th>
									<th
										className={classes.clickableRecord}
										onClick={() => sortByHeader('Alignment')}
									>
										Alignment
									</th>
									<th
										className={classes.clickableRecord}
										onClick={() => sortByHeader('Roundness')}
									>
										Roundness
									</th>
									<th
										className={classes.clickableRecord}
										onClick={() => sortByHeader('Closure')}
									>
										Closure
									</th>
									<th
										className={classes.clickableRecord}
										onClick={() => sortByHeader('Spacing')}
									>
										Spacing
									</th>
									<th
										className={classes.clickableRecord}
										onClick={() => sortByHeader('Line Ratio')}
									>
										Line Ratio
									</th>
									<th
										className={classes.clickableRecord}
										onClick={() => sortByHeader('Bisection')}
									>
										Bisection
									</th>
									<th
										className={classes.clickableRecord}
										onClick={() => sortByHeader('Bisection Angle')}
									>
										Bisection Angle
									</th>
								</tr>
							</thead>
							<tbody>
								{data.records?.map((row, i) => {
									// Formatting into percentages
									const sessionId = row[0];
									const score = (row[10] * 1).toFixed(2);
									const straightness = (row[1] * 1).toFixed(2);
									const equilaterality = (row[2] * 1).toFixed(2);
									const alignment = (row[3] * 1).toFixed(2);
									const roundness = (row[4] * 1).toFixed(2);
									const closure = (row[5] * 1).toFixed(2);
									const spacing = (row[6] * 1).toFixed(2);
									const lineRatio = (row[7] * 1).toFixed(2);
									const bisection = (row[8] * 1).toFixed(2);
									const bisectionAngle = (row[9] * 1).toFixed(2);
									return (
										<tr key={i}>
											<td>{sessionId}</td>
											<td>{score}</td>
											<td>{straightness}</td>
											<td>{equilaterality}</td>
											<td>{alignment}</td>
											<td>{roundness}</td>
											<td>{closure}</td>
											<td>{spacing}</td>
											<td>{lineRatio}</td>
											<td>{bisection}</td>
											<td>{bisectionAngle}</td>
										</tr>
									);
								})}
							</tbody>
						</table>
					</div>
				</div>
			);
		}
		// If grabbing from the test table
		else if (data.table === 'test') {
			// test table display
			return (
				<div className={classes.limitY}>
					<div className={classes.limitX}>
						<table>
							<thead>
								<tr>
									<th
										className={classes.clickableRecord}
										onClick={() => sortByHeader('Session ID')}
									>
										Session ID
									</th>
									<th
										className={classes.clickableRecord}
										onClick={() => sortByHeader('Shape')}
									>
										Shape
									</th>
									<th
										className={classes.clickableRecord}
										onClick={() => sortByHeader('Dimension')}
									>
										Dimension
									</th>
									<th
										className={classes.clickableRecord}
										onClick={() => sortByHeader('Score')}
									>
										Score
									</th>
								</tr>
							</thead>
							<tbody>
								{data.records?.map((row, i) => {
									const sessionId = row[0];
									const shape = row[1];
									const dimension = row[2];
									const score = (row[3] * 1).toFixed(2).toString();
									return (
										<tr
											className={classes.clickableRecord}
											onClick={viewRecord(sessionId, shape)}
											key={i}
										>
											<td>{sessionId}</td>
											<td>{shape}</td>
											<td>{dimension}</td>
											<td>{score}</td>
										</tr>
									);
								})}
							</tbody>
						</table>
					</div>
				</div>
			);
		}
		// If grabbing from the rawData table
		else if (data.table === 'rawData') {
			// rawData table display - Very ugly table without session ID specified
			return (
				<div className={classes.limitY}>
					<div className={classes.limitX}>
						<table>
							<thead>
								<tr>
									<th
										className={classes.clickableRecord}
										onClick={() => sortByHeader('Session ID')}
									>
										Session ID
									</th>
									<th
										className={classes.clickableRecord}
										onClick={() => sortByHeader('Shape')}
									>
										Shape
									</th>
									<th>X Coordinates</th>
									<th>Y Coordinates</th>
									<th>Time Stamps</th>
									<th
										className={classes.clickableRecord}
										onClick={() => sortByHeader('Width')}
									>
										Canvas Pixel Width
									</th>

									<th
										className={classes.clickableRecord}
										onClick={() => sortByHeader('Height')}
									>
										Canvas Pixel Height
									</th>
								</tr>
							</thead>
							<tbody>
								{data.records?.map((row, i) => {
									return (
										<tr
											className={classes.clickableRecord}
											onClick={viewRecord(row[0], row[1])}
											key={i}
										>
											<td>{row[0]}</td>
											<td>{row[1]}</td>
											<td>{row[2]}</td>
											<td>{row[3]}</td>
											<td>{row[4]}</td>
											<td>{row[5]}</td>
											<td>{row[6]}</td>
										</tr>
									);
								})}
							</tbody>
						</table>
					</div>
				</div>
			);
		} else if (data.table === 'measurement') {
			// measurement table display
			return (
				<div className={classes.limitY}>
					<div className={classes.limitX}>
						<table>
							<thead>
								<tr>
									<th
										className={classes.clickableRecord}
										onClick={() => sortByHeader('Session ID')}
									>
										Session ID
									</th>
									<th
										className={classes.clickableRecord}
										onClick={() => sortByHeader('Shape')}
									>
										Shape
									</th>
									<th
										className={classes.clickableRecord}
										onClick={() => sortByHeader('Dimension')}
									>
										Dimension
									</th>
									<th
										className={classes.clickableRecord}
										onClick={() => sortByHeader('Score')}
									>
										Score
									</th>
								</tr>
							</thead>
							<tbody>
								{data.records?.map((row, i) => {
									const score = (row[3] * 1).toFixed(2);
									return (
										<tr
											className={classes.clickableRecord}
											onClick={viewRecord(row[0], row[1])}
											key={i}
										>
											<td>{row[0]}</td>
											<td>{row[1]}</td>
											<td>{row[2]}</td>
											<td>{score}</td>
										</tr>
									);
								})}
							</tbody>
						</table>
					</div>
				</div>
			);
		}
		else if (data.table === 'difference') {
			// difference table display
			return (
				<div>
					<div className={classes.limitY}>
						<div className={classes.limitX}>
							<table>
								<thead>
									<tr>
										<th className={classes.clickableRecord} onClick={() => sortByHeader('Session ID')}>Session ID</th>
										<th className={classes.clickableRecord} onClick={() => sortByHeader('Total Score Z Score')}>Total Score Z Score</th>
										<th className={classes.clickableRecord} onClick={() => sortByHeader('Z Score Straightness')}>Z Score Straightness</th>
										<th className={classes.clickableRecord} onClick={() => sortByHeader('Z Score Equilaterality')}>Z Score Equilaterality</th>
										<th className={classes.clickableRecord} onClick={() => sortByHeader('Z Score Alignment')}>Z Score Alignment</th>
										<th className={classes.clickableRecord} onClick={() => sortByHeader('Z Score Roundness')}>Z Score Roundness</th>
										<th className={classes.clickableRecord} onClick={() => sortByHeader('Z Score Closure')}>Z Score Closure</th>
										<th className={classes.clickableRecord} onClick={() => sortByHeader('Z Score Spacing')}>Z Score Spacing</th>
										<th className={classes.clickableRecord} onClick={() => sortByHeader('Z Score Line Ratio')}>Z Score Line Ratio</th>
										<th className={classes.clickableRecord} onClick={() => sortByHeader('Z Score Bisection')}>Z Score Bisection</th>
										<th className={classes.clickableRecord} onClick={() => sortByHeader('Z Score Bisection Angle')}>Z Score Bisection Angle</th>
									</tr>
								</thead>
								<tbody>
									{data.records?.map((row, i) => (
										<tr key={i}>
											<td>{row[0]}</td>
											<td>{(row[10] * 1).toFixed(2)}</td>
											<td>{(row[1] * 1).toFixed(2)}</td>
											<td>{(row[2] * 1).toFixed(2)}</td>
											<td>{(row[3] * 1).toFixed(2)}</td>
											<td>{(row[4] * 1).toFixed(2)}</td>
											<td>{(row[5] * 1).toFixed(2)}</td>
											<td>{(row[6] * 1).toFixed(2)}</td>
											<td>{(row[7] * 1).toFixed(2)}</td>
											<td>{(row[8] * 1).toFixed(2)}</td>
											<td>{(row[9] * 1).toFixed(2)}</td>
										</tr>
									))}
								</tbody>
							</table>
						</div>
					</div>
				</div>
			);
		}
		return;
	} else {
		setTimeout(() => {
			noRecordsConfirmed(<h2>No records were found!</h2>);
		}, 3000);
		return noRecords;
	}
	
}
export default RecordTable;