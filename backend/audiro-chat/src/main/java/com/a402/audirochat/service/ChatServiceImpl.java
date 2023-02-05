package com.a402.audirochat.service;

import com.a402.audirochat.dto.ChannelThumbnailDTO;
import com.a402.audirochat.dto.MessageDTO;
import com.a402.audirochat.entity.Channel;
import com.a402.audirochat.entity.ChannelMessage;
import com.a402.audirochat.entity.User;
import com.a402.audirochat.repository.ChannelRepository;
import com.a402.audirochat.repository.UserNicknameRepository;
import com.a402.audirochat.repository.UserRepository;
import java.util.ArrayList;
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
        // 시간순 정렬 필요
        Optional<User> user = userRepository.findById(userId);

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
    public void createChannel(String u1, String u2, String nickname) {
        // 채널 생성
        Channel channel = new Channel();

        // user에 삽입
        Optional<User> user1 = userRepository.findById(u1);
        Optional<User> user2 = userRepository.findById(u2);

        String nickname2 = userNicknameRepository.findUserNicknameById(u2);

        user1.get().addChannels(channel, nickname2);
        user2.get().addChannels(channel, nickname);

        userRepository.save(user1.get());
        userRepository.save(user2.get());
    }

    // 테스트용 메서드
    @Transactional
    public void createChannel(String u1, String u2, String nickname1, String nickname2) {
        // 채널 생성
        Channel channel = new Channel();

        // user에 삽입
        Optional<User> user1 = userRepository.findById(u1);
        Optional<User> user2 = userRepository.findById(u2);

        user1.get().addChannels(channel, nickname2);
        user2.get().addChannels(channel, nickname1);

        userRepository.save(user1.get());
        userRepository.save(user2.get());
    }
}
