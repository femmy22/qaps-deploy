// Redraw is repsonsible for redrawing any shapes that are selected from the records page
// The shape that is requested will be displayed on the left side of the page.
// The other side will include how the child drew a shape. It is scaled to fit the screen size appropriately.

import { useEffect, useRef } from 'react';
import { Link, useLocation } from 'react-router-dom';
import classes from '../../styles.module.css';
import Circle from './Circle';
import DoubleLine from './DoubleLine';
import TripleLine from './TripleLine';
import SingleLine from './SingleLine';
import VerticalLine from './VerticalLine';
import Square from './Square';
import MiniVerticalLines from './MiniVerticalLines';
import UnsymmetricalLines from './UnsymmetricalLines';
import PlusSign from './PlusSign';
import Triangle from './Triangle';

function Redraw() {
	const shapeRef = useRef(); // Referring to the actual JSX canvas tag
	const { state } = useLocation(); // this is undefined when coming in; array is coming in in recordtables tho
	const { data } = state;

	// Determine which shape needs to be displayed on the left side of the page.
	function getPerfectShape(shape) {
		switch (shape) {
			case 'Circle':
				return <Circle />;
			case 'Double Line':
				return <DoubleLine />;
			case 'Triple Line':
				return <TripleLine />;
			case 'Square':
				return <Square />;
			case 'Single Line':
				return <SingleLine />;
			case 'Vertical Line':
				return <VerticalLine />;
			case 'Mini Vertical Lines':
				return <MiniVerticalLines />;
			case 'Unsymmetrical Lines':
				return <UnsymmetricalLines />;
			case 'Plus Sign':
				return <PlusSign />;
			case 'Triangle':
				return <Triangle />;
			default:
				return <p>Shape Data Error</p>;
		}
	}

	// Removes brackets from string arrays
	function removeBrackets(stringArray) {
		for (let i = 0; i < stringArray.length; i++) {
			stringArray[i] = stringArray[i].replace('[[', '');
			stringArray[i] = stringArray[i].replace(']]', '');
			stringArray[i] = stringArray[i].replace('[', '');
			stringArray[i] = stringArray[i].replace(']', '');
		}
	}

	// Manual Version of resizeCanvas function
	function reset() {
		const ctx = shapeRef.current.getContext('2d');
		let newWidth = window.innerWidth / 2;
		let newHeight = window.innerHeight;
		ctx.canvas.width = newWidth;
		ctx.canvas.height = newHeight;
		onSubmitRedrawHandler();
	}

	// This is called after 1 second passes once the Redraw component is called
	// This basically functions as the main function of this component.
	// It calls all functions and implements logic to convert the string data from the tables to data that makes up a drawing.
	function onSubmitRedrawHandler() {
		// Grab coordinates and time stamps; these are just large strings that need to be parsed
		let xString = data[0][2];
		let yString = data[0][3];
		let timeString = data[0][4];
		// Remove whitespace
		xString = xString.replace(/\s/g, '');
		yString = yString.replace(/\s/g, '');
		timeString = timeString.replace(/\s/g, '');
		// Split into arrays of strings
		const xStringArray = xString.split('],');
		const yStringArray = yString.split('],');
		const timeStringArray = timeString.split('],');
		// Remove brackets - only integers/floats separated by commas will remain
		removeBrackets(xStringArray);
		removeBrackets(yStringArray);
		removeBrackets(timeStringArray);

		const xMultiStringArray = [];
		const yMultiStringArray = [];
		const timeMultiStringArray = [];
		// Create 2D arrays of strings
		for (let i = 0; i < xStringArray.length; i++) {
			xMultiStringArray.push(xStringArray[i].split(','));
			yMultiStringArray.push(yStringArray[i].split(','));
			timeMultiStringArray.push(timeStringArray[i].split(','));
		}

		// 2D arrays that will hold numerical values
		const xArray = [];
		const yArray = [];
		const timeArray = [];
		// Parse strings into numbers
		for (let i = 0; i < xMultiStringArray.length; i++) {
			const xTemp = [];
			const yTemp = [];
			const timeTemp = [];
			for (let j = 0; j < xMultiStringArray[i].length; j++) {
				xTemp.push(parseFloat(xMultiStringArray[i][j]));
				yTemp.push(parseFloat(yMultiStringArray[i][j]));
				timeTemp.push(parseInt(timeMultiStringArray[i][j]));
			}
			xArray.push(xTemp);
			yArray.push(yTemp);
			timeArray.push(timeTemp);
		}

		const originalDimensionsX = data[0][5]; // Width of the canvas during evaluation
		const originalDimensionsY = data[0][6]; // Height of the canvas during evaluation
		const currentDimensionsX = window.innerWidth / 2; // Width of the current canvas that is replaying a drawing
		const currentDimensionsY = window.innerHeight; // Height of the current canvas that is replaying a drawing

		let xRatio = currentDimensionsX / originalDimensionsX;
		let yRatio = currentDimensionsY / originalDimensionsY;

		// Always look for smallest scale factor
		let scaleFactor;
		if (xRatio > yRatio) {
			scaleFactor = yRatio;
		} else {
			scaleFactor = xRatio;
		}

		// Resize the drawing to be more appropriate with the current screen being viewed
		let highestX = 0;
		let highestY = 0;
		for (let i = 0; i < xArray.length; i++) {
			for (let j = 0; j < xArray[i].length; j++) {
				xArray[i][j] *= scaleFactor;
				yArray[i][j] *= scaleFactor;
				if (xArray[i][j] > highestX) {
					highestX = xArray[i][j];
				}
				if (yArray[i][j] > highestY) {
					highestY = yArray[i][j];
				}
			}
		}

		// Shift the shape based on the scale factor above towards the center of the canvas
		for (let i = 0; i < xArray.length; i++) {
			for (let j = 0; j < xArray[i].length; j++) {
				xArray[i][j] += (currentDimensionsX - highestX) / 4;
				yArray[i][j] += (currentDimensionsY - highestY) / 4;
			}
		}

		const initialTime = timeArray[0][0]; // Record of when the drawing first started
		// Sets timestamps to be based off how much time has passed since drawings started
		for (let i = 0; i < timeArray.length; i++) {
			for (let j = 1; j < timeArray[i].length; j++) {
				timeArray[i][j] = timeArray[i][j] - initialTime;
			}
		}

		// Recreates drawing
		const ctx = shapeRef.current.getContext('2d');
		for (let i = 0; i < xArray.length; i++) {
			ctx.beginPath();
			ctx.lineWidth = 4;
			for (let j = 0; j < xArray[i].length - 1; j++) {
				setTimeout(() => {
					ctx.moveTo(xArray[i][j], yArray[i][j]);
					ctx.lineTo(xArray[i][j + 1], yArray[i][j + 1]);
					ctx.stroke();
				}, timeArray[i][j]);
			}
		}
	}

	// After one second passes, redraw the chosen shape appropriate to the screen size.
	useEffect(() => {
		const ctx = shapeRef.current.getContext('2d');

		/**
		 * Resizes the canvas and clears stored x and y coordinates
		 * if the window is resized.
		 */
		function resizeCanvas() {
			let newWidth = window.innerWidth / 2;
			let newHeight = window.innerHeight;
			ctx.canvas.width = newWidth;
			ctx.canvas.height = newHeight;
		}

		resizeCanvas();
		setTimeout(onSubmitRedrawHandler, 1000);
	});

	return (
		<div className={classes.testingTemplate}>
			<div className={classes.postionAbsolute}>
				<Link className={classes.button} to="/records">
					Go Back
				</Link>
				<button className={classes.button} onClick={reset}>
					Reset
				</button>
			</div>
			{getPerfectShape(data[0][1])}
			<canvas ref={shapeRef} />
		</div>
	);
}

export default Redraw;
