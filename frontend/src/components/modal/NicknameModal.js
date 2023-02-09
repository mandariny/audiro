import React, { useState } from 'react'
import styled from 'styled-components';
import axios from 'axios'
const StyeldNicknameModal=styled.div`
    
`;

const NicknameModal = (props) => {

    const [newNickname,setNewNickname]=useState('')
    const onChange=(e)=>{    
        setNewNickname(e.target.value)
        setNewNickname(e.target.value)
        console.log(newNickname)
        console.log(e.target.value)
        }
    
    const token=localStorage.getItem('login-token')

    const submitHandler=(e)=>
    {
        e.preventDefault()
    }    

    const ChangeNickname=(e)=> {
        console.log("newNickName")
        console.log(newNickname)
        axios.post('http://i8a402.p.ssafy.io:80/api/user/change-nickname', 
        {
            method:'POST',
            headers: {Auth: `${token}`},
            newNickName:`${newNickname}`
        })
        .then ((res)=>{
            console.log("결과 받기")
            console.log(res);
            console.log(res.Headers.Refresh);
            const jwtToken=res.Headers.Refresh;
            localStorage.setItem('login-token', jwtToken);
            console.log('success');
        })
        .catch((err=>{
            console.log(err.data)
        }))
    }

    return (
        <StyeldNicknameModal>
       
            <form onSubmit={submitHandler}>
                <input onChange={onChange} value={newNickname}  type='text'/> 
                <button type='button' onClick={ChangeNickname}>닉네임 변경</button>
            </form>
        </StyeldNicknameModal>
    );
};

export default NicknameModal;
