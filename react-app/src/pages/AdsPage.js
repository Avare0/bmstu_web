import React, {useEffect, useState} from 'react';
import NavBar from "../components/NavBar/NavBar";
import HouseModel from "../repos/HouseModel";
import Loading from "../components/loader/Loading";
import '../static/css/style.css';
import HouseBriefDescription from "../components/HouseBriefDescription";
const AdsPage = () => {
    let rep = new HouseModel();

    let [data, setData] = useState(null);

    function getHouses(data) {
        data = data['data']
        setData(data);
    }

    useEffect(() => {
        rep.getAllHouses(getHouses);
    }, [])

    return (
        <div className='container'>

            {data ? <div>
            {data.map((information, index) =>
                <HouseBriefDescription data={information} key={index} />
            )}
        </div> : <Loading />}
        </div>
    );
};

export default AdsPage;