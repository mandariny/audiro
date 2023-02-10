import React from 'react';
import { Link } from 'react-router-dom';
import ChatThumbnail from './ChatThumbnail'

const ChatThumbnailList = (props) => {
    const chatThumbnailList = props.chatThumbnailList && props.chatThumbnailList.map((channel) => (
        // <Link to={`/channel/${props.channel_id}`}>
            <ChatThumbnail
            channel_id={channel.channelId}
            nickname={channel.nickname}
            last_message={channel.lastMessage}
            />
        // </Link>
        
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