package com.a402.audirochat.service;

import com.a402.audirochat.dto.ChannelThumbnailDTO;
import com.a402.audirochat.dto.MessageDTO;
import com.a402.audirochat.entity.Channel;
import com.a402.audirochat.entity.ChannelMessage;
import com.a402.audirochat.entity.User;
import com.a402.audirochat.repository.ChannelRepository;
import com.a402.audirochat.repository.UserNicknameRepository;
import com.a402.audirochat.repository.UserRepository;

import java.util.List;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.Optional;
import java.util.stream.Collectors;

@Slf4j
@Service
@RequiredArgsConstructor
public class ChatServiceImpl implements ChatService{

    private final UserRepository userRepository;
    private final ChannelRepository channelRepository;
    private final UserNicknameRepository userNicknameRepository;

    private Optional<User> getUser(String userId){
        Optional<User> user = userRepository.findById(userId);
        if(!user.isPresent()){
            User newUser = new User(userId);
            userRepository.save(newUser);
            user = userRepository.findById(userId);
        }
        return user;
    }

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

        log.info("채널 정보 : " + channel.get().toString());

        channel.get().addChannelMessage(message);
        channelRepository.save(channel.get());
        log.info("메세지를 저장했습니다. " + messageDTO.getContent());
    }

    @Override
    public List<ChannelThumbnailDTO> getChannelThumbnail(String userId) {

        Optional<User> user = getUser(userId);

        return user.get().getChannels().stream()
                .map(c -> ChannelThumbnailDTO.builder()
                        .channelId(c.getChannel().getId())
                        .nickname(c.getMemberNickname())
                        .lastMessage(c.getChannel().getLastMessage())
                        .build())
                .collect(Collectors.toList());
    }

    @Override
    public List<MessageDTO> getChannelMessages(String channelId) {

        Optional<Channel> channels = channelRepository.findById(channelId);
        return channels.get().getMessages().stream()
                .map(m -> MessageDTO.builder()
                        .userId(m.getUserId())
                        .userNickname(m.getUserNickname())
                        .contentType(m.getContentType())
                        .content(m.getContent())
                        .sendTime(m.getSendTime())
                        .build())
                .collect(Collectors.toList());
    }

    @Transactional
    @Override
    public String createChannel(MessageDTO messageDTO) {
        // 채널 생성
        Channel channel = new Channel();

        // user에 삽입
        Optional<User> user1 = getUser(messageDTO.getUserId());
        Optional<User> user2 = getUser(messageDTO.getReceiverId());

        String nickname2 = userNicknameRepository.findUserNicknameById(messageDTO.getReceiverId());

        user1.get().addChannels(channel, nickname2);
        user2.get().addChannels(channel, messageDTO.getUserNickname());

        userRepository.save(user1.get());
        userRepository.save(user2.get());

        return channel.getId();
    }
}
