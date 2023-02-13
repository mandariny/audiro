import logo from './logo.svg';
import './App.css';
import ChatList from './websocket/ChatList';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import ChatRoom from './websocket/ChatRoom';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route exact path='/' element={<ChatList/>}/>
        <Route path='/channel/:channel_id' element={<ChatRoom/>}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
