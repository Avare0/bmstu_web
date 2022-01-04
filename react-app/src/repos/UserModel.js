import BaseModel from "./BaseModel";

class UserModel extends BaseModel{

    async login(username, password) {
        return this.repository.post('/users/token', {'username' : username, 'password': password})
    }

    async refresh(token) {
        return this.repository.post('/users/refresh', {'refresh' : token})
    }

    async register(data, callback) {
        this.repository.post('/users', data).then(resp => callback(resp.data))
    }



}

export default UserModel;