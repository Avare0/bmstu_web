import React from 'react';
import HouseFacilities from "./HouseFacilities";
import {Link} from "react-router-dom";
const HouseBriefDescription = ({data}) => {
    return (
        <div>
            <Link to={'/ads/' + data.id} className="nolink">
            <div className="house">
                <div className="house_img">
                    <img src={window.static_url+ data.house_photo[0].photo} alt="" />
                </div>
                <div className="house_info">
                    <h4>{ data.name }</h4>
                    <div style={{'display': 'flex'}}>
                        <div className="house_sleep">
                            <div className="house_img_sleep">
                                <img src={window.static_url+ '/house_description/sleep.png'} alt=""/>
                            </div>
                            <p className="amount">{ data.beds_amount }</p>
                        </div>
                        <div className="house_sleep">
                            <div className="house_img_sleep">
                                <img src={window.static_url+ '/house_description/user.png'} alt=""/>
                            </div>
                            <p className="amount">{data.guests_amount}</p>
                        </div>
                        <div className="house_sleep">
                            <div className="house_img_sleep">
                                <img src={window.static_url+ '/house_description/shower.png'} alt=""/>
                            </div>
                            <p className="amount">{data.bathrooms_amount}</p>
                        </div>
                    </div>
                    <p className="house_adress">
                        {data.city.name}, {data.city.country.name}, {data.address}
                    </p>
                </div>


                <div className="facilities_and_views">

                    <h3>Удобства</h3>
                    <HouseFacilities facilities={data.house_facilities} />

                </div>
            </div>

        </Link>
        </div>
    );
};

export default HouseBriefDescription;