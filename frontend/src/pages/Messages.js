import React from 'react';
import styled from 'styled-components';
import Headset from '../assets/images/Group.png'
import Send from '../assets/images/send.png'
import Logo from '../components/Logo';
import Nav from '../components/Nav';

const StyledMessageBox=styled.div`
    display:flex;
    flex-direction:column;
    
    justify-content:center;
    // align-items:center;
    margin:16px;
`;

const StyledMyMessage=styled.div`
    display:flex;
    justify-content:end;
    height:50px;
    margin:16px;
`;

const StyledMessage=styled.div`
    display: flex;
    background-color: '#F5336D';
    height:50px;
    margin:16px;
`;
const StyledHeadsetImage=styled.img`
    background-color:white;
    width: 20px;
    height: 16px;
    border-radius:100%;
    margin: 8px;
`;
const StyledHeadsetWrapper=styled.div`
    background-color:white;
    border-radius:100%;
    width:35px;
    height:35px;
    display:flex;
    align-items:center;
    margin:8px
`;

const StyledInput=styled.input`
    width: 85vw;
    background: transparent;
    margin: 8px;
    &:focus {
        outline: none;  
    }
`;

const StyledOpponent=styled.div`
    background-color: #1E0E40;
    height: 38px;
    margin-top: 34px ;
    padding-left:16px;
    display: flex;
    align-items: center;
    width:90vw;
`;

const StyledOpponentWrapper=styled.div`
    display: flex;
    justify-content: center;
`;

const StyledInputSet=styled.div`
    background-color: #1E0E40;
    display: flex;
    flex-direction: row;
    width: 96vw;
    justify-content: center;
    align-items: center;
    margin:4px;
    padding:4px;

`;

const StyledSendImage=styled.input`
    width:20px;
    height:20px;
    
`;

const StyledSentMessage=styled.div`
    border: 1px solid #6522F2;
    border-radius: 15px 0px 15px 15px;
    padding: 10px 20px 1px 20px;
    margin: 4px;
    font-size: 10px;
    height:21px;
`;

const StyledGotMessage=styled.div`
    background-color: #6522F2;
    border-radius: 0px 15px 15px 15px; 
    padding: 10px 20px 1px 20px;
    margin: 4px;
    font-size: 10px;
    height:21px;
`;
const StyledTime=styled.div`
    font-size: 10px;
    line-height:12px;
    font-family: 'Inter';
    font-style: normal;
    text-align:end;
    margin:4px;
`;

const StyledSender=styled.div`
    color: #6522F2;
    font-size: 12px;
`;

const StyledHr=styled.hr`
    width: 90vw;
    display: flex;
    justify-content: center;
    margin: 8px;
`;
const StyledWriting=styled.div`
    font-size:16px;
    margin-left:36px;
    font-size:12px;
    line-height:12.1px;
`;


const Messages = () => {
    function submitHandler(e){
        e.preventDefault()
        console.log('submitted')
    }

    return (
        <>
        <Logo/>
        <Nav/>
        <StyledOpponentWrapper><StyledOpponent>????????????????????? ??????</StyledOpponent>  </StyledOpponentWrapper>

        <StyledMessageBox>
          
        
        <StyledMyMessage> 
            <StyledSentMessage >?????? ?????? ????????? 
                <br/>
                <br/><StyledTime>????????????</StyledTime>
            </StyledSentMessage>
            <StyledHeadsetWrapper><StyledHeadsetImage src={Headset}/></StyledHeadsetWrapper>
        </StyledMyMessage>
        

        <StyledMessage>
            <StyledHeadsetWrapper><StyledHeadsetImage src={Headset}/></StyledHeadsetWrapper>
            <div>
                <StyledSender> ???????????? </StyledSender> 
            <StyledGotMessage ><div>?????? ?????????</div></StyledGotMessage>
            <StyledTime>????????????</StyledTime>
            </div>  
        </StyledMessage>

        <br/>
        <br/>
        </StyledMessageBox>
        <StyledWriting>????????? ?????? ???...</StyledWriting>
        <StyledHr/>
        
        <StyledInputSet><form id='send' onSubmit={submitHandler}><StyledInput  placeholder= "????????? ???????????? ????????? ???????????????" type='text' /> </form> <StyledSendImage form='send' type='image' src={Send}/> </StyledInputSet>
        </>
    );
};

export default Messages;