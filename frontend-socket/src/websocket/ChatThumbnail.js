import React from 'react';
import { Link } from 'react-router-dom';

const ChatThumbnail = (props) => {
    
    const clickHandler = () =>{
        console.log("click!");
        // Navigate(`/channel/${props.channel_id}`);
    }

    return (
        // <div onClick={clickHandler}>
        <div>
            <Link to={`/channel/${props.channel_id}`}>
            {props.channel_id}
            {props.nickname}
            {props.last_message}
            </Link>
            
        </div>
    )
}

export default ChatThumbnail;