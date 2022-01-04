import React, {useEffect, useState} from 'react';
import Input from "../components/Input";
// import {Checkbox} from "rsuite";
import Select from "react-select";
import CitiesModel from "../repos/CitiesRep";
import MyButton from "../components/MyButton";
import HouseModel from "../repos/HouseModel";
import {Checkbox} from "@mui/material";
import {FormControlLabel} from "@mui/material";
import { makeStyles } from '@mui/styles';
import {withStyles} from "@mui/styles";
const AdCreatePage = () => {
    let rep = new CitiesModel()
    let houseRep = new HouseModel()

    let mapping = {
        sauna: 1,
        pool: 2,
        view: 3,
        washing: 4,
        parking: 5,
        conditioner: 6,
        wifi: 7
      }

    const [cities, setCities] = useState([])

    const [name, setName] = useState('')
    const [desc, setDesc] = useState('')
    const [city, setCity] = useState({})
    const [guests, setGuests] = useState(1)
    const [beds, setBeds] = useState(1)
    const [address, setAddress] = useState('')
    const [rules, setRules] = useState('')
    const [bathrooms, setBathrooms] = useState(1)

    const [photos, setPhotos] = useState(null);

    const options = [
        {value: 1, label: 'Moscow'},
        {value: 2, label: 'Paris'}
    ]

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

    function submit() {
                console.log(facilities)
        console.log(photos)

        let fd = new FormData()
        Array.from(photos).forEach(file => {
            fd.append('photo', file);
        })

        fd.append('name', name)
        fd.append('desc', desc)
        fd.append('city', city.value)
        fd.append('guests_amount', guests)
        fd.append('beds_amount', beds)
        fd.append('address', address)
        fd.append('rules', rules)
        fd.append('bathrooms_amount', bathrooms)
        // console.log(Object.keys(facilities).filter((k, i) => i == true))
        // Object.keys(facilities).filter((k, i) => i == true).forEach(
        //
        //     (k, i) => {
        //         console.log(k)
        //         fd.append('facility', mapping[k])
        //     }
        // )
        for (const key in facilities) {
            if (facilities[key] == true)
                fd.append('facility', mapping[key])
        }


        houseRep.createHouse(fd, (data) => {console.log('created')})
    }

    const [facilities, setFacilities] = React.useState({
        sauna: false,
        pool: false,
        view: false,
        washing: false,
        parking: false,
        conditioner: false,
        wifi: false
      });
    const { sauna, pool, view, washing, parking, conditioner, wifi } = facilities;
    const handleFlavorChange = (event) => {

        setFacilities({ ...facilities, [event.target.name]: event.target.checked });

      };

    const MyCheckbox = withStyles({
      root: {
        color: "black",
        "&$checked": {
          color: "black"
        }
      },
      checked: {}
    })((props) => <Checkbox color="default" {...props} />);

    const customStyles = {
      option: (provided, state) => ({
        ...provided,
        color: state.isSelected ? 'black' : 'black',
          backgroundColor: 'white',
      }),
      control: (provided, state) => ({
        ...provided,
        marginTop: "5%",
          width: '241px',
          color: 'black',
          border: state.isFocused? '1px solid black': '1px solid black'
      }),
        container: (provided) => ({
        ...provided,
          width: '241px'
      }),
    }
    return (
        <div className='container'>
            <div className="add_house_form">

                    <p className="auth_field">Название жилья</p>
                    <Input type='text' value={name} onchange={e => setName(e.target.value)} />
                    <p className="auth_field">Описание</p>
                    <Input type='text' value={desc} onchange={e => setDesc(e.target.value)} />
                    <p className="auth_field">Город</p>
                    <Select width='200px' styles={customStyles} options={cities} menuColor='black' value={city} onChange={updateCity}/>
                    <p className="auth_field">Количество гостей</p>
                    <Input type='number' value={guests} onchange={e => setGuests(e.target.value)} />
                    <p className="auth_field">Количество кроватей</p>
                    <Input type='number' value={beds} onchange={e => setBeds(e.target.value)}  />
                    <p className="auth_field">Адрес</p>
                    <Input type='text' value={address} onchange={e => setAddress(e.target.value)}  />
                    <p className="auth_field">Правила проживания</p>
                    <Input type='text' value={rules} onchange={e => setRules(e.target.value)}  />
                    <p className="auth_field">Количество ванных комант</p>
                    <Input type='number' value={bathrooms} onchange={e => setBathrooms(e.target.value)}  />

                    <p className="auth_field">Дополнительные удобства</p>
                    {/*<Checkbox title='asd' />*/}
                    {/*<div className="checkbox_flex">*/}

                    {/*    <div className="checkbox_block">*/}
                    {/*        <input type="checkbox" id="" value="{{ facility.id }}"*/}
                    {/*               name="facility[]" />*/}
                    {/*            <label htmlFor=''>*/}
                    {/*            </label>*/}
                    {/*            <p>123</p>*/}
                    {/*    </div>*/}

                    {/*</div>*/}
                    <div style={{display: 'flex', flexDirection: 'column'}}>
                    <FormControlLabel
                        control={
                          <MyCheckbox
                            checked={sauna}
                            onChange={handleFlavorChange}
                            name="sauna"
                          />
                        }
                        label="Сауна"
                      />
                    <FormControlLabel
                        control={
                          <MyCheckbox
                            checked={pool}
                            onChange={handleFlavorChange}
                            name="pool"
                          />
                        }
                        label="Бассейн"
                      />
                    <FormControlLabel
                        control={
                          <MyCheckbox
                            checked={view}
                            onChange={handleFlavorChange}
                            name="view"
                          />
                        }
                        label="Красивый вид"
                      />
                    <FormControlLabel
                        control={
                          <MyCheckbox
                            checked={washing}
                            onChange={handleFlavorChange}
                            name="washing"
                          />
                        }
                        label="Стиральная машина"
                      />
                    <FormControlLabel
                        control={
                          <MyCheckbox
                            checked={parking}
                            onChange={handleFlavorChange}
                            name="parking"
                          />
                        }
                        label="Парковка"
                      />
                    <FormControlLabel
                        control={
                          <MyCheckbox
                            checked={conditioner}
                            onChange={handleFlavorChange}
                            name="conditioner"
                          />
                        }
                        label="Кондиционер"
                      />
                    <FormControlLabel
                        control={
                          <MyCheckbox
                            checked={wifi}
                            onChange={handleFlavorChange}
                            name="wifi"
                          />
                        }
                        label="WI-FI"
                      />
                    </div>
                    <p className="auth_field">Фотографии жилого помещения</p>
                    <label className="upload bold font_18" style={{width: '200px', textAlign: 'center'}}>
                        Выбрать файлы
                        <input type="file" required multiple name="images" onChange={e => setPhotos(e.target.files)}/>
                    </label>
                    <br />
                <br />
                <MyButton text='Добавить жилое помещение' onClick1={submit}/>
                        {/*<button className="btn black bold font_20" style={{marginTip: '20px'}}>Добавить жилое помещение*/}
                        {/*</button>*/}

            </div>
            <br/>
            <br/>
            <br/>
        </div>
    );
};

export default AdCreatePage;