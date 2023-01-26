import React from "react";
import {BrowserRouter, Route, Routes,Link} from "react-router-dom";
import Home from './Home';
import MyGift from './MyGift';
import Messenger from './Messenger';
import "../styles/GiftList.css"

const GiftList = () =>{
    return (
        <div>
            <h1> Home</h1>
            <div className="gift-list">
            <Link to="/gifts/:giftid"><img src='https://media.discordapp.net/attachments/1056882470429138968/1068086212054745118/love1.jpg' height={105} width={170} /></Link>
            <Link to="/gifts/:giftid"><img src='https://cdn.discordapp.com/attachments/1056882470429138968/1068086212272861245/love2.jpg' height={105} width={170} /></Link>
            <Link to="/gifts/:giftid"><img src='https://media.discordapp.net/attachments/1056882470429138968/1068086212444819486/love3.jpg' height={105} width={170} /></Link>
   
            <Link to="/gifts/:giftid"><img src='https://cdn.discordapp.com/attachments/1056882470429138968/1068086212650336297/love4.jpg' height={105} width={170} /></Link>
            <Link to="/gifts/:giftid"><img src='https://cdn.discordapp.com/attachments/1056882470429138968/1068081563310506014/Notes_230126_170914.jpg' height={105} width={170} /></Link>
            <Link to="/gifts/:giftid"><img src='https://cdn.discordapp.com/attachments/1056882470429138968/1068086212876841020/love5.jpg' height={105} width={170} /></Link>
      
            <Link to="/gifts/:giftid"><img src='https://shop2.daumcdn.net/thumb/R500x500/?fname=http%3A%2F%2Fshop2.daumcdn.net%2Fshophow%2Fp%2FZ20293623281.jpg%3Fut%3D20221209092821' height={105} width={170} /></Link>
            <Link to="/gifts/:giftid"><img src='http://www.akbobada.com/home/akbobada/archive/akbo/img/202212200942036.jpg' height={105} width={170} /></Link>
            <Link to="/gifts/:giftid"><img src='https://image.bugsm.co.kr/album/images/200/40824/4082425.jpg?version=20230105002539.0' height={105} width={170} /></Link>
            
            {/* <BrowserRouter>
            <Routes>
                <Route exact path="/" element={<Home/>}/>
                <Route path="/mygift" element={<MyGift/>}/>
                <Route path="/gifts" element={<GiftList/>}/>
                <Route path="/messenger" element={<Messenger/>}/>
              </Routes>
            </BrowserRouter> */}
            </div>
        </div>
      )
};
   
export default GiftList;