import axios from "axios";
import React from 'react';
import {useContext} from "react";
import BaseModel from "./BaseModel";
// axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';

class HouseModel extends BaseModel{

    async getAllHouses(callback) {
        this.repository.get('/houses').then(resp => callback(resp.data));
    }

    async getById(id, callback) {
        this.repository.get('/houses/' + id.toString()).then(resp => callback(resp.data));
    }
    async makeOrder(id, startDate, endDate, guests, user_id, callback) {
        this.repository.post('/orders', {
            house_id: id,
            date_from: startDate,
            date_till: endDate,
            guests_amount: guests
        });
    }

    async getUserHouses(id, callback) {
        this.repository.get('/houses', {params: {user_id: id}}).then(resp => callback(resp.data));
    }

    async createHouse(data, callback) {
        this.repository.post('/houses', data)
    }
    async deleteHouse(id, callback) {
        this.repository.delete(`/houses/${id}`).then(resp => callback(resp.data))
    }
}

export default HouseModel;
