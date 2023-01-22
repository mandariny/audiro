import React from "react";
import {Route, Routes} from "react-router-dom";
import Home from './pages/Home';
import MyGift from './pages/MyGift';
import Messenger from './pages/Messenger';

function App() {
  return (
    <div className="app">
      <Routes>
        <Route exact path="/" component={Home}/>
        <Route path="/mygift" component={MyGift}/>
        <Route path="/messenger" component={Messenger}/>
      </Routes>
    </div>
  );
}

export default App;
