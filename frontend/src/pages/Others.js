import React from 'react';
import styled from 'styled-components';
import {useParams} from 'react-router-dom'

const OthersBackground=styled.div`
    position: absolute;
    height: 100vh;   
    width: 100vw;
    top: 20%; 
    backdrop-filter: brightness(50%);
    // 블러야 투명도야 lighten? darken? opacity: 0.5;
    display:flex;
    justify-content:center;
    align-itmes:center;
`

const OthersMateButton=styled.button`
    background-color: #6522f2;
    border-radius:20px;
    position: absolute;
    top:40%;
    width:248px;
    height:73px;
    font-weight: bold;
    font-family: var(--font-nanumSquareR);
`

const Others = () => {
    const {giftid}=useParams()
    console.log(giftid)   
    return (
        <OthersBackground>
            <div>
            다른 사람 페이지입니다<br/>
            {giftid}님 페이지입니다.
            </div>

            <OthersMateButton>음악 메이트 신청하기</OthersMateButton>
              
        </OthersBackground>
    );
};

export default Others;