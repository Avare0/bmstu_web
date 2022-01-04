import React, {useContext, useEffect, useState} from 'react';
import NavBar from "../components/NavBar/NavBar";
import {Context} from "../index";
import OrdersModel from "../repos/OrdersModel";
import Loading from "../components/loader/Loading";
import {Link} from "react-router-dom";
import '../static/css/style.css';
const UserOrdersPage = () => {

    const [data, setData] = useState(null)

    const {store} = useContext(Context)

    let rep = new OrdersModel()

    function updateOrders(data) {
        setData(data.data)
    }

    useEffect(() => {
        rep.getUserOrders(JSON.parse(localStorage.getItem('user')).id, updateOrders)
    }, [])



    return (
        <div className='container'>
            {!data ? <Loading /> :
                <div>
            <h2>Мои заказы:</h2><br/>
            {data?.length == 0 ? <h4 style={{textAlign: 'center'}}>Вы еще ничего не бронировали</h4> : ''}
            {data?.map(order =>
                <div className="house_order">
                    <div className="house_order_date_and_num bold">
                        <div className="house_order_name">
                            <Link to={`/ads/${order.house.id}`} className="nolink">
                                {order.house.name}
                            </Link>
                        </div>
                    </div>

                    <div className="house_order_dates font_20">
                        {order.date_from} -
                        <br/>

                            {order.date_till}
                    </div>
                    <div className="house_order_dates font_20" style={{textAlign: 'right'}}>
                        {order.guests_amount + ' человек'}
                    </div>
                </div>
            )}
            </div>}
        </div>
    );
};

export default UserOrdersPage;