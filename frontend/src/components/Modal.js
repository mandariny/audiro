import React from "react";
import "../styles/Modal.css";
import {GrFormClose} from 'react-icons/gr'

function Modal({ setOpenModal }) {
  return (
    <div className="modalBackground">
      <div className="modalContainer">
        <div className="titleCloseBtn">
          <button
            onClick={() => {
              setOpenModal(false);
            }}
          >
            <GrFormClose/>
          </button>
        </div>
        <div className="title">음악메이트 목록</div>
        <div className="body">
            <div>신촌 너구리</div>
            <div>천재 개발자</div>
            <div>역삼음악대장</div>
            <div>싸버지</div>
        </div>
      </div>
    </div>
  );
}

export default Modal;