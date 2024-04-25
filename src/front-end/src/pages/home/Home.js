import { useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import classes from './Home.module.css';

function Home(props) {
	const navigate = useNavigate();

	// Takes user to login page if no token is found
	useEffect(() => {
		props.onNameChange(undefined);
		const token = sessionStorage.getItem('Security Token');
		if (token == null || token === 'undefined') {
			navigate('/login');
		}
	});

	// Technically does not log out the user from the back-end
	// Instead, it removes the token needed to allow for back-end interaction.
	function logout() {
		sessionStorage.removeItem('Security Token');
		navigate('/login');
	}

	return (
		<div className={classes.home}>
			<div className={classes.selection}>
				<Link className={classes.link} to="/new-evaluation">
					Take New Prewriting Evaluation
				</Link>
				<Link className={classes.link} to="/records">
					View Existing Evaluations
				</Link>
			</div>
			<Link className={classes.button} to="/home/ReportSearch">
					Report Search
			</Link>	
			<button className={classes.logout} onClick={logout}>
				Log Out
			</button>
		</div>
	);
}

export default Home;
