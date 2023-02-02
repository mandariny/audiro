package com.a402.audirochat.controller;

import com.a402.audirochat.dto.MessageDTO;
import com.a402.audirochat.service.ChatService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.messaging.handler.annotation.DestinationVariable;
import org.springframework.messaging.handler.annotation.MessageMapping;
import org.springframework.messaging.handler.annotation.SendTo;
import org.springframework.stereotype.Controller;

@Slf4j
@RequiredArgsConstructor
@Controller
public class ChatController {

    private final ChatService chatService;

    @MessageMapping("/{channel}/message")
    @SendTo("/sub/{channel}")
    public MessageDTO sendMessage(String userId, @DestinationVariable("channel") String channelId, MessageDTO messageDTO){
        chatService.saveMessage(channelId, messageDTO);
        return messageDTO;
    }
}
