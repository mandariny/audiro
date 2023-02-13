import React from 'react';
import { Link } from 'react-router-dom';

const ChatThumbnail = (props) => {

    return (
        // 해당 컴포넌트를 누르면 채팅방으로 이동함
        <div>
            <Link to={`/messenger/${props.channel_id}`}>
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