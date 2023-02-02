import React from "react";
import '../styles/Messenger.css'

import styled from 'styled-components';
import Chatroom2 from '../components/Chatroom2'
const Messenger=() => {
  const example=[
    {nickname:'신촌너구리',text:"일과 끝나고 노래 들었",time:"오후 2:00",unread:2},
    {nickname:'전체 개발자',text:"코딩할 때 듣기 너무 좋은 노래네요",time:"오후 2:00",unread:1}
  ]
  
    return (
        <div>
            <h1>Messenger</h1>
            
            {example.map(item => <Chatroom2 {...item}/>)}
            
        </div>
       
    )
  }

export default Messenger;