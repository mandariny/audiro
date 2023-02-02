import React, {useState, useEffect} from "react";
import "../../styles/Modal.css";
import {GrFormClose} from 'react-icons/gr'
import styled from 'styled-components';
import {Navigate, useNavigate} from 'react-router-dom';

import axios from "axios";


const StyledModalBG = styled.div`
    position: absolute;
    height: 100vh;   
    width: 100vw;
    top: 40%; 
`;

const StyledModalContainer = styled.div`
    position: absolute;
    left: 15%;
    width: 200px;
    border-radius: 20px;
    background-color: #6522f2;
    padding: 20px;
`;

const StyledModalClose = styled.div`
    display: flex;
    justify-content: flex-end;
`;

const StyledModalClostBtn = styled.div`
    background-color: transparent;
    border: none;
    font-size: 25px;
    cursor: pointer;
`;

const StyledModalTitle = styled.div`
    text-align: center;
    font-size: 20px;
    font-weight: bold;
    font-family: var(--font-nanumSquareR);
    margin-bottom: 30px;
`;  

const StyledModalListBtn = styled.div`
    text-align: center;
    font-size: 17px;
    font-weight: bold;
    font-family: var(--font-nanumSquareR);

    > *{
      color: black;
      background-color: #ffffff;
      margin-left: 20px;
      margin-right: 20px;
      padding-top: 10px;
      padding-bottom: 10px;
      border-radius: 20px;
      margin-bottom: 15px;
    }
`;

function Modal({ setOpenModal }) {

  const [mateList, setMateList] = useState([]);
  useEffect(() => {
      axios.get('http://localhost:8080/musicmate', {params: {userId: 2}})
          .then((res) => 
            setMateList(res.data))
  }, []);

  const navigate = useNavigate();

  return (
    <StyledModalBG>
      <StyledModalContainer>
        <StyledModalClose>
          <StyledModalClostBtn onClick={() => { setOpenModal(false) }}>
              <GrFormClose/>
          </StyledModalClostBtn>
        </StyledModalClose>
        <StyledModalTitle>음악메이트 목록</StyledModalTitle>
        <StyledModalListBtn>
            {mateList.map(item => <div onClick={()=>{setOpenModal(false); navigate('/gifts', {nickname: {item}})}}>{item}</div>)}
        </StyledModalListBtn>
      </StyledModalContainer>
    </StyledModalBG>
  );
}

export default Modal;