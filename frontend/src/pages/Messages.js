import React from 'react';
import styled from 'styled-components';
import Headset from '../assets/images/Group.png'
const StyledMessageBox=styled.div`
    display:flex;
    flex-direction:column;
    background-color:black;
    justify-content:center;
    align-items:center;

`
const StyledMyMessage=styled.div`
    display:flex;
`

const StyledMessage=styled.div`
    display: flex;
`
const StyledHeadsetImage=styled.img`
    background-color:white;
    width: 32px;
    heigth: 32px;
    border-radius:100%;
`
const StyledInput=styled.input`
    placeholder: "새로운 사람과의 대화를 시작합니다";
    size:text;
    width: 90vw;
`

const Messages = () => {
    return (
        <StyledMessageBox>
        메시지    
        
        <StyledMyMessage>
            <div >내가 보낸 메시지</div><StyledHeadsetImage src={Headset}/>
        </StyledMyMessage>
        <StyledMessage>
            <StyledHeadsetImage src={Headset}/><div background-color='#F5336D'>받은 메시지</div>
        </StyledMessage>

        <StyledInput />
        </StyledMessageBox>
    );
};

export default Messages;