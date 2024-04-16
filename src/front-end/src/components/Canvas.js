/**
 * The Canvas Component will be used for every shape
 * This component will be used for taking user input
 */

import { useEffect, useRef } from 'react';

// These will be arrays of arrays
const xCoordinates = [];
const yCoordinates = [];
const timeStamp = [];

// These are the arrays that go in the arrays listed above
// They will reset when the pointerup event occurs
const xStroke = [];
const yStroke = [];
const timeStroke = [];

// drawingData contains all x and y coordinates as well as timestamp for each point in the drawing
// These will be in all shapes; no test declared yet
const drawingData = {
	xCoordinates: xCoordinates,
	yCoordinates: yCoordinates,
	timeStamp: timeStamp,
};

function Canvas(props) {
	const canvasRef = useRef(); // Referring to this component's JSX

	// useEffect occurs when an instance of the component is loaded
	useEffect(() => {
		let firstLoad = true;
		const currentCanvas = canvasRef.current;
		const ctx = currentCanvas.getContext('2d');
		let painting = false;

		/**
		 * Resizes the canvas and clears stored x and y coordinates
		 * if the window is resized.
		 */
		function resizeCanvas() {
			let newWidth = window.innerWidth / 2;
			let newHeight = window.innerHeight;
			currentCanvas.width = newWidth;
			currentCanvas.height = newHeight;
			xCoordinates.length = 0;
			yCoordinates.length = 0;
			timeStamp.length = 0;
		}

		/**
		 * Start drawing when touching screen or mouse clicked down
		 * @param {*} event refers to the 'event' that occurred
		 * In this case, the event is the pointerdown event.
		 */
		function startPosition(event) {
			// For some reason, resizing needs to be done after initial loading.
			// This is a clever way to make sure resizing is done before drawing.
			// That being said, this is a bit of a hack.
			if (firstLoad) {
				resizeCanvas();
				firstLoad = false;
			}
			painting = true;
			draw(event);
		}

		/**
		 * Stop drawing when no longer touching or mouse is no longer clicked down
		 */
		function finishedPosition() {
			painting = false;
			ctx.beginPath();
			xCoordinates.push(xStroke.slice());
			yCoordinates.push(yStroke.slice());
			timeStamp.push(timeStroke.slice());
			xStroke.length = 0;
			yStroke.length = 0;
			timeStroke.length = 0;
		}

		/**
		 * Does the actual drawing on the canvas element
		 * @param {*} event refers to the 'event' that occurred
		 * In this case, the event is usually the pointermove event.
		 * @returns when drawing is stopped
		 */
		function draw(event) {
			if (!painting) return;
			ctx.lineWidth = 4;
			const X = event.offsetX;
			const Y = event.offsetY;
			ctx.lineTo(X, Y);
			ctx.stroke();
			ctx.beginPath();
			ctx.moveTo(X, Y);
			makeArray(X, Y);
		}

		/**
		 * Stores all x and y coordinates of our drawing, relative to the canvas origin
		 * @param {*} x the x coordinate of a given pixel that was drawn
		 * @param {*} y the y coordiante of a given pixel that was drawn
		 */
		function makeArray(x, y) {
			let time = Date.now();
			xStroke.push(x);
			yStroke.push(y);
			timeStroke.push(time);
		}

		/**
		 * Send JSON to back-end and recieve a score on the given test.
		 * Although we are sending score back to front-end, we don't want to display beyond the demo.
		 */
		async function showResults(event) {
			switch (event.code) {
				case 'Enter':
					if (drawingData.xCoordinates.length === 0) return;
					currentCanvas.removeEventListener('pointermove', draw);
					currentCanvas.removeEventListener('pointerdown', startPosition);
					currentCanvas.removeEventListener('pointerup', finishedPosition);
					window.removeEventListener('resize', resizeCanvas);
					window.removeEventListener('keydown', showResults);
					const drawingDataSubmission = JSON.parse(JSON.stringify(drawingData)); // Used to prevent potential race condition
					let result = await props.onSubmit(drawingDataSubmission); // Send drawing data to the parent component (Circle, DoubleLine, or etc.)
					// Give control back to user if there was an error
					if (result === 'Error') {
						currentCanvas.addEventListener('pointermove', draw);
						currentCanvas.addEventListener('pointerdown', startPosition);
						currentCanvas.addEventListener('pointerup', finishedPosition);
						window.addEventListener('keydown', showResults);
						window.addEventListener('resize', resizeCanvas);
					}
					break;
				case 'KeyR':
					resizeCanvas();
					break;
				default:
					break;
			}
		}

		// Adding event listeners that enable drawing on our canvas
		currentCanvas.addEventListener('pointermove', draw);
		currentCanvas.addEventListener('pointerdown', startPosition);
		currentCanvas.addEventListener('pointerup', finishedPosition);
		window.addEventListener('keydown', showResults);
		window.addEventListener('resize', resizeCanvas);
		resizeCanvas();

		// Remove event listeners when component cleans up
		return () => {
			currentCanvas.removeEventListener('pointermove', draw);
			currentCanvas.removeEventListener('pointerdown', startPosition);
			currentCanvas.removeEventListener('pointerup', finishedPosition);
			window.removeEventListener('keydown', showResults);
			window.removeEventListener('resize', resizeCanvas);
		};
	});

	return <canvas ref={canvasRef} />;
}

export default Canvas;
