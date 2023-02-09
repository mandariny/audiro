import React from "react"

const ChatMessage = (props) => {

    return (
        <div>
            {props.nickname}
            {props.content}
            {props.userId}
            {props.contentType}
            {props.sendTime}
        </div>
    )
}

export default ChatMessage;