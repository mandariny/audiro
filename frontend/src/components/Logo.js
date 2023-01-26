import React from "react";
import '../styles/Logo.css';

const Logo=()=>{

    return(
        <div className="logo-container">
            <div className="logo-circle-left"></div>
            <div className="logo">어디:로</div>
            <div className="sub-logo">나와 새로운 사람의 음악 공간</div>
            <div className="logo-circle-right"></div>
        </div>
    );
};

export default Logo;