// Component associated with the single horizontal line test.

import { useEffect, useRef, useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import { TestSession, LeftHanded } from '../../App';
import { newData } from './evaluationNavigator';
import Canvas from '../../components/Canvas';
import classes from '../../styles.module.css';

function SingleLine() {
	const navigate = useNavigate();
	const testSession = useContext(TestSession);
	const dominantHand = useContext(LeftHanded);
	const shapeRef = useRef(); // Referring to the actual JSX canvas tag

	// Submit drawing data to be stored into the back-end
	async function onsubmitSingleLineHandler(drawingData) {
		// Adds the test type to the drawing data
		const singleLineData = {
			shape: 'Single Line',
			session: testSession.testSessionId,
			json: {
				x_cords: drawingData.xCoordinates,
				y_cords: drawingData.yCoordinates,
				time_stamps: drawingData.timeStamp,
				canvasDimensionX: window.innerWidth / 2,
				canvasDimensionY: window.innerHeight,
			},
		};
		let navigationLink = await newData(singleLineData);
		if (navigationLink === 'Error') {
			return navigationLink; // Don't continue to next shape if error occurs. This allows the current Canvas component to reactivate.
		}
		navigate(navigationLink); // Go to the next shape.
	}

	// Draw perfect shape when page is loaded or resized
	useEffect(() => {
		const ctx = shapeRef.current.getContext('2d');

		/**
		 * Resizes the canvas and clears stored x and y coordinates
		 * if the window is resized.
		 */
		function resizeShape() {
			let newWidth = window.innerWidth / 2;
			let newHeight = window.innerHeight;
			ctx.canvas.width = newWidth;
			ctx.canvas.height = newHeight;
			ctx.beginPath();
			ctx.lineWidth = 4;
			ctx.moveTo(newWidth / 5, newHeight / 2);
			ctx.lineTo(newWidth * (4 / 5), newHeight / 2);
			ctx.stroke();
		}

		// Event listeners for the Pre-set test shape
		window.addEventListener('resize', resizeShape);
		resizeShape();

		return () => {
			window.removeEventListener('resize', resizeShape);
		};
	});

	// Note that the Canvas components below will not load if there is no testSessionId
	if (dominantHand.leftHanded) {
		return (
			<div className={classes.testingTemplate}>
				{testSession.testSessionId ? (
					<Canvas onSubmit={onsubmitSingleLineHandler} />
				) : null}
				<canvas className={classes.testModel} ref={shapeRef} />
			</div>
		);
	} else {
		return (
			<div className={classes.testingTemplate}>
				<canvas className={classes.testModel} ref={shapeRef} />
				{testSession.testSessionId ? (
					<Canvas onSubmit={onsubmitSingleLineHandler} />
				) : null}
			</div>
		);
	}
}

export default SingleLine;
