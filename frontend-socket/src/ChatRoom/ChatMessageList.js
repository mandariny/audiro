import React from 'react';
import ChatMessage from './ChatMessage';

const ChatMessageList = (props) => {
    // 맵으로 돌면서 컴포넌트 생성
    // props로 정보 전달
    const chatMessageList = props.messageList && props.messageList.map((msg, index) => (
        <ChatMessage
        key={index}
        user_id={msg.userId}
        nickname={msg.userNickname}
        content_type={msg.contentType}
        content={msg.content}
        send_time={msg.sendTime}
        />
    ));

    return(
        <div>
            <ul>
                {chatMessageList}
            </ul>
        </div>
    )
}

export default ChatMessageList;