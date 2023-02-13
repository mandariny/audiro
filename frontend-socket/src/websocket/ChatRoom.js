import {useRef, useState, useEffect} from "react";
import {useParams} from "react-router-dom";
import * as StompJs from "@stomp/stompjs";
import ChatMessageList from './ChatMessageList';
import axios from "axios";

const BASE_URL = "ws://localhost:8080/ws-stomp";
const REQUEST_URL = "http://localhost:8080/message";
const user_id = 1;
const user_nickname = "pickapicka";

const ChatRoom = () => {

    const [messageList, setMessageList] = useState([]);
    const [message, setMessage] = useState('');

    const {channel_id} = useParams();
    // const channel_id = "ch1";
    const client = useRef({});

    const connect = () => {
        console.log("id: "+channel_id);
        client.current = new StompJs.Client({
            brokerURL: BASE_URL,
            onConnect: () => {
                console.log("소켓 연결 성공!");
                subscribe();
            },
        });
        client.current.activate();
    };

    const subscribe = () => {
        console.log("subscribe 시작");
        client.current.subscribe(`/sub/${channel_id}`, (data) => {
            const json_data = JSON.parse(data.body);
            console.log(json_data);
            console.log("전송된 데이터 : " + json_data.content);
            setMessageList((message_list) => [
                ...message_list, json_data
            ]);
        });
    };

    const publish = (message) => {
        if(!client.current.connected) return;

        console.log(message);

        client.current.publish({
            destination: `/pub/channel/${channel_id}`,
            body: JSON.stringify({
                userId: user_id,
                userNickname: user_nickname,
                contentType: "MESSAGE",
                content: message
            }),
        });

        setMessage('');
    };

    const disconnect = () => {
        client.current.deactivate();
    };

    const handleChange = (event) => {
        setMessage(event.target.value);
    };

    const handleSubmit = (event, message) => {
        event.preventDefault();

        publish(message);
    };

    useEffect(() => {
        connect();

        axios.get(REQUEST_URL, {params: {channelId: channel_id}})
            .then((res)=>{
                setMessageList(res.data);
                // console.log(res.data);
            })
            .catch(error => {
                console.log(error.response);
            })

        return () => disconnect();
    }, []);

    return (
        <div>
            <ChatMessageList messageList={messageList}/>
            <form onSubmit={(event) => handleSubmit(event, message)}>
                <div>
                    <input type={'text'} name={'chatInput'} onChange={handleChange} value={message} />
                </div>
                <input type={'submit'} value={'전송'} />
            </form>
        </div>
    );
}
export default ChatRoom;