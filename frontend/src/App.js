import React from "react";
import {BrowserRouter, Route, Routes} from "react-router-dom";
import Home from './pages/Home';
import GiftDetail from './pages/GiftDetail';
import Messenger from './pages/Messenger';
import './App.css';
import GiftList from "./pages/GiftList";
import Login from './pages/Login'
import Musicmate from "./pages/Musicmate";
import Intro from './pages/Intro'

import Others from "./pages/Others";
import Messages from "./pages/Messages";

function App() {

  return (
    <div>
      {/* <Logo userId='연희동 아자르'/> */}
      <BrowserRouter>
      {/* <Nav/> */}
      <Routes>
          <Route exact path="/" element={<Intro/>}/>
          <Route path='/intro' element={<Intro/>}/>
          <Route path='/home' element={<Home/>}/>

          <Route path="/gifts" element={<GiftList/>}/>
          <Route path="/gifts/:giftid" element={<GiftDetail/>}/>
          
          <Route path="/messenger" element={<Messenger/>}/>
          <Route path='/login' element={<Login/>}/>
          <Route path='/musicmate' element={<Musicmate/>}/> 
          
          <Route path='/others/:nickname' element={<Others/>}/>
          <Route path='/messenger/:opponent' element={<Messages/>} />
      </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;