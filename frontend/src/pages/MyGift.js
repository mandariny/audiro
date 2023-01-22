import React, {useState, useRef} from "react";
import '../styles/MyGift.css';
import Modal from "../components/Modal";

const MyGift = () => {
  const [modalOpen, setModalOpen] = useState(false);
  const outside = useRef();

  return (
    <div ref={outside} onClick={(e)=>{if(e.target==outside.current) setModalOpen(false)}}>
      <h1>MyGift</h1>
      <button onClick={()=>{ setModalOpen(true) }}> Open </button>
      {modalOpen && <Modal setOpenModal={setModalOpen} />}
    </div>  
  );
}


export default MyGift;