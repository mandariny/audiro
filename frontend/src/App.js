import React from "react";
import {BrowserRouter, Route, Routes} from "react-router-dom";
import Home from './pages/Home';
import MyGift from './pages/MyGift';
import Messenger from './pages/Messenger';
import Nav from './components/Nav';
import './App.css';
import Logo from './components/Logo';
import GiftList from "./pages/GiftList";
function App() {
  return (
    <div>
      <Logo/>
      <BrowserRouter>
      <Nav/>
      <Routes>
          <Route exact path="/" element={<Home/>}/>
          <Route path="/gifts/:giftid" element={<MyGift/>}/>
          <Route path="/gifts" element={<GiftList/>}/>
          <Route path="/messenger" element={<Messenger/>}/>
        </Routes>
      </BrowserRouter>
      
    </div>
  );
}

export default App;