import React from "react";
import '../styles/Home.css'
import styled from 'styled-components';
import naver_logo from '../assets/images/naver_logo.png'
import Logo from "../components/Logo";
import kakao from "../assets/images/kakao_logo.png"
import naver from "../assets/images/naver_logo.png"
import google from "../assets/images/google_logo.png"

const StyledLoginContainer = styled.div`
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin-top: 80px;
`;

const StyledLoginTitle = styled.div`
    font-size: 20px;
    font-family: var(--font-nanumSquareR);
    margin-bottom: 20px;
`;

const StyledLoginBtnWrapper = styled.div`
    background-color: #6522F2;
    padding: 40px;
    border-radius: 50px;
`;

const StyledLoginBtn = styled.div`
    color: #000000;
    background-color: ${props => props.background};
    padding-left: 20px;
    padding-right: 20px;
    padding-top: 10px;
    padding-bottom: 10px;
    margin-bottom: 10px;
    border-radius: 20px;
    font-size: 15px;
    font-family: var(--font-nanumSquareR);
    display: flex;
    align-items: center;
    justify-content: center;
`;

const StyledLoginLogo = styled.div`
    margin-right: 5px;
    display: flex;
    align-items: center;
    justify-content: center;
`;

const Home = () =>{

    return (
        <div>
            <Logo />
            <StyledLoginContainer>
            <StyledLoginTitle>로그인</StyledLoginTitle>
            <StyledLoginBtnWrapper>
                <StyledLoginBtn background="#FFE812"> 
                    <StyledLoginLogo><img src={kakao} height="20"/></StyledLoginLogo> 카카오로 로그인하기
                </StyledLoginBtn>
                <StyledLoginBtn background="#FFFFFF"> 
                    <StyledLoginLogo><img src={google} height="20"/></StyledLoginLogo>
                    구글로 로그인하기
                </StyledLoginBtn>
                <StyledLoginBtn background="#FFFFFF"> 
                    <StyledLoginLogo><img src={naver} height="20"/></StyledLoginLogo>
                    네이버로 로그인하기
                </StyledLoginBtn>
            </StyledLoginBtnWrapper>
            {/* <button id='naver-login'><a href={'https://www.naver.com'}><img src={naver_logo}/>네이버로 로그인하기</a> </button>
            <br/>
            <button id='kakao-login'><a href={'https://www.kakao.com'}><div class='link-text'>카카오로 로그인하기</div> </a> </button>
            <br/>
            <button id='google-login'><a href={'https://www.google.com'}><div class='link-text'>구글로 로그인하기</div> </a> </button>
            <br/> */}
            </StyledLoginContainer>

        </div>
      )
};
   
export default Home;