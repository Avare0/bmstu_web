import React, {useContext, useEffect, useState} from 'react';
import {useNavigate, useParams} from "react-router-dom";
import NavBar from "../components/NavBar/NavBar";
import Loading from "../components/loader/Loading";
import HouseModel from "../repos/HouseModel";
import '../static/css/style.css';
import {Context} from "../index";
import ImageSlider from "../components/ImageSlider";
import HouseFacilities from "../components/HouseFacilities";
import MyButton from "../components/MyButton";
import OrderForm from "../components/forms/OrderForm";
import HouseTestimonials from "../components/forms/HouseTestimonials";
import HouseDescription from "../components/HouseDescription";
import DeleteButton from "../components/DeleteButton";
const HousePage = () => {
    let params = useParams();
    let rep = new HouseModel();
    let images = [];

    let [data, setData] = useState(null);
    useEffect(() => {
        rep.getById(params.id, getHouse);
    }, [])

    function getHouse(data) {
        data = data['data']
        setData(data);
        console.log(data);
    }

    // return (
    //     <div className='container'>
    //          {data ? <HouseView data={data}/> : <Loading />}
    //     </div>
    // );

    const [testimonials, setTestimonials] = useState([])


    // console.log(images)
    return (
        <div className='container'>
        {data ? <div>
            <div>
                <div className="house_header_flex">
                    <div className="header_wrapper">
                        <div style={{display: 'flex', alignItems: 'center'}}>
                            <h1>{data.name} </h1>
                            <DeleteButton id={data.id} owner_id={data.owner.id} />
                        </div>


                        <p className="font_24">{data.city.country.name}, {data.city.name}, {data.address}</p>
                    </div>
                    <div className="owner_wrapper">
                        <div className="owner" style={{alignContent: 'center', justifyContent: 'center'}}>
                            <p className="font_20"
                               style={{marginRight: '20px'}}>{data.owner.first_name} {data.owner.last_name}</p>
                            <div className="avatar">
                                <img src={window.static_url + data.owner.photo} alt=""/>
                            </div>

                        </div>
                    </div>
                </div>
            </div>
            <ImageSlider images={data.house_photo}/>
            <div className="info_order" >
                <HouseDescription data={data}/>
                <div style={{height: 'auto', backgroundColor: 'black', width: '2px', }} ></div>
                <OrderForm data={data} />
            </div>


            <HouseTestimonials id={data.id} />
        </div>: <Loading />}</div>
    );
};

export default HousePage;