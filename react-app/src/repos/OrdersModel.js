import BaseModel from "./BaseModel";
import axios from "axios";
import React from 'react';
import {useContext} from "react";

export default class OrdersModel extends BaseModel{

    async getUserOrders(id, callback) {
        this.repository.get('/orders', {params: {user_id: id}}).then(resp => callback(resp.data));
    }
}