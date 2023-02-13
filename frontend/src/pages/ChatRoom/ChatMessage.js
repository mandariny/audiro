import React from "react"
import styled from 'styled-components';

const StyledChatContainer = styled.div`
    display: flex;
    margin-bottom: 20px;
`;

const StyledChatProfile = styled.div`
    background-color: white;
    border-radius: 100%;
    width: 35px;
    height: 35px;
    margin-right: 15px;
`;

const StyledChatWrapper = styled.div`
    display: flex;
    flex-direction: column;
    justify-content: center;
`;

const StyledChatNickname = styled.div`
    font-size: 16px;
    font-family: var(--font-nanumSquareB);
    color: #6522F2;
`;

const StyledChatMsgYou = styled.div`
    font-size: 16px;
    font-family: var(--font-nanumSquareR);
    color: white;
    margin-top: 5px;
    background-color: #6522F2;
    padding: 10px;
    border-radius: 0px 10px 10px 10px;
    height: 20px;
`;

const StyledChatDate = styled.div`
    font-size: 13px;
    font-family: var(--font-nanumSquareL);
    color: white;
    margin-top: 5px;
    text-align: end;
`;

const ChatMessage = (props) => {
    console.log(props.user_id);

    const StringMessage = (props) => {
        return (
            <StyledChatContainer>
                <StyledChatProfile></StyledChatProfile>
                <StyledChatWrapper>
                    <StyledChatNickname>{props.nickname}</StyledChatNickname>
                    <StyledChatMsgYou>{props.content}</StyledChatMsgYou>
                    {/* {props.user_id} */}
                    {/* {props.content_type} */}
                    <StyledChatDate>{props.send_time}</StyledChatDate>
                </StyledChatWrapper>  
            </StyledChatContainer>
        )
    }

    // 이미지인 경우엔 http~~~하는 이미지 주소를 보여주게끔,,,
    const ImageMessage = (props) => {
        return(
            <StyledChatContainer>
                <StyledChatProfile></StyledChatProfile>
                <StyledChatWrapper>
                    <StyledChatNickname>{props.nickname}</StyledChatNickname>
                    <img alt="이미지 메세지" src={props.content}/>
                    {/* {props.user_id} */}
                    {/* {props.content_type} */}
                    <StyledChatDate>{props.send_time}</StyledChatDate>
                </StyledChatWrapper>
            </StyledChatContainer>
        )
    }

    // 메세지인 경우와 이미지인 경우로 나누어서 표현
    if(props.content_type == 'MESSAGE'){
        return (
            <StringMessage
                user_id={props.user_id}
                nickname={props.nickname}
                content_type={props.content_type}
                content={props.content}
                send_time={props.send_time}
            />
        )
    }
    return (
        <ImageMessage
            user_id={props.user_id}
            nickname={props.nickname}
            content_type={props.content_type}
            content={props.content}
            send_time={props.send_time}
        />
    )
}

export default ChatMessage;