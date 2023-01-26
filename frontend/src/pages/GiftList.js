import React from "react";
import {BrowserRouter, Route, Routes,Link} from "react-router-dom";
import Home from './Home';
import MyGift from './MyGift';
import Messenger from './Messenger';

const GiftList = () =>{
    return (
        <div>
            <h1> Home</h1>
            
            <img src='https://www.naver.com' height={100} width={100} /> 
            <img src='https://www.naver.com' height={100} width={100} /> 
            <img src='https://www.naver.com' height={100} width={100} /> 
            <br/>
            <img src='https://www.kakao.com' height={100} width={100} /> 
            <img src='https://www.naver.com' height={100} width={100} /> 
            <img src='https://www.naver.com' height={100} width={100} /> 
            <br/>
            <Link to="/gifts/:giftid"><img src='https://shop2.daumcdn.net/thumb/R500x500/?fname=http%3A%2F%2Fshop2.daumcdn.net%2Fshophow%2Fp%2FZ20293623281.jpg%3Fut%3D20221209092821' height={100} width={100} /></Link>
            <Link to="/gifts/:giftid"><img src='http://www.akbobada.com/home/akbobada/archive/akbo/img/202212200942036.jpg' height={100} width={100} /></Link>
            <Link to="/gifts/:giftid"><img src='https://image.bugsm.co.kr/album/images/200/40824/4082425.jpg?version=20230105002539.0' height={100} width={100} /></Link>
            <br/>
            {/* <BrowserRouter>
            <Routes>
                <Route exact path="/" element={<Home/>}/>
                <Route path="/mygift" element={<MyGift/>}/>
                <Route path="/gifts" element={<GiftList/>}/>
                <Route path="/messenger" element={<Messenger/>}/>
              </Routes>
            </BrowserRouter> */}
        </div>
      )
};
   
export default GiftList;