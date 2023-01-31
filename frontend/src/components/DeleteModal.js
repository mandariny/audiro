import {GrFormClose} from 'react-icons/gr'
import React, { PropsWithChildren } from 'react';
import styled from 'styled-components';
import { useNavigate } from 'react-router-dom';


function DeleteModal({setOpenModal}) {
    const closeDeleteModal = () => {
        setOpenModal(false);
    };
    const naviagte=useNavigate()
    const deleteGift=()=>{
      naviagte(-1)
    }
    return (
        <div className="modalBackground">
          <div className="modalContainer">
 
            <div className="title">삭제시 기기에서도 삭제됩니다. 정말 지우시곘습니까</div>
            <div >
                <button onClick={deleteGift}> 삭제 </button>
                <button onClick={closeDeleteModal}> 취소 </button>

            </div>
          </div>
        </div>
      );
}


export default DeleteModal;