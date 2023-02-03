import React from 'react';
import styled from 'styled-components';
import Headset from '../assets/images/Group.png'
import Send from '../assets/images/send.png'
const StyledMessageBox=styled.div`
    display:flex;
    flex-direction:column;
    
    justify-content:center;
    // align-items:center;
    margin:16px

`
const StyledMyMessage=styled.div`
    display:flex;
    justify-content:end;
    height:50px;
    margin:16px;
`

const StyledMessage=styled.div`
    display: flex;
    background-color: '#F5336D';
    height:50px;
    margin:16px;
`
const StyledHeadsetImage=styled.img`
    background-color:white;
    width: 42px;
    height: 42px;
    border-radius:100%;
    margin: 8px;
 
`
const StyledInput=styled.input`
    width: 85vw;
    background: transparent;
    margin: 8px;
    &:focus {
        outline: none;  
    }
`
const StyledOpponent=styled.div`
    background-color: #1E0E40;
    height: 50px;
    margin: 24px ;
    display: flex;
    align-items: center;
`

const StyledInputSet=styled.div`
    background-color: #1E0E40;
    display:flex;

`
const StyledSendImage=styled.img`
    width:20px;
    heigth:20px;
    
`
const StyledSentMessage=styled.div`
    border: 1px solid #6522F2;
    border-radius: 15px 0px 15px 15px;
    padding: 4px;
    margin: 4px;
`

const StyledGotMessage=styled.div`
    background-color: #6522F2;
    border-radius: 0px 15px 15px 15px; 
    padding: 4px;
    margin: 4px;
`
const StyledTime=styled.div`
    font-size: 12px;
`

const StyledSender=styled.div`
    color: #6522F2;
    font-size: 16px;
`

const StyledHr=styled.hr`
    width: 82vw;
    display: flex;
    justify-content: center;
    margin: 8px;
`
const StyledWriting=styled.div`
    font-size:16px;
`
const Messages = () => {
    function submitHandler(e){
        e.preventDefault()
        console.log('submitted')
    }
    return (
        <>
        <StyledOpponent>대화상대님과의 편지</StyledOpponent>  

        <StyledMessageBox>
          
        
        <StyledMyMessage> 
            <StyledSentMessage >내가 보낸 메시지 
                <br/>
                <br/><StyledTime>작성시간</StyledTime>
            </StyledSentMessage>
            <StyledHeadsetImage src={Headset}/> 
            
        </StyledMyMessage>
        <StyledMessage>
            <StyledHeadsetImage src={Headset}/>
            <div>
                <StyledSender> 보낸사람 </StyledSender> 
            <StyledGotMessage ><div>받은 메시지</div></StyledGotMessage>
            <StyledTime>작성시간</StyledTime>
            </div>
            
        </StyledMessage>
        <br/>
        <br/>
        </StyledMessageBox>

        <StyledHr/>
        <StyledWriting>메세지 입력 중...</StyledWriting>
        <StyledInputSet><form onSubmit={submitHandler}><StyledInput placeholder= "새로운 사람과의 대화를 시작합니다" type='text' /></form> <StyledSendImage src={Send}/></StyledInputSet>
        </>
    );
};

export default Messages;