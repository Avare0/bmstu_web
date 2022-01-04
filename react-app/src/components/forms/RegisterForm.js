import React, {useContext, useEffect, useState} from 'react';
import Input from "../Input";
import MyButton from "../MyButton";
import '../../static/css/style.css'
import MyButtonWithLink from "../MyButtonWithLink";
import CitiesModel from "../../repos/CitiesRep";
import Select from "react-select";
import UserModel from "../../repos/UserModel";
import {Context} from "../../index";
import {useNavigate} from "react-router-dom";

const RegisterForm = () => {
    let rep = new CitiesModel()
    let userRep = new UserModel()

    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [lastName, setLastName] = useState('');
    const [firstName, setFirstName] = useState('');
     const [city, setCity] = useState({})
     const [cities, setCities] = useState([])
    const [sex, setSex] = useState({})
    const [type, setType] = useState({})
    const [photos, setPhotos] = useState(null);
    const sexes = [{
         value: 'm', label: 'Мужской'
    },
    {
         value: 'f', label: 'Женский'
    }]
    const types = [{
         value: 'guest', label: 'Гость'
    },
        {value: 'owner', label: 'Собственник'}]
    const {store} = useContext(Context);
    function getCities(data) {
        data = data.data
        let res = data.map((info) => {
            return {value: info.id, label: info.name}
        })
        setCities(res)
        console.log(res)
    }
    function updateCity(e) {
        setCity(e)
    }

    useEffect(()=> {
        rep.getCities(getCities)
    }, [])

    const customStyles = {
      option: (provided, state) => ({
        ...provided,
        color: state.isSelected ? 'black' : 'black',
          backgroundColor: 'white',
      }),
      control: (provided, state) => ({
        ...provided,

          width: '200px',
          color: 'black',
          border: '3px solid black',
          borderRadius: 'none',
          height: '35px',
          lineHeight: '35px'
      }),
        container: (provided) => ({
        ...provided,
          width: '200px',
            height: '35px',
            lineHeight: '35px',
            marginBottom: '15px',
      }),
        indicatorsContainer: (provided) => ({
            ...provided,
            height: '35px',
            lineHeight: '35px'
        }),
        input: (provided) => ({
            ...provided,
            height: '35px',
            lineHeight: '35px'
        })
    }
    const history = useNavigate()
    function registerCallback(data) {
        store.login(username, password)
        history('/ads')
    }



    function submit() {
        let fd = new FormData()
        fd.append('photo', photos[0]);

        fd.append('username', username)
        fd.append('first_name', firstName)
        fd.append('last_name', lastName)
        fd.append('password', password)
        fd.append('type', type.value)
        fd.append('sex', sex.value)

        userRep.register(fd, registerCallback)
        // houseRep.createHouse(fd, (data) => {console.log('created')})
    }

    return (
        <div>

             <div className="auth_form">
                 <form>
                <p className="auth_field">Имя пользователя</p>
                <Input type='text' onchange={e => setUsername(e.target.value)} value={username}/>
                <p className="auth_field">Пароль</p>
                <Input type='password' onchange={e => setPassword(e.target.value)} value={password}/>
                     <p className="auth_field">Имя</p>
                <Input type='text' onchange={e => setFirstName(e.target.value)} value={firstName}/>
                     <p className="auth_field">Фамилия</p>
                <Input type='text' onchange={e => setLastName(e.target.value)} value={lastName}/>

                     <p className="auth_field">Город</p>
                <Select width='150px' styles={customStyles} options={cities} menuColor='black' value={city} onChange={updateCity}/>
                     <p className="auth_field">Пол</p>
                     <Select width='150px' styles={customStyles} options={sexes} menuColor='black' value={sex} onChange={e=> setSex(e)}/>
                     <p className="auth_field">Тип пользователя</p>
                     <Select width='150px' styles={customStyles} options={types} menuColor='black' value={type} onChange={e=> setType(e)}/>
                     <p className="auth_field">Фотография</p>
                <label className="upload bold font_18" style={{width: '200px', textAlign: 'center'}}>
                        Выбрать файл
                        <input type="file" required name="images" onChange={e => setPhotos(e.target.files)}/>
                    </label>
                <MyButton text='Войти' onClick1={submit} />
                {/*<a className="btn black bold" href="/register">Регистрация</a>*/}
            </form>
        </div>

        </div>
    );
};

export default RegisterForm;