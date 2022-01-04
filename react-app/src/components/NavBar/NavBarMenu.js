import React, {useContext, useEffect} from 'react';
import {Context} from "../../index";
import {observer} from "mobx-react-lite";
import MyButton from "../MyButton";
import {Link} from "react-router-dom";
import NavLink from "./NavLink";
const NavBarMenu = ({store}) => {


    return (
        <div>
            <div className="lk">
                <div className="lk_username bold">
                    {store.user?.first_name} {store.user?.last_name}
                </div>
                <div className="lk_img avatar">
                    <img src={store.user?.photo} alt=""/>
                </div>
                <div class="dropdown">
                    <div class="wrapper"><Link className="nolink" to="/orders">Заказы</Link></div>

                    {(store.user?.type == 'admin' || store.user?.type == 'owner') &&<div class="wrapper">
                        <Link className="nolink" to="/userads">Объявления</Link>
                    </div>}
                    <div class="wrapper"><Link to='/ads' onClick={e => store.logout()}>Выход</Link></div>

                </div>
            </div>
        </div>

);
};

export default observer(NavBarMenu);