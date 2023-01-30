import React, {useState, useRef} from "react";
import '../styles/MyGift.css';
import Modal from "../components/Modal";
import {BsHeadphones} from "react-icons/bs"
import {HiMusicNote} from "react-icons/hi";
import {FaHeart} from "react-icons/fa"
import fun from '../assets/images/fun.png';
import love from '../assets/images/love.png';
import sad from '../assets/images/sad.png';
import wow from '../assets/images/wow.png';
import {useParams} from 'react-router-dom'
import song from '../assets/audio/Ditto.mp3';
import DeleteModal from "../components/DeleteModal";
import styled from 'styled-components';

const MyGift = () => {
  const [modalOpen, setModalOpen] = useState(false);
  const [deleteModalOpen, setDeleteModalOpen] = useState(false);
  const outside = useRef();
  const {giftid}=useParams()
  console.log([deleteModalOpen, setDeleteModalOpen])
  return (
    <div ref={outside} onClick={(e)=>{if(e.target==outside.current) setModalOpen(false)
    
    
    }}>
      <div className="mygift-container">
        <div className="mygift-title">반가워요, 연희동 아자르님 👋 {giftid}번째 글입니다. </div>
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
          <div className="mygift-detail-btn-delete" onClick={()=>{ setDeleteModalOpen(true)
          console.log(deleteModalOpen)
          }} >삭제하기</div>
        </div>

        <div className="mygift-detail-img"></div>
        <image> </image>

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
        <audio controls>
          <source src={song} type="audio/mpeg"></source>
        </audio>
        <iframe width="560" height="315" src="https://www.youtube.com/embed/pSUydWEqKwE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

        <div className="mygift-detail-reaction-wrapper">
          <div className="mygift-detail-reaction">
            <img src={love} height="35px" width="35px"/>
            <div className="mygift-detail-reaction-number">2301</div>
          </div>
          <div className="mygift-detail-reaction">
            <img src={sad} height="35px" width="35px"/>
            <div className="mygift-detail-reaction-number">12</div>
          </div>
          <div className="mygift-detail-reaction">
            <img src={wow} height="35px" width="35px"/>
            <div className="mygift-detail-reaction-number">3</div>
          </div>
          <div className="mygift-detail-reaction">
            <img src={fun} height="35px" width="35px"/>
            <div className="mygift-detail-reaction-number">200</div>
          </div>
        </div>
      </div>
      {modalOpen && <Modal className="gift-modal" setOpenModal={setModalOpen} />}
      {deleteModalOpen&& <DeleteModal setOpenModal={setDeleteModalOpen}/>}
      
    </div>  
  );
  
}


export default MyGift;