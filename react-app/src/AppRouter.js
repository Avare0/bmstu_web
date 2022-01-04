import React from 'react';

import {Route, BrowserRouter, Routes} from "react-router-dom";
import UserOrdersPage from "./pages/UserOrdersPage";
import AuthPage from "./pages/AuthPage";
import AdsPage from "./pages/AdsPage";
import HousePage from "./pages/HousePage";
import NavBar from "./components/NavBar/NavBar";
import UserAdsPage from "./pages/UserAdsPage";
import MainPage from "./pages/MainPage";
import AdCreatePage from "./pages/AdCreatePage";
import RegisterPage from "./pages/RegisterPage";
const AppRouter = () => {
    return (
            <BrowserRouter>
                <div className='container'>
                    <NavBar/>
                    </div>
                <Routes>

                    <Route exact path='/ads' element={<AdsPage/>} />
                    <Route exact path='/ads/:id' element={<HousePage/>} />
                    <Route exact path='/auth' element={<AuthPage />} />
                    <Route exact path='/orders' element={<UserOrdersPage />} />
                    <Route exact path='/userads' element={<UserAdsPage />} />
                    <Route exact path='/ads/create' element={<AdCreatePage />} />
                    <Route exact path='/' element={<MainPage />}/>
                    <Route exact path='/register' element={<RegisterPage />}/>
                </Routes>
            </BrowserRouter>
    );
};

export default AppRouter;