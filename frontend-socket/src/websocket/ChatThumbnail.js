import React from 'react';
import { Navigate, useNavigate } from 'react-router-dom';

const ChatThumbnail = (props) => {
    
    const clickHandler = () =>{
        console.log("click!");
        Navigate(`/channel/${props.channel_id}`);
    }

    return (
        <div onClick={clickHandler}>
            {props.channel_id}
            {props.nickname}
            {props.last_message}
        </div>
    )
}

export default ChatThumbnail;