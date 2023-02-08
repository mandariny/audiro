import React, {useEffect, useState, useParams} from 'react';
import Logo from '../components/Logo';
import Nav from '../components/Nav';

const Home = (location) => {

    const [token, setToken] = useState();

    useEffect(() => {
        const params = new URLSearchParams(location.search);
        // console.log(window.location);
        const jwtToken = params.get("auth");
        // console.log(jwtToken);
        setToken(jwtToken);
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