// Component associated with the circle test.

// Component associated with the circle test.

import { useEffect, useRef, useContext, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { TestSession, LeftHanded } from '../../App';
import { newData } from './evaluationNavigator';
import Canvas from '../../components/Canvas';
import classes from '../../styles.module.css';

function Circle() {
    const navigate = useNavigate();
    const testSession = useContext(TestSession);
    const dominantHand = useContext(LeftHanded);
    const shapeRef = useRef(); // Referring to the actual JSX canvas tag
const [showFirstButton, setShowFirstButton] = useState(true);
    const [showSecondButton, setShowSecondButton] = useState(false);

    const handleFirstButtonClick = () => {
        setShowFirstButton(false);
    }
    const handleScndButtonClick = () => {
        setShowSecondButton(false);
    }
    const buttonStyle = {
        padding: '10px', 
        fontSize: '16px', 
        textAlign: 'center', 
        boxSizing: 'border-box',

    };

    useEffect(() => {
        const timer1 = setTimeout(() => setShowFirstButton(true), 1000); 
        const timer2 = setTimeout(() => setShowSecondButton(true), 5000); 
        // Clear the timers when the component unmounts
        return () => {
            clearTimeout(timer1);
            clearTimeout(timer2);
        };
    }, []);
    // Submit drawing data to be stored into the back-end
    async function onsubmitCircleHandler(drawingData) {
        // Adds the test type to the drawing data
        const circleData = {
            shape: 'Circle',
            session: testSession.testSessionId,
            json: {
                x_cords: drawingData.xCoordinates,
                y_cords: drawingData.yCoordinates,
                time_stamps: drawingData.timeStamp,
                canvasDimensionX: window.innerWidth / 2,
                canvasDimensionY: window.innerHeight,
            },
        };
        let navigationLink = await newData(circleData); // Send data to evaluationNavigator. Get link for next shape back.
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
            ctx.arc(newWidth / 2, newHeight / 2, newWidth / 3, 0, 2 * Math.PI);
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
                    {showFirstButton && (
                    <button style={buttonStyle}>
                        Draw the Shape
                    </button>
                )}
                {showSecondButton && (
                    <button
                        style={buttonStyle}
                    >
                        Hit R or Enter
                    </button>
                )}
                {testSession.testSessionId ? (
                    <Canvas onSubmit={onsubmitCircleHandler} />
                ) : null}
                <canvas className={classes.testModel} ref={shapeRef} />
            </div>
        );
    } else {
        return (
            <div className={classes.testingTemplate}>
                <canvas className={classes.testModel} ref={shapeRef} />
{showFirstButton && (
                    <button style={buttonStyle} onClick={handleFirstButtonClick}>
                        Draw the Shape
                    </button>
                )}
                {showSecondButton && (
                    <button style={buttonStyle} onClick={handleScndButtonClick}>
                        Hit R to restart
                    </button>
                )}

                {testSession.testSessionId ? (
                    <Canvas onSubmit={onsubmitCircleHandler} />
                ) : null}
            </div>
        );
    }
}

export default Circle;
