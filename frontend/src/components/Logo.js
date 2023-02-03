import React from "react";
import styled, { keyframes } from 'styled-components';
import Headset from '../assets/images/Group.png'

const StyledLogoContainer = styled.div`
    display: flex;
    flex-direction: column;
    margin-left: 35px;
    padding-bottom: 30px;
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
`;

const StyledLogoHeadset=styled.img`
    height: 24px;
    width: 24px;
    background-color: white;
    border-radius: 100%;
    margin-right: 8px;
`;

const Logo=(props)=>{   

    return(
        <StyledLogoContainer>
            <StyledLogoCircleLeft></StyledLogoCircleLeft>
            <StyledLogo>어디:로</StyledLogo>
            <StyledSubLogo>나와 새로운 사람의 음악 공간</StyledSubLogo>
            {/* {props.userId}님 */}
            {/* <StyledLogoGreet><StyledLogoHeadset src={Headset}/>{props.userId}님</StyledLogoGreet> */}
            <StyledLogoCircleRight></StyledLogoCircleRight>
        </StyledLogoContainer>
    );
};

export default Logo;