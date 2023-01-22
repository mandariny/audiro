import React, {useState} from "react";
import { Link } from "react-router-dom";
import '../styles/Nav.css'

const Nav=()=>{

    const items=[
        {
            title: '홈',
            link: '/'
        },
        {
            title: '나의 엽서',
            link: '/mygift'
        },
        {
            title: '편지함',
            link: '/messenger'
        },
    ];

    const [select, setSelect] = useState('홈');
    const onClicked = (type)=>{
        setSelect(type);
    }

    return(
        <nav className="nav-container">
            {items.map((item, index) => (
                <div 
                    key={index}
                    onClick={() => {
                        onClicked(item.title);
                    }}
                    className={`${select === item.title ? 'select' : ''}`}
                >
                    <Link to={item.link}>
                        {item.title}
                    </Link>
                </div>
            ))}
        </nav>
    );
};

export default Nav;