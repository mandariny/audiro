package com.a402.audirochat.service;

import com.a402.audirochat.dto.MessageDTO;

public interface ChatService {

    void saveMessage(String channelId, MessageDTO messageDTO);
}
