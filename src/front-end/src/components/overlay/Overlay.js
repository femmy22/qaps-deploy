// This component helps prevent scroll bars from appearing.

import classes from './Overlay.module.css';

function Overlay(props) {
	return <div className={classes.window}>{props.children}</div>;
}

export default Overlay;
