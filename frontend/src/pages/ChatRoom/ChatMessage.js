import React from "react"

const ChatMessage = (props) => {

    const StringMessage = (props) => {
        return (
            <div>
                {props.nickname + " : "}
                {props.content}
                {/* {props.user_id} */}
                {/* {props.content_type} */}
                {props.send_time}
            </div>
        )
    }

    // 이미지인 경우엔 http~~~하는 이미지 주소를 보여주게끔,,,
    const ImageMessage = (props) => {
        return(
            <div>
            {props.nickname + " : "}
            <img alt="이미지 메세지" src={props.content}/>
            {/* {props.user_id} */}
            {/* {props.content_type} */}
            {props.send_time}
        </div>
        )
    }

    // 메세지인 경우와 이미지인 경우로 나누어서 표현
    if(props.content_type == 'MESSAGE'){
        return (
            <StringMessage
                user_id={props.user_id}
                nickname={props.nickname}
                content_type={props.content_type}
                content={props.content}
                send_time={props.send_time}
            />
        )
    }
    return (
        <ImageMessage
            user_id={props.user_id}
            nickname={props.nickname}
            content_type={props.content_type}
            content={props.content}
            send_time={props.send_time}
        />
    )
}

export default ChatMessage;