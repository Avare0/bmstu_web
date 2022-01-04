import BaseModel from "./BaseModel";
import axios from "axios";
import React from 'react';
import {useContext} from "react";

export default class CitiesModel extends BaseModel{

    async getUserOrders(id, callback) {
        this.repository.get('/orders', {params: {user_id: id}}).then(resp => callback(resp.data));
    }
    async getCities(callback) {
        this.repository.get('/cities').then(resp => callback(resp.data))
    }
}