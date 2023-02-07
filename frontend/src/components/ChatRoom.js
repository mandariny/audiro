import React from 'react';
import Headset from '../assets/images/Group.png'
import styled from 'styled-components';

const StyledChatRoom=styled.div`
    display: flex;
    justify-content: space-around;
    background-color: #1E0E40;
    height:56px;

`

const StyledHeadset=styled.img`
    height: 40px;
    width: 40px;
    background-color: white;
    border-radius: 100%;
    margin-right: 8px;
`

const StyledFlatline=styled.div`
    // color: white;
    // width: 300px;
    // height: 1px;
`
const StyledUnread=styled.div`
    background-color: #F5336D;
    width:20px;
    height:20px;
    border-radius: 100%;
    text-align: center;
`
const StyledNickname=styled.div`
    color: #6522F2
`

const StyledText=styled.div`
    display: flex;
    flex-direction:column;

    justify-content: space-around;
    align-items
`

const ChatRoom = () => {
    return (
        <>
        <StyledChatRoom>
        <StyledHeadset src={Headset}/>
        <StyledText>
            <StyledNickname>신촌너구리</StyledNickname>
            <div>일과 끝나고 노래들었... </div>
        </StyledText>
        <StyledText>
            <div>오후 2:00</div>
            <StyledUnread>2</StyledUnread>
        </StyledText>
        
        </StyledChatRoom>
        <StyledFlatline/>
        <hr/>
        </>
    );
};

export default ChatRoom;