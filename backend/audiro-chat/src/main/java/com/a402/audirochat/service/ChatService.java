package com.a402.audirochat.service;

import com.a402.audirochat.dto.ChannelThumbnailDTO;
import com.a402.audirochat.dto.MessageDTO;
import java.util.List;

public interface ChatService {

    void saveMessage(String channelId, MessageDTO messageDTO);

    List<ChannelThumbnailDTO> getChannelThumbnail(String userId);

    List<MessageDTO> getChannelMessages(String channelId);

    void createChannel(String user1, String user2);
}
