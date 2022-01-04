import axios from "axios";
import React from 'react';
import {useContext} from "react";
import BaseModel from "./BaseModel";
// axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';

export default class TestimonialsModel extends BaseModel {

    async getTestimonials(id, callback) {
        this.repository.get(`/houses/${id}/testimonials`).then(resp => callback(resp.data));
    }

    async makeTestimonial(id, data, callback) {
        this.repository.post(`/houses/${id}/testimonials`, data).then(resp => callback());
    }
}