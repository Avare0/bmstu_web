import {makeAutoObservable} from "mobx";
import UserModel from "../repos/UserModel";
import {decode} from "jsonwebtoken";
import jwtDecode from "jwt-decode";

export default class Store {
    user = null;
    isAuthenticated = false;
    rep = new UserModel()

    constructor() {
        makeAutoObservable(this);
    }

    setAuth(bool) {
        this.isAuthenticated = bool
    }

    setUser(data) {
        this.user = data;
        this.user.photo = window.static_url + data.photo
    }

    async login(username, password) {
        try {
            const resp = await this.rep.login(username, password)
            localStorage.setItem('token', resp.data.access)
            localStorage.setItem('refresh', resp.data.refresh)
            this.setAuth(true);
            localStorage.setItem('user', JSON.stringify(resp.data.user))
            this.setUser(resp.data.user)
        } catch (e) {
            console.log(e.request)
        }

    }

    async logout() {
        localStorage.removeItem('token');
        localStorage.removeItem('refresh');
        localStorage.removeItem('user');
        // this.setUser({});
        this.setAuth(false);
    }

    async checkAuth() {
        console.log(localStorage.getItem('user'))
        if (localStorage.getItem('refresh')) {
            const resp = await this.rep.refresh(localStorage.getItem('refresh'))
            localStorage.setItem('token', resp.data.access)
        }
        if (localStorage.getItem('user') != 'null' & localStorage.getItem('user') != null) {
            this.setAuth(true);
            this.setUser(JSON.parse(localStorage.getItem('user')))
        }
    }
}