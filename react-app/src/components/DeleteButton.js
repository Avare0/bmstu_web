import React, {useContext} from 'react';
import {useNavigate} from "react-router-dom";
import {Context} from "../index";
import HouseModel from "../repos/HouseModel";

const DeleteButton = ({id, owner_id}) => {
    const history = useNavigate()
    let rep = new HouseModel();
    const {store} = useContext(Context)
    function redirect() {
            history('/ads')
        }
    return (
       <div style={{marginLeft: '10px', "&:hover": {
      cursor: 'pointer'
    }}} onClick={e=> rep.deleteHouse(id, redirect)}>

             {(store.user.id == owner_id || store.user.type =='admin')&&<div style={{ width: '50px', height: '50px'}}>
                <img src={window.static_url+'bin.png'} alt="" style={{
                    width: '30px',
                    height: '30px',
                    marginLeft: 'auto',
                    marginRight: 'auto',
                    display: 'block',
                    marginTop: '14px'}}/>
            </div>}
        </div>
    );
};

export default DeleteButton;