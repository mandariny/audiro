import React from "react";
import '../styles/Logo.css';
import styled from 'styled-components';
import Group from '../assets/images/Group.png'
import Headset from '../assets/images/headset.png'

const Logo=(props)=>{   
    const cur=window.location.href
    if (cur=='http://localhost:3000/intro'){
        return null;
    }

    return(
        <div className="logo-container">
            <div className="logo-circle-left"></div>
            <div className="logo">어디:로</div>
            <div className="sub-logo">나와 새로운 사람의 음악 공간</div>
            안녕하세요 {props.userId}님
            <div className="logo-circle-right"></div>
        </div>
    );
};

export default Logo;