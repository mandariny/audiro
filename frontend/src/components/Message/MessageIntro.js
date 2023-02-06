import React from 'react';
import Headset from '../../assets/images/Group.png'
import styled from 'styled-components';

const StyledChatRoom=styled.div`
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 5px;
`;

const StyledHeadset=styled.div`
    height: 40px;
    width: 40px;
    background-color: white;
    border-radius: 100%;
    margin-right: 10px;
`;

const StyledMessageIntroWrapper = styled.div`
    display: flex;
    justify-content: space-around;
    align-items: center;
    width: 250px;
`;

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
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 1px;
    font-size: 13px;
    font-family: var(--font-nanumSquareR);
`
const StyledNickname=styled.div`
    color: #6522F2;
    font-size: 14px;
    font-family: var(--font-nanumSquareEB);
`

const StyledTextCenter=styled.div`
    display: flex;
    flex-direction:column;
    justify-content: space-around;
    align-items:flex-start;
    margin-left:8px;
    margin-top: 5px;
    
    > div{
        display: block;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        width: 150px;
        margin-bottom: 10px;
        font-size: 14px;
        font-family: var(--font-nanumSquareR);
    }
    
`
const StyledTextRight=styled.div`
    display: flex;
    flex-direction:column;
    align-items: flex-end;
    justify-content: space-around;
    margin-right:8px;
    >*{
        margin-bottom: 5px;
    }
`

const MessageIntro = (props) => {
   
    return (
        <>
            <StyledChatRoom>
                <StyledHeadset/>

                <StyledMessageIntroWrapper>
                    <StyledTextCenter>
                        <StyledNickname>{props.nickname}</StyledNickname>
                        <div>{props.text} </div>
                    </StyledTextCenter>
                    <StyledTextRight>
                        <div>{props.time}</div>
                        <StyledUnread>{props.unread}</StyledUnread>
                    </StyledTextRight>
                </StyledMessageIntroWrapper>
    
            </StyledChatRoom>
            <StyledFlatline/>
            <hr/>
        </>
    );
};

export default MessageIntro;