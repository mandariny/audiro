import React from "react";
import styled from 'styled-components';
import axios from "axios";

const StyleUserInfoContainer = styled.div`
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 30px;
`;

const StyleUserInfoImg = styled.div`
    border-radius: 100%;
    background-color: white;
    width: 70px;
    height: 70px;
    margin-bottom: 50px;
`;

const StyledUserInfoWrapper = styled.div`
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    width: 300px;
    margin-bottom: 10px;
`;

const StyleUserInfoTitle = styled.div`
    font-size: 16px;
    font-family: var(--font-nanumSquareB);
    color: white;
`;

const StyleUserInfoText = styled.div`
    font-size: 16px;
    font-family: var(--font-nanumSquareL);
    color: white;
`;

const UserInfo = () =>{

    return (
        <StyleUserInfoContainer>
            <StyleUserInfoImg></StyleUserInfoImg>
            <StyledUserInfoWrapper>
                <StyleUserInfoTitle>이름</StyleUserInfoTitle>
                <StyleUserInfoText>이가옥</StyleUserInfoText>
            </StyledUserInfoWrapper>
            <StyledUserInfoWrapper>
                <StyleUserInfoTitle>이메일</StyleUserInfoTitle>
                <StyleUserInfoText>dlrkdhr321@gmail.com</StyleUserInfoText>
            </StyledUserInfoWrapper>
            <StyledUserInfoWrapper>
                <StyleUserInfoTitle>닉네임</StyleUserInfoTitle>
                <StyleUserInfoText>okiii</StyleUserInfoText>
            </StyledUserInfoWrapper>

        </StyleUserInfoContainer>
      )
};

export default UserInfo;