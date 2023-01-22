import React, {useState, useRef} from "react";
import '../styles/MyGift.css';
import Modal from "../components/Modal";
import {BsHeadphones} from "react-icons/bs"
import {HiMusicNote} from "react-icons/hi";
import {FaHeart} from "react-icons/fa"

const MyGift = () => {
  const [modalOpen, setModalOpen] = useState(false);
  const outside = useRef();

  return (
    <div ref={outside} onClick={(e)=>{if(e.target==outside.current) setModalOpen(false)}}>
      <div className="mygift-container">
        <div className="mygift-title">반가워요, 연희동 아자르님 👋 </div>
        <div className="mygift-wrapper">
          <div className="mygift-profile"><BsHeadphones fill='black' size="30"/></div>
          <div className="mygift-list-wrapper">
            <div className="mygift-list-number">20</div>
            <div className="mygift-list-title">나의 엽서</div>
          </div>
          <div className="mygift-spot-wrapper">
            <div className="mygift-spot-number">20</div>
            <div className="mygift-spot-title">방문한 지점</div>
          </div>
          <div className="mygift-mate-wrapper" onClick={()=>{ setModalOpen(true) }}>
            <div className="mygift-mate-number">20</div>
            <div className="mygift-mate-title">음악 메이트</div>
          </div>
        </div>

        <div className="mygift-detail-btn-wrapper">
          <div className="mygift-detail-btn-open">비공개</div>
          <div className="mygift-detail-btn-delete">삭제하기</div>
        </div>

        <div className="mygift-detail-img"></div>

        <div className="mygift-detail-bottom-wrapper">
          <div className="mygift-detail-song-wrapper">
            <HiMusicNote fill="#6522f2" size="16"/>
            <div className="mygift-detail-singer">뉴진스</div>
            <div>-</div>
            <div className="mygift-detail-title">ditto</div>
          </div>

          <div className="mygift-detail-heart-wrapper">
            <FaHeart fill="red"/>
            <div className="mygift-detail-heart-number">21340</div>
          </div>
        </div>

        <div className="mygift-detail-reaction-wrapper">
          <div className="mygift-detail-reaction-1">
            
          </div>
          <div className="mygift-detail-reaction-1"></div>
          <div className="mygift-detail-reaction-1"></div>
          <div className="mygift-detail-reaction-1"></div>
        </div>
      </div>
      {modalOpen && <Modal className="gift-modal" setOpenModal={setModalOpen} />}
    </div>  
  );
}


export default MyGift;