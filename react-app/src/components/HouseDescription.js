import React, {useContext} from 'react';
import HouseFacilities from "./HouseFacilities";
import MyButton from "./MyButton";
import {Context} from "../index";
import {useNavigate} from "react-router-dom";

const HouseDescription = ({data}) => {
    const {store} = useContext(Context)
    const history = useNavigate()


    function redirect(data) {
        history('/ads')
    }


    return (
        <div style={{width: '50%'}}>
            {/*<br/>*/}
            <h1>Информация</h1>
            <div className="description">
                <p className="font_20">{data.desc}</p>
                <div className="house_sleep">
                    <div className="house_img_sleep">
                        <img src={window.static_url + 'house_description/sleep.png'} alt=""/>
                    </div>
                    <p className="amount">{data.beds_amount} - кол-во спальных мест</p>
                </div>
                <div className="house_sleep">
                    <div className="house_img_sleep">
                        <img src={window.static_url + 'house_description/user.png'} alt=""/>
                    </div>
                    <p className="amount">{data.guests_amount} - кол-во гостей</p>
                </div>
                <div className="house_sleep">
                    <div className="house_img_sleep">
                        <img src={window.static_url + 'house_description/shower.png'} alt=""/>
                    </div>
                    <p className="amount">{data.bathrooms_amount} - кол-во ванных комнат</p>
                </div>
                <p className="font_24 semibold">Дополнительные удобства:</p>
                <HouseFacilities facilities={data.house_facilities}/>
                <p className="font_24 semibold">Правила проживания:</p>
                {data.rules}
                <br/>
                {/*{(store.user.id == data.owner.id || store.user.type =='admin')&& <MyButton text='Удалить' onClick1={e=> rep.deleteHouse(data.id, redirect)} />}*/}
            </div>
        </div>
    );
};

export default HouseDescription;