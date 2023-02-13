import React, {useEffect, useState} from 'react';
import { Link } from 'react-router-dom';
import ChatThumbnail from './ChatThumbnail'

const ChatThumbnailList = (props) => {
    const [chatThumbnailList, setChatThumbnailList] = useState([]);
    
    useEffect(()=>{
        
        // 맵으로 돌면서 리스트 목록을 하나씩 컴포넌트화
        const chatList = props.chatThumbnailList && props.chatThumbnailList.map((channel, index) => (
            //  필요한 정보 props로 전달
                <ChatThumbnail
                key={index}
                channel_id={channel.channelId}
                nickname={channel.nickname}
                last_message={channel.lastMessage}
                last_time={channel.lastMessageTime}
                />
            
        ));
        setChatThumbnailList(chatList)
    }, [props.chatThumbnailList])

    return(
        <div>
            {/* 일단 ul로 각 컴포넌트 뿌리게만 해둠 */}
            <ul>
                {chatThumbnailList}
            </ul>
        </div>
    )
}

export default ChatThumbnailList;