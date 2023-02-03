package com.a402.audirochat.service;

import com.a402.audirochat.dto.ChannelThumbnailDTO;
import com.a402.audirochat.dto.MessageDTO;
import com.a402.audirochat.entity.Channel;
import com.a402.audirochat.entity.ChannelMessage;
import com.a402.audirochat.entity.User;
import com.a402.audirochat.repository.ChannelRepository;
import com.a402.audirochat.repository.UserRepository;
import java.util.ArrayList;
import java.util.List;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.Optional;

@Service
@RequiredArgsConstructor
public class ChatServiceImpl implements ChatService{

    private final UserRepository userRepository;
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

    @Override
    public List<ChannelThumbnailDTO> getChannelThumbnail(String userId) {
        Optional<User> user = userRepository.findById(userId);


        return null;
    }

    @Override
    public List<MessageDTO> getChannelMessages(String channelId) {
        return null;
    }

    @Override
    public void createChannel(String user1, String user2) {

    }
}
