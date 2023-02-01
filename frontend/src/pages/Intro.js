import React from 'react';
import {Link} from 'react-router-dom'
const Intro = () => {
    return (
        <div>
            <div className="logo-container">
            취향 저격 음악 마니또
            <div className="logo-circle-left"></div>
            <div className="logo">어디:로</div>
            <div className="sub-logo">나와 새로운 사람이 음악으로 연결되는 공간</div>

            <div className="logo-circle-right"></div>
        </div>

            <Link to='/login'> 로그인 하기 </Link>
        </div>
    );
};

export default Intro;