import React, {useContext, useEffect, useState} from 'react';

import TestimonialsModel from "../../repos/TestimonialsModel";
import MyButton from "../MyButton";
import {Context} from "../../index";
const HouseTestimonials = ({id}) => {
    let rep = new TestimonialsModel()

    const {store} = useContext(Context)

    const [testimonials, setTestimonials] = useState([])
    const [text, setText] = useState('')

    useEffect(() => {
        rep.getTestimonials(id, getTestimonials)
    }, [])

    function getTestimonials(data) {
        console.log(data)
        setTestimonials(data.data)
    }

    function updateTestimonials() {
        rep.getTestimonials(id, getTestimonials)
    }

    function onSumbit(e) {
        e.preventDefault()
        rep.makeTestimonial(id, {text: text}, updateTestimonials)
        setText('')
    }

    return (
        <div>
            <h1 className="" style={{textAlign: 'center', marginTop: '20px'}}>Отзывы</h1>
            {testimonials.map(rev =>
                <div className="message_wrapper">
                    <div className="message">


                        <div className="sender">
                            <div className="avatar">
                                <img src={window.static_url + rev.user.photo} alt=""/>
                            </div>
                            <p className="font_15">{rev.user.first_name} {rev.user.last_name}</p>
                        </div>
                        <div className="message_info">
                            <p>{rev.text}</p>
                            <p>{rev.date}</p>
                        </div>
                    </div>
                </div>
            )}
            <textarea style={{marginBottom: '20px'}} value={text} onChange={event => setText(event.target.value)} className='black font_18 testimon_textfield w-100' placeholder='Добавить отзыв'/>
            <MyButton text='Добавить отзыв' disabled={store.isAuthenticated? false: true} onClick1={onSumbit}/>
        </div>

    );
};

export default HouseTestimonials;