import React from "react";
import { Link } from "react-router-dom";

const Nav=()=>{
    return(
        <nav>
            <div>
                <Link to="/">
                    Home
                </Link>
            </div>
            <div>
                <Link to="/mygift">
                    MyGift
                </Link>
            </div>
            <div>
                <Link to="/messenger">
                    Messenger
                </Link>
            </div>
        </nav>
    );
};

export default Nav;