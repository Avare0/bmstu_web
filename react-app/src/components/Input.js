import React from 'react';

const Input = ({type, onchange, value}) => {
    return (
        <input type={type} className='auth_input font_18 center' onChange={onchange} value={value}/>
    );
};

export default Input;