import React, {useContext, useState} from 'react';
import Input from "../Input";
import MyButton from "../MyButton";
import MyButtonWithLink from "../MyButtonWithLink";
import {Context} from "../../index";
import {Icon} from "@mui/material";
import {observer} from "mobx-react-lite";
import {useNavigate} from "react-router-dom";
const AuthForm = () => {

    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const {store} = useContext(Context);
    const history = useNavigate()

    function redirect() {
        store.login(username, password)
        history('/ads')
    }

    return (
        <div className="auth_form">
            <form>
                <p className="auth_field">Имя пользователя</p>
                <Input type='text' onchange={e => setUsername(e.target.value)} value={username}/>
                <p className="auth_field">Пароль</p>
                <Input type='password' onchange={e => setPassword(e.target.value)} value={password}/>

                <MyButton text='Войти' onClick1={() => redirect()} />
            </form>
            <br/>
                <MyButtonWithLink href="/register" text='Регистрация' />
                {/*<a className="btn black bold" href="/register">Регистрация</a>*/}
        </div>
    );
};

export default observer(AuthForm);