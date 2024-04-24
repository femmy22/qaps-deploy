import { useEffect, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import classes from './Home.module.css';

function Home(props) {
    const [showPopup, setShowPopup] = useState(true);
    const navigate = useNavigate();

// Takes user to login page if no token is found
    useEffect(() => {
        props.onNameChange(undefined);
        const token = sessionStorage.getItem('Security Token');
        if (token == null || token === 'undefined' || token.trim() === '') {
            navigate('/login');
        }
    }, []); // Added empty dependency array to run only on mount

// Technically does not log out the user from the back-end
    // Instead, it removes the token needed to allow for back-end interaction.
    function logout() {
        sessionStorage.removeItem('Security Token');
        navigate('/login');
    }
    
    function togglePopup(){
        setShowPopup(false);
    }
    
    return (
        <div>
            <div className={classes.popup-1}>
                {showPopup && (
                    <h1 className={classes.popup}>
                        Welcome to our Prewriting App! <br />
                        Would you like a tour?
                        <div className={classes.button}>
                            <a href='http://www.qapsapp.com/new-evaluation' className={`${classes.btn} ${classes.btnYes}`}>Yes</a>
                            <button className={classes.btnNo} onClick={togglePopup}>No</button>
                        </div>
                    </h1>
                )}
            </div>
            <div className={classes.home}> 
                <div className={classes.selection}>
                    <Link className={classes.link} to="/new-evaluation">
                        Take New Prewriting Evaluation
                    </Link>
                    <Link className={classes.link} to="/records">
                        View Existing Evaluations
                    </Link>
                </div>
                <button className={classes.logout} onClick={logout}>
                    Log Out
                </button>
            </div>
        </div>
    );
}

export default Home;
