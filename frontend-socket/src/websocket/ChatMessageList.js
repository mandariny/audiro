import React from 'react';
import ChatMessage from './ChatMessage';

const ChatMessageList = (props) => {
    const chatMessageList = props.messageList && props.messageList.map((msg) => (
        <ChatMessage
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