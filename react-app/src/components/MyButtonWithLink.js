import React from 'react';
import {Link} from "react-router-dom";
const MyButtonWithLink = ({text, href, additionClasses=''}) => {


    return (
        <div>
            <Link className={"btn black bold " + additionClasses}  to={href} >{text}</Link>
        </div>
    );
};

export default MyButtonWithLink;