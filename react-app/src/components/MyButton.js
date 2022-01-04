import React from 'react';
import {Link} from "react-router-dom";
const MyButton = ({text, classes, onClick1, disabled=false}) => {
    return (
            <button type="button" className={"btn black bold " + classes} disabled={disabled} onClick={(e) => onClick1(e)}>{text}</button>
    );
};

export default MyButton;