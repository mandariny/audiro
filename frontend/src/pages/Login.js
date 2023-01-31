import React from "react";
import '../styles/Home.css'
import styled from 'styled-components';
import naver_logo from '../assets/images/naver_logo.png'

const Home = () =>{

    return (
        <div>
            <h1> 로그인</h1>
            <div className="buttons">
            <button id='naver-login'><a href={'https://www.naver.com'}><img src={naver_logo}/>네이버로 로그인하기</a> </button>
            <br/>
            <button id='kakao-login'><a href={'https://www.kakao.com'}><div class='link-text'>카카오로 로그인하기</div> </a> </button>
            <br/>
            <button id='google-login'><a href={'https://www.google.com'}><div class='link-text'>구글로 로그인하기</div> </a> </button>
            <br/>
            </div>

        </div>
      )
};
   
export default Home;