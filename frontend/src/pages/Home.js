import React, {useEffect, useState, useParams} from 'react';
import Logo from '../components/Logo';
import Nav from '../components/Nav';

import jwt from 'jwt-decode';
const Home = () => {

    const [token, setToken] = useState();

    useEffect(() => {
        const params = new URLSearchParams(window.location.search);
        console.log(window.location);
        console.log(window.location.search);
        const jwtToken = params.get("auth");
        console.log(jwtToken);
        setToken(jwtToken);
        localStorage.setItem('login-token', jwtToken);
        console.log("parsing");
        //console.log(jwt(token));
        //console.log(jwt(token["ninkName"]));
    }, [])

    return (
        <div>
            <Logo/>
            <Nav/>
            홈 서비스 소개
            {token}
        </div>
    );
};

export default Home;