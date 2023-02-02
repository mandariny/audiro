package com.a402.audirochat.service;

import com.a402.audirochat.dto.MessageDTO;
import com.a402.audirochat.entity.Channel;
import com.a402.audirochat.entity.ChannelMessage;
import com.a402.audirochat.repository.ChannelRepository;
import lombok.RequiredArgsConstructor;

import java.util.Optional;

@RequiredArgsConstructor
public class ChatServiceImpl implements ChatService{

    private final ChannelRepository channelRepository;

    @Override
    public void saveMessage(String channelId, MessageDTO messageDTO) {
        ChannelMessage message = ChannelMessage.builder()
                .userId(messageDTO.getUserId())
                .userNickname(messageDTO.getUserNickname())
                .contentType(messageDTO.getContentType())
                .content(messageDTO.getContent())
                .sendTime(messageDTO.getSendTime())
                .build();
        Optional<Channel> channel = channelRepository.findById(channelId);
        channel.get().addChannelMessage(message);

        channelRepository.save(channel.get());
    }
}
