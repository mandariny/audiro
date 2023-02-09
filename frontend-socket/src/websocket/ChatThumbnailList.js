import React from 'react';
import ChatThumbnail from './ChatThumbnail'

const ChatThumbnailList = (props) => {
    const chatThumbnailList = props.chatThumbnailList && props.chatThumbnailList.map((channel) => (
        <ChatThumbnail
        channel_id={channel.channelId}
        nickname={channel.nickname}
        last_message={channel.lastMessage}
        />
    ));

    return(
        <div>
            <ul>
                {chatThumbnailList}
            </ul>
        </div>
    )
}

export default ChatThumbnailList;