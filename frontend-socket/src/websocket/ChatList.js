import {useRef, useState, useEffect} from "react";
import {useParams} from "react-router-dom";
import * as StompJs from "@stomp/stompjs";
import ChatThumbnailList from './ChatThumbnailList'
import axios from "axios";

const BASE_URL = "ws://localhost:8080/ws-stomp";
const REQUEST_URL = "http://localhost:8080/channel/list";
const user_id = 1;
const user_nickname = "pickapicka";

const ChatList = () => {

    const [channelList, setChannelList] = useState([]);

    const client = useRef({});

    const connect = () => {
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
        channelList.forEach((channel) => {
            client.current.subscribe(`/sub/${channel.channelId}`, (data) => {
                const subChannel = async () => {
                    console.log("sub 발생 : " + JSON.parse(data.body).content);
                    const res = await axios.get(REQUEST_URL, {params: {userId: user_id}});
                    //     .then((res)=>{
                    //     setChannelList(res.data);
                    // })
                    setChannelList(res.data);
                    console.log(res.data);
                    console.log(channelList);
                    //     res.data);
                    // setMessageList((message_list) => [
                    //     ...message_list, json_data
                    // ]);
                }
                subChannel();
            });
        });
    };

    const disconnect = () => {
        console.log("소켓 통신 종료");
        client.current.deactivate();
    };

    useEffect(() => {
        const getList = async () => {
            const res = await axios.get(REQUEST_URL, {params: {userId: user_id}});
            // .then((res)=>{
            //     setChannelList(res.data);
            //     console.log(res.data)
            // })
            setChannelList(res.data);
            // console.log(res.data);
        }
        getList();
        connect();

        return () => disconnect();
    }, []);

    return(
        <div>
            <ChatThumbnailList chatThumbnailList={channelList}/>
        </div>
    )
}
export default ChatList