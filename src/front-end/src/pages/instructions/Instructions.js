import { Link, useNavigate } from 'react-router-dom';
import { useRef } from 'react';
import classes from './Instructions.module.css';
import Modal from '../../components/modal/Modal';



function Instructions(props) {
	const navigate = useNavigate();
	const dominantHandRef = useRef(false);
	const currentDate = new Date();

	// Uses Date/Time for session ID
	const month = currentDate.getMonth() + 1; // getMonth() starts at 0 for January; adding 1 for this reason
	const day = currentDate.getDate();
	const year = currentDate.getFullYear();
	const hour = currentDate.getHours();
	const minute = currentDate.getMinutes();
	const second = currentDate.getSeconds();

	const testSessionId = `${month}:${day}:${year}:${hour}:${minute}:${second}`; // Generate unique ID

	// Updates the child name that will be shared in every test
	function submitHandler(event) {
		event.preventDefault();
		props.onHandChange(dominantHandRef.current.checked);
		props.onNameChange(testSessionId); // Save student name alongside test session ID
		navigate('/new-evaluation/circle'); // Navigate to the first shape test
	}

	return (
		<div className={classes.instructions}>
			<Modal>
				<p>
					Drawing is done on the blank side. Press the "Enter" key to continue
					to next shape. Press the "R" key to reset the current drawing. Please
					do not refresh the page or go back to previous shapes after submitting
					them.
				</p>
				<label htmlFor="dominantHand" aria-label="Left Handed">
					<input type="checkbox" id="dominantHand" ref={dominantHandRef} />
					Left Handed
				</label>
				<form className={classes.form} onSubmit={submitHandler}>
					<span className={classes.idPrompt}>
						Be sure to keep track of this ID with the child!
					</span>
					<span className={classes.id}>{testSessionId}</span>
					<button className={classes.begin}>Begin Test</button>
				</form>    
				<Link className={classes.link} to="/">
					<p>Return to Homepage</p>
				</Link>    
			</Modal>    
		</div>
	);
}	

export default Instructions;
