import React from 'react';
import styled from 'styled-components';
import MusicmateItem from '../components/musicmate/MusicmateItem';
import Logo from "../components/Logo";
import Nav from "../components/Nav";

import axios from 'axios';
import ProfileHeader from "../components/mygift/ProfileHeader";
import jwt from 'jwt-decode';

const StyledMMContainer = styled.div`
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    margin: 20px;
`;

const Musicmate = () => {

    const token = localStorage.getItem('login-token');
    console.log(jwt(token));
    const nickname = jwt(token)['nickName']; 
    console.log(nickname);

    return (
        <div>
            <Logo/>
            <Nav/>
            <StyledMMContainer>
                <MusicmateItem/>
            </StyledMMContainer>
        </div>
    );
};

export default Musicmate;