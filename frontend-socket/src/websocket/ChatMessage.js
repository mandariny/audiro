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