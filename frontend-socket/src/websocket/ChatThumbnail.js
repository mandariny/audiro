import React from 'react';
import { Link } from 'react-router-dom';

const ChatThumbnail = (props) => {

    return (
        // <div onClick={clickHandler}>
        <div>
            <Link to={`/channel/${props.channel_id}`}>
            {"채널명 : " + props.channel_id}
            <br></br>
            {"상대방 닉네임 : " + props.nickname}
            <br></br>
            {"마지막 메세지 : " + props.last_message}
            <br></br>
            {"마지막 대화 시간 : " + props.last_time}
            </Link>
        </div>
    )
}

export default ChatThumbnail;