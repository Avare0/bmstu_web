import axios from "axios";


class BaseModel {

    constructor() {
        this.repository = axios.create({
            withCredentials: true,
            baseURL: window.base_api_url
        })
        this.repository.interceptors.request.use(config => {
            if (localStorage.getItem('token') !== null)
                config.headers.authorization = `Bearer ${localStorage.getItem('token')}`
            return config
        })
    }
}

export default BaseModel;