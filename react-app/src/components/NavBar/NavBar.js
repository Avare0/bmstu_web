import React, {useContext, useEffect} from 'react';
import {Link} from "react-router-dom";
import MyButtonWithLink from "../MyButtonWithLink";
import {Context} from "../../index";
import {observer} from "mobx-react-lite";
import NavBarMenu from "./NavBarMenu";
const NavBar = () => {
    const {store} = useContext(Context)

    useEffect(() => {
        store.checkAuth()
    }, [])

    return (
        <div>
            <header>
            <div className="nav">
                <li className="nav-item bold nolink">
                    <Link className="nolink" to="/">Главная</Link>
                    <Link className="nolink" to="/ads">Объявления</Link>
                </li>
                <li>
                    <div className="auth nav-item">
                        {/*{% if not request.user.is_authenticated %}*/}

                        {!store.isAuthenticated ?
                            <div className="auth_btn"><MyButtonWithLink href="/auth" text="Авторизация" /></div>:
                            <NavBarMenu store={store} />
                        }

                            </div>
                            </li>
                            </div>

                            </header>
        </div>
    );
};

export default observer(NavBar);