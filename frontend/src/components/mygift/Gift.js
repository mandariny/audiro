import React, {useState, useRef, useEffect} from "react";
import { Link } from "react-router-dom";
import styled from 'styled-components';

const Gift = (props) => {
  
  return (
    <div>
        <Link to={`/gifts/${props.id}`}><img src={props.src} height={105} width={170}/></Link>
    </div>
  );
  
}


export default Gift;