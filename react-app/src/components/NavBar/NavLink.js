import React from 'react';

const NavLink = ({text, func}) => {

    function action(e) {
        e.preventDefault()

    }

    return (
        <a className='nolink' onClick={func}>{text}</a>
    );
};

export default NavLink;