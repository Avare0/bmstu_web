import React from 'react';
import Input from "../components/Input";
import NavBar from "../components/NavBar/NavBar";
import AuthForm from "../components/forms/AuthForm";
import {observer} from "mobx-react-lite";
import '../static/css/style.css';
const AuthPage = () => {
    return (
        <div className='container'>
            <AuthForm />
        </div>
    )
};

export default observer(AuthPage);