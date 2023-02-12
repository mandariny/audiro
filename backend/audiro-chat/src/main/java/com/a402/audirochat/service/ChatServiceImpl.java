package com.a402.audirochat.service;

import com.a402.audirochat.dto.ChannelThumbnailDTO;
import com.a402.audirochat.dto.MessageDTO;
import com.a402.audirochat.entity.Channel;
import com.a402.audirochat.entity.ChannelMessage;
import com.a402.audirochat.entity.User;
import com.a402.audirochat.exception.ChannelNotExistException;
import com.a402.audirochat.repository.ChannelRepository;
import com.a402.audirochat.repository.UserNicknameRepository;
import com.a402.audirochat.repository.UserRepository;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Comparator;
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

    private Optional<User> getUser(long userId){
        Optional<User> user = userRepository.findById(userId);
        if(!user.isPresent()){
            User newUser = new User(userId);
            userRepository.save(newUser);
            user = userRepository.findById(userId);
        }

        log.info("유저 정보 : " + user.toString());
        return user;
    }

    private Optional<Channel> getChannel(String channelId){
        Optional<Channel> channel = channelRepository.findById(channelId);
        if(!channel.isPresent()){
            throw new ChannelNotExistException();
        }
        return channel;
    }

    private class TimeComparator implements Comparator<ChannelThumbnailDTO>{
        @Override
        public int compare(ChannelThumbnailDTO t1, ChannelThumbnailDTO t2){
            return t2.getLastMessageTime().compareTo(t1.getLastMessageTime());
        }

        @Override
        public boolean equals(Object o){
            return false;
        }
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

        Optional<Channel> channel = getChannel(channelId);
        log.info("채널 정보 확인 : " + channel.get());

        channel.get().addChannelMessage(message);
        channelRepository.save(channel.get());
        log.info("메세지를 저장했습니다. " + messageDTO.getContent());
    }

    @Override
    public List<ChannelThumbnailDTO> getChannelThumbnail(long userId) {
        Optional<User> user = getUser(userId);
        List<ChannelThumbnailDTO> channelThumbnailDTOList = user.get().getChannels().stream()
                .map(c -> ChannelThumbnailDTO.builder()
                        .channelId(c.getChannel().getId())
                        .nickname(c.getMemberNickname())
                        .lastMessage(channelRepository.findById(c.getChannel().getId()).get().getLastMessage())
                        .lastMessageTime(channelRepository.findById(c.getChannel().getId()).get().getLastMessageTime())
                        .build())
                .collect(Collectors.toList());

        channelThumbnailDTOList.sort(new TimeComparator());

        return channelThumbnailDTOList;
    }

    @Override
    public List<MessageDTO> getChannelMessages(String channelId) {

        Optional<Channel> channels = getChannel(channelId);
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
        Channel channel = new Channel();
        log.info("채널 생성!!");

        Optional<User> user1 = getUser(messageDTO.getUserId());
        Optional<User> user2 = getUser(messageDTO.getReceiverId());
        log.info("user에 채널 정보 저장");

        String nickname2 = userNicknameRepository.findUserNicknameById(messageDTO.getReceiverId());
        log.info("상대방 닉네임 확인");

        user1.get().addChannels(channel, nickname2);
        user2.get().addChannels(channel, messageDTO.getUserNickname());
        log.info("채널 인포 생성");

        userRepository.save(user1.get());
        userRepository.save(user2.get());
        log.info("유저 정보 업데이트");

        channelRepository.save(channel);
        log.info("채널 정보 저장");

        return channel.getId();
    }
}