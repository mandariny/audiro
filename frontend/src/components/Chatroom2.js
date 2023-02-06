import React from 'react';
import Headset from '../assets/images/Group.png'
import styled from 'styled-components';

const StyledChatRoom=styled.div`
    display: flex;
    justify-content: space-between;
    background-color: #1E0E40;
    height:56px;

`

const StyledHeadset=styled.img`
    height: 40px;
    width: 40px;
    background-color: white;
    border-radius: 100%;
    margin-right: 8px;
    margin-left:8px;
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
    color: #6522F2;
    margin-top:4px;
    
`

const StyledTextCenter=styled.div`
    display: flex;
    flex-direction:column;

    justify-content: space-around;
    align-items;
    margin-left:8px;
    
`
const StyledTextRight=styled.div`
    display: flex;
    flex-direction:column;

    justify-content: space-around;
    align-items;
    margin-right:8px;
`

const Chatroom2 = (props) => {
    // if (props.text.length<15){
    //     while(props.text.length<15){
    //         props.text+='.'
    //     }
    // }
    // if (props.text.length>15){
    //     const tmp=props.text.slice(0,12)
    //     props.text=tmp+'...'
    // }
    return (
        <>
        <StyledChatRoom>
        <StyledHeadset src={Headset}/>
        <StyledTextCenter>
            <StyledNickname>{props.nickname}</StyledNickname>
            <div>{props.text} </div>
        </StyledTextCenter>
        <StyledTextRight>
            <div>{props.time}</div>
            <StyledUnread>{props.unread}</StyledUnread>
        </StyledTextRight>
        
        </StyledChatRoom>
        <StyledFlatline/>
        <hr/>
        </>
    );
};

export default Chatroom2;