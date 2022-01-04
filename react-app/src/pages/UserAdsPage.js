import React, {useEffect, useState} from 'react';
import HouseBriefDescription from "../components/HouseBriefDescription";
import HouseModel from "../repos/HouseModel";
import {Link} from "react-router-dom";
import MyButtonWithLink from "../components/MyButtonWithLink";
import Loading from "../components/loader/Loading";
import '../static/css/style.css';
const UserAdsPage = () => {
    let rep = new HouseModel();

    let [data, setData] = useState([]);

    function getHouses(data) {
        data = data['data']
        setData(data);
    }

    useEffect(() => {
        rep.getUserHouses(JSON.parse(localStorage.user).id, getHouses);
    }, [])
    return (
        <div className='container'>
            <MyButtonWithLink style={{marginBottom: '20px'}} href="/ads/create" additionalClasses="testimonial_btn" text='Создать объявление' />
            <h2>Мои объявления</h2>
            {data.length == 0 ? <Loading /> :
                <div>
                {data.map((information, index) =>
                    <HouseBriefDescription data={information} key={index} />
                )}
                    </div>}
        </div>
    );
};

export default UserAdsPage;