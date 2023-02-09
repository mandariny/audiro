import React, {useState, useEffect} from "react";
import styled, { keyframes } from 'styled-components';
import {BsHeadphones} from "react-icons/bs"

import axios from "axios";
import jwt from 'jwt-decode';

const StyledLogoContainer = styled.div`
    display: flex;
    flex-direction: column;
    margin-left: 35px;
    padding-top: 20px;
`;

const StyledLogoCircleLeft = styled.div`
    position: absolute;
    top: 35px;
    left: 25px;
    z-index: -99;
    width: 27px;
    height: 27px;
    background-color: rgba(101, 34, 242, 0.56);
    border-radius: 100%;
`;

const StyledLogoText=styled.div`
    font-size: 40px;
    font-family: var(--font-nanumSquareEB);
`;

const StyledLogo = styled.div`
    font-size: 40px;
    font-family: var(--font-nanumSquareEB);
    color: white;
`;

const moveInLeft = keyframes`
    0% {
        opacity: 0;
        transform: translateX(-50px);
    }
    80% {
        transform: translateX(10px);
    }
    100% {
        opacity: 1;
        transform: translateY(0);
    }
`

const StyledSubLogo = styled.div`
    font-size: 16px;
    font-family: var(--font-nanumSquareL);
    animation-name: ${moveInLeft};
    animation-duration: 3s;
    color: white;
`;

const StyledLogoCircleRight = styled.div`
    position:absolute;
    top: 20px;
    left: 120px;
    z-index: -99;
    width: 70px;
    height: 70px;
    background-color: rgba(101, 34, 242, 0.56);
    border-radius: 100%;
`;

const StyledLogoGreet=styled.div`
    display: flex;
    justify-content: end;
    margin-right: 15px;
    align-items: center;
`;

const StyledLogoHeadset=styled.div`
    background-color: white;
    border-radius: 100%;
    width: 20px;
    height: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 3px;
`;

const StyledLogoProfile = styled.div`
    text-align: end;
    color: white;
    margin-right: 5px;
    font-size: 15px;
    font-family: var(--font-nanumSquareR);
    margin-left: 5px;
`;

const Logo=(props)=>{   

    const token = localStorage.getItem('login-token');
    console.log(jwt(token));
    const nickname = jwt(token)['nickName']; 
    console.log(nickname);
    const userId = jwt(token)['userId']; 
    console.log(userId);

    const [userImg, setuserImg] = useState();
    useEffect(() => {
        axios.get(`http://i8a402.p.ssafy.io/api/user/${userId}`, {headers: {Auth: `${token}`}})
            .then((res) => {
                 setuserImg(res.data.img);
                })
    }, []);

    return(
        <StyledLogoContainer>
            <StyledLogoCircleLeft></StyledLogoCircleLeft>
            <StyledLogo>어디:로</StyledLogo>
            <StyledSubLogo>나와 새로운 사람의 음악 공간</StyledSubLogo>
            <StyledLogoGreet>
                <StyledLogoHeadset>
                    <img src={userImg}/>
                </StyledLogoHeadset>
                <StyledLogoProfile>{nickname}님</StyledLogoProfile>
            </StyledLogoGreet>
            <StyledLogoCircleRight></StyledLogoCircleRight>
            {/*  */}
        </StyledLogoContainer>
    );
};

export default Logo;