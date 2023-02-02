import React, {useState, useRef} from "react";
import {Link} from "react-router-dom";

import Modal from "../components/modal/Modal";
import {BsHeadphones} from "react-icons/bs"
import {HiMusicNote} from "react-icons/hi";

import styled from 'styled-components';
import Logo from "../components/Logo";
import Nav from "../components/Nav";
import style from "react-awesome-modal/lib/style";

const StyledHeader = styled.div`
    margin-top: 20px;
    margin-left: 10px;
    margin-right: 10px;
    position: relative;
`;

const StyledMyGiftTitle = styled.div`
    font-size: 17px;
    font-family: var(--font-nanumSquareEB);
    margin-bottom: 25px;
    margin-left: 10px;
    color: white;
`;

const StyledMyGiftHeaderWrapper = styled.div`
    display: flex;
    justify-content: space-around;
    margin-bottom: 60px;
    margin-left: 10px;
    margin-right: 10px;
`;

const StyledMyGiftProfile = styled.div`
    height: 40px;
    width: 40px;
    border-radius: 100%;
    background-color: white;
    display: flex;
    justify-content:center;
    align-items: center;
`;

const StyledMyGiftListNumber = styled.div`
    text-align: center;
    margin-bottom: 10px;
    font-size: 18px;
    font-family: var(--font-nanumSquareEB);
    color: white;
`;

const StyledMyGiftListTitle = styled.div`
    text-align: center;
    font-size: 13px;
    font-family: var(--font-nanumSquareR);
    color: white;
`;

const StyledMyGiftListWrapper=styled.div`
    display: flex;
    justify-content: center;
    align-items: center;
`;

const StyledMyGiftList = styled.div`
    margin-left: 10px;
    margin-right: 10px;
    display: grid;
    grid-template-columns: 1fr 1fr;
    column-gap: 5px;
    row-gap: 5px;
`;


const StyledMateModal = styled.div`
    position: absolute;
    top: 50%;
`

const GiftList = () =>{
    const [modalOpen, setModalOpen] = useState(false);

    return (
        <div>
            <Logo/>
            <Nav/>
            <StyledHeader>
                <StyledMyGiftTitle>반가워요, 연희동 아자르님 👋 </StyledMyGiftTitle>

                <StyledMyGiftHeaderWrapper>
                    <StyledMyGiftProfile><BsHeadphones fill='black' size="30"/></StyledMyGiftProfile>
                    <div>
                        <StyledMyGiftListNumber>20</StyledMyGiftListNumber>
                        <StyledMyGiftListTitle>나의 엽서</StyledMyGiftListTitle>
                    </div>
                    <div>
                        <StyledMyGiftListNumber>20</StyledMyGiftListNumber>
                        <StyledMyGiftListTitle>방문한 지점</StyledMyGiftListTitle>
                    </div>
                    <div onClick={()=>{ setModalOpen(true) }}>
                        <StyledMyGiftListNumber>20</StyledMyGiftListNumber>
                        <StyledMyGiftListTitle>음악 메이트</StyledMyGiftListTitle>
                    </div>
                </StyledMyGiftHeaderWrapper>
            </StyledHeader>

            <StyledMyGiftListWrapper>
                <StyledMyGiftList>
                    <Link to="/gifts/1"><img src='https://media.discordapp.net/attachments/1056882470429138968/1068086212054745118/love1.jpg' height={105} width={170} /></Link>
                    <Link to="/gifts/2"><img src='https://cdn.discordapp.com/attachments/1056882470429138968/1068086212272861245/love2.jpg' height={105} width={170} /></Link>
                    <Link to="/gifts/3"><img src='https://media.discordapp.net/attachments/1056882470429138968/1068086212444819486/love3.jpg' height={105} width={170} /></Link>
        
                    <Link to="/gifts/4"><img src='https://cdn.discordapp.com/attachments/1056882470429138968/1068086212650336297/love4.jpg' height={105} width={170} /></Link>
                    <Link to="/gifts/5"><img src='https://cdn.discordapp.com/attachments/1056882470429138968/1068081563310506014/Notes_230126_170914.jpg' height={105} width={170} /></Link>
                    <Link to="/gifts/6"><img src='https://cdn.discordapp.com/attachments/1056882470429138968/1068086212876841020/love5.jpg' height={105} width={170} /></Link>
            
                    <Link to="/gifts/7"><img src='https://shop2.daumcdn.net/thumb/R500x500/?fname=http%3A%2F%2Fshop2.daumcdn.net%2Fshophow%2Fp%2FZ20293623281.jpg%3Fut%3D20221209092821' height={105} width={170} /></Link>
                    <Link to="/gifts/8"><img src='http://www.akbobada.com/home/akbobada/archive/akbo/img/202212200942036.jpg' height={105} width={170} /></Link>
                    <Link to="/gifts/9"><img src='https://image.bugsm.co.kr/album/images/200/40824/4082425.jpg?version=20230105002539.0' height={105} width={170} /></Link>
                </StyledMyGiftList>
            </StyledMyGiftListWrapper>
            <StyledMateModal>{modalOpen && <Modal setOpenModal={setModalOpen} />}</StyledMateModal>
        </div>
      )
};
   
export default GiftList;