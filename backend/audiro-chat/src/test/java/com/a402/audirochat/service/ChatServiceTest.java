package com.a402.audirochat.service;

import com.a402.audirochat.dto.ChannelThumbnailDTO;
import com.a402.audirochat.dto.MessageDTO;
import com.a402.audirochat.entity.Channel;
import com.a402.audirochat.entity.ContentType;
import com.a402.audirochat.repository.ChannelRepository;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;

@SpringBootTest
public class ChatServiceTest {

    @Autowired
    private ChatService chatService;

    @Autowired
    private ChannelRepository channelRepository;

    @Test
    @DisplayName("메세지 저장 테스트")
    void saveMessageTest(){
        for(int i=1; i<=5; i++){
            MessageDTO messageDTO = MessageDTO.builder()
                    .userId("user1")
                    .userNickname("sohee")
                    .contentType(ContentType.MESSAGE)
                    .content("message~~~~~~~~안녕 ㅎㅎ")
                    .sendTime(LocalDateTime.now())
                    .build();
            chatService.saveMessage("ch"+i, messageDTO);
        }

        Optional<Channel> channel = channelRepository.findById("ch1");
        Assertions.assertThat(channel.get().getLastMessage()).isEqualTo("message~~~~~~~~안녕 ㅎㅎ");
    }

    @Test
    @DisplayName("getChannelThumbnail 테스트")
    void getChannelThumbnailTest(){
        List<ChannelThumbnailDTO> channelThumbnailDTOList = chatService.getChannelThumbnail("user1");
        Assertions.assertThat(channelThumbnailDTOList.size()).isEqualTo(5);
    }

    @Test
    @DisplayName("getChannelMessages 테스트")
    void getChannelMessagesTest(){
        List<MessageDTO> messageDTOList = chatService.getChannelMessages("ch1");
        Assertions.assertThat(messageDTOList.get(0).getContent()).isEqualTo("message~~~~~~~~안녕 ㅎㅎ");
    }
}
