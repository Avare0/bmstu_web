import React, {useContext, useState} from 'react';
import DateRangePicker from "react-bootstrap-daterangepicker";
import MyButton from "../MyButton";
import Input from "../Input";
import HouseModel from "../../repos/HouseModel";
import {Context} from "../../index";
const OrderForm = ({data}) => {

    const {store} = useContext(Context)

    let rep = new HouseModel()
    const [startDate, setStartDate] = useState('')
    const [endDate, setEndDate] = useState('')
    const [guests, setGuests] = useState(1)

    function handleApply(event, picker) {
        setStartDate(picker.startDate.format('YYYY-MM-DD'));
        setEndDate(picker.endDate.format('YYYY-MM-DD'));
    }
    function submit(e) {
        e.preventDefault()
        console.log(startDate, endDate, guests)
        rep.makeOrder(data.id, startDate, endDate,  guests)
    }

    function today() {
            var date = new Date();
            var dd = String(date.getDate()).padStart(2, '0');
            var mm = String(date.getMonth() + 1).padStart(2, '0'); //January is 0!
            var yyyy = date.getFullYear();

            let date_str = yyyy + '-' + mm + '-' + dd;
            return date_str;
        }
    function invalidDates(date) {
        // console.log(date.format('YYYY-MM-DD'))
        // for(let i = 0; i < date.orders_house.length; i++)
        let check_date = new Date(date);
        console.log(check_date)
        if (check_date < new Date(today()))
            return true;
        for (let i = 0; i < data.orders_house.length; i++) {
            let date1 = new Date(data.orders_house[i].date_from);
            let date2 = new Date(data.orders_house[i].date_till);
            date1.setDate(date1.getDate() - 1);
            console.log(date1, date2)
            if (check_date >= date1 - 1 && check_date <= date2)
                return true;

        }
        return false;
    }
    console.log(store.isAuthenticated, 'auth')

    return (
        <div  style={{width: '48%', marginLeft: '20px'}}>
            {/*<br/>*/}
            <h1 style={{textAlign: 'left'}}>Бронирование</h1>
            <div className="order">
                <div className="row">
                    <p className='font_20'>Даты пребывания: </p>

                <DateRangePicker initialSettings={{
                    startDate: today(), endDate: today(), autoApply: true, locale: {
                        format: 'YYYY-MM-DD'
                    }, isInvalidDate: invalidDates
                }} onApply={handleApply}>
                    <input type="text" className="black bold font_20"
                           style={{height: '45px', marginRight: '20px', textAlign: 'center'}} />
                </DateRangePicker>
                    </div>
                <div className="row">
                    <p className='font_20'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Кол-во гостей: </p>
                    <input type="text" placeholder="Кол-во гостей" className="black bold font_20"
                       style={{width: '290px', textAlign: 'center', height: '45px', marginRight: '20px'}} value={guests} onChange={e => setGuests(e.target.value)} />
                </div>


                {/*<button className="btn black bold testimonial_btn" type="submit"></button>*/}
                <MyButton text="ЗАБРОНИРОВАТЬ" disabled={store.isAuthenticated? false: true} additionalClasses="testimonial_btn" onClick1={submit} />
                {/*</form>*/}
            </div>
        </div>
    );
};

export default OrderForm;