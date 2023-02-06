import {GrFormClose} from 'react-icons/gr'
import React, { PropsWithChildren } from 'react';
import styled from 'styled-components';
import { useNavigate } from 'react-router-dom';

const StyledDeleteModalBackgroud=styled.div`
    position: absolute;
    height: 100vh;   
    width: 100vw;
    top: 42%; 
    backdrop-filter: brightness(50%);
    // 블러야 투명도야 lighten? darken? opacity: 0.5;
`

const StyledDeleteAlarm=styled.div`
    text-align: center;
    font-size: 15px;
    font-weight: bold;
    
    margin-bottom: 30px;
`;
const StyledDeletModal=styled.div`
    position: absolute;
    left: 15%;
    width: 200px;
    height: 120px;
    border-radius: 20px;
    background-color: #6522f2;
    padding: 20px;

`;
const StyledDeleteButtons=styled.div`
    margin-top: 40px;
    display: flex;
    justify-content: space-between;
    color: black;
    
`
const StyledDeleteButton=styled.div`
    color:black;
    background-color: white;
    border-radius: 20%;
    
`

function DeleteModal({setOpenModal}) {
    const closeDeleteModal = () => {
        setOpenModal(false);
    };
    const naviagte=useNavigate()
    const deleteGift=()=>{
      naviagte('/gifts')

    }
    return (
        <StyledDeleteModalBackgroud>
          <StyledDeletModal>
 
            <StyledDeleteAlarm >피드를 삭제하시면 해당공간에 남겨진 엽서도 삭제됩니다. 정말 삭제하시겠습니까?</StyledDeleteAlarm>
            <StyledDeleteButtons>
                
                <StyledDeleteButton onClick={closeDeleteModal}> 취소 </StyledDeleteButton>
                <StyledDeleteButton onClick={deleteGift}> 삭제 </StyledDeleteButton>
            </StyledDeleteButtons>
          </StyledDeletModal>
        </StyledDeleteModalBackgroud>
      );
}


export default DeleteModal;