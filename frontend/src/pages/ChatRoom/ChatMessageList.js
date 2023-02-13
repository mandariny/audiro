import React, {useEffect, useRef} from 'react';
import ChatMessage from './ChatMessage';
import styled from 'styled-components';

const StyledChatContainer = styled.div`
    display: flex;
    flex-direction: column;
    margin-left: 30px;
    margin-right: 30px;
    overflow: auto;
    height: 500px;
    /* margin-bottom: 50px; */
`;

const StyledChatRoomTitle = styled.div`
    font-size: 17px;
    font-family: var(--font-nanumSquareEB);
    margin-bottom: 25px;
    color: white;
    margin-top: 30px;
    margin-left: 20px;
    margin-right: 20px;
    padding: 10px;
    background-color: rgba(65, 22, 162, 0.5);
`;

const ChatMessageList = (props) => {
    // 맵으로 돌면서 컴포넌트 생성
    // props로 정보 전달
    console.log(props.userId);
    const chatMessageList = props.messageList && props.messageList.map((msg, index) => (
        msg.userId == 1 ?
            <ChatMessage
                key={index}
                user_id={msg.userId}
                nickname={msg.userNickname}
                content_type={msg.contentType}
                content={msg.content}
                send_time={msg.sendTime}
                />
         : <></>
    ));

    const scrollRef = useRef(null);
    const scrollToBottom = () => {
        scrollRef.current?.scrollIntoView({ behavior: "smooth" });
    }
    useEffect(()=>{
        scrollToBottom()
    }, [])


    return(
        <>            
            <StyledChatRoomTitle>gaok님과의 편지</StyledChatRoomTitle>
            <StyledChatContainer>
                {chatMessageList}
                {/* <div ref={scrollRef}/> */}
            </StyledChatContainer>
        </>
    )
}

export default ChatMessageList;