// First component needed to interact with back-end.
// If not logged in, back-end will not interact with front-end.
// Additionally, front-end will break.

import { useRef, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import classes from './Login.module.css';
import Modal from '../../components/modal/Modal';

function Login() {
	const navigate = useNavigate();
	const usernameRef = useRef();
	const passwordRef = useRef();
	let [invalidCredentials, invalidConfirmed] = useState();

	// Initiates the login once credentials are submitted
	function loginSubmissionHandler(event) {
		event.preventDefault();
		const enteredUsername = usernameRef.current.value;
		const enteredPassword = passwordRef.current.value;
		const loginCredentials = {
			username: enteredUsername,
			password: enteredPassword,
		};

		const URL = 'http://localhost:5000/login';
		// 	const URL = 'http://3.238.55.170:5000/login';  // AWS server
		fetch(URL, {
			method: 'POST',
			body: JSON.stringify(loginCredentials),
			headers: {
				Accept: 'application/json',
				'Content-Type': 'application/json',
			},
		})
			.then((response) => {
				if (response.status === 200) {
					response.json().then((data) => {
						const { token } = data;
						sessionStorage.setItem('Security Token', token);
						navigate('/');
					});
				} else {
					invalidConfirmed('Invalid username/password');
				}
			})
			.catch((error) => {
				console.log(error);
			});
	}

	return (
	
		<Modal>
			<h2>Please Enter Credentials</h2>
			<form className={classes.credentials} onSubmit={loginSubmissionHandler}>
				<span className={classes.inputField}>
					<label htmlFor="username">UserName</label>
					<input id="username" type="text" required ref={usernameRef} />
				</span>
				<span className={classes.inputField}>
					<label htmlFor="password">Password</label>
					<input id="password" type="password" required ref={passwordRef} />
				</span>
				{/* 'Invalid credentials' message to appear when appropriate */}
				<p>{invalidCredentials}</p>
				<button className={classes.login}>Login</button>
			</form>
		</Modal>
			 

	);
}

export default Login;
