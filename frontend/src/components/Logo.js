import React from "react";
import '../styles/Logo.css';
import styled from 'styled-components';
import Group from '../assets/images/Group.png'
import Headset from '../assets/images/Group.png'

const StyledLogoContainer=styled.div`
    display: flex;
    flex-direction: column;
    margin-left: 35px;
    padding-bottom: 30px;
    padding-top: 20px;
`
const StyledLogoCircleLeft=styled.div`
    position: absolute;
    top: 35px;
    left: 25px;
    z-index: -99;
    width: 27px;
    height: 27px;
    background-color: rgba(101, 34, 242, 0.56);
    border-radius: 100%;
`
const StyledLogoText=styled.div`
    font-size: 40px;
    font-family: var(--font-nanumSquareEB);
`

const StyledLogoSub=styled.div`
    position:absolute;
    top: 20px;
    left: 120px;
    z-index: -99;
    width: 70px;
    height: 70px;
    background-color: rgba(101, 34, 242, 0.56);
    border-radius: 100%;
`
const StyledLogoGreet=styled.div`
    display: flex;
    justify-content: end;
    margin-right: 15px;
`
const StyledLogoHeadset=styled.img`
    height: 24px;
    width: 24px;
    background-color: white;
    border-radius: 100%;
    margin-right: 8px
`

const Logo=(props)=>{   
    const cur=window.location.href
    if (cur=='http://localhost:3000/intro'){
        return null;
    }

    return(
        <StyledLogoContainer >
            <StyledLogoCircleLeft/>
            <StyledLogoText >어디:로</StyledLogoText>
            나와 새로운 사람의 음악 공간<StyledLogoSub/>
            <StyledLogoGreet><StyledLogoHeadset src={Headset}/>{props.userId}님</StyledLogoGreet>
           
        </StyledLogoContainer>
    );
};

export default Logo;