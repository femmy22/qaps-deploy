// Simply a UI assistant component

import classes from "./Modal.module.css";

function Modal(props) {
	return <section className={classes.modal}>{props.children}</section>;
}

export default Modal;
