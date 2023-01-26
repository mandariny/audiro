import React from "react";
import '../styles/Home.css'

const Home = () =>{
    return (
        <div>
            <h1> Home</h1>
            <div className="buttons">
            <button id='naver-login'><a href={'https://www.naver.com'}><div class='link-text' id='naver-text'>네이버</div></a> </button>
            <br/>
            <button id='kakao-login'><a href={'https://www.kakao.com'}><div class='link-text'>카카오</div> </a> </button>
            <br/>
            <button id='google-login'><a href={'https://www.google.com'}><div class='link-text'>구글</div> </a> </button>
            <br/>
            </div>
        </div>
      )
};
   
export default Home;