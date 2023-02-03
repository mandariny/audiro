package com.a402.audirochat.repository;

import com.a402.audirochat.entity.Channel;
import com.a402.audirochat.entity.User;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import java.util.Optional;

@SpringBootTest
public class UserRepositoryTest {

    @Autowired
    UserRepository userRepository;

    @Autowired
    ChannelRepository channelRepository;

    @Test
    @DisplayName("User 2명 만들고 서로 채팅방 5개 들어가있기")
    void create2User(){
        int arr[] = {2, 1};
        for(int i=0; i<2; i++){
            User user = new User();
            user.setId("user"+(i+1));
            for(int j=0; j<5; j++){
                Optional<Channel> channel = channelRepository.findById("ch"+(j+1));
                user.addChannels(channel.get(), "user"+arr[i]);
            }
            userRepository.save(user);
        }
    }

    @Test
    @DisplayName("User를 만들어보자~~")
    void createUser(){
        User user = new User();
        user.setId("sohee");
        Channel channel = new Channel();
        channel.setId("ch2");
        user.addChannels(channel, "sohee_friend");

        userRepository.save(user);
    }

    @Test
    @DisplayName("User의 채널을 찾아보자!")
    void readUser(){
        Optional<User> user = userRepository.findById("sohee");
        System.out.println(user.toString());
    }

    @Test
    @DisplayName("User에 채널을 추가해 업데이트 하깅")
    void updateUser(){
        Optional<User> user = userRepository.findById("sohee");
        Channel channel = new Channel();
        channel.setId("ch3");
        user.get().addChannels(channel, "sohee_friend2");

        userRepository.save(user.get());

        user = userRepository.findById("sohee");
        Assertions.assertThat(user.get().getChannels().get(1).getMemberNickname()).isEqualTo("sohee_friend2");
    }

    @Test
    @DisplayName("User 삭제!!")
    void deleteUser(){
        userRepository.deleteById("sohee");
        Assertions.assertThat(userRepository.findById("sohee")).isEqualTo(Optional.empty());
    }
}
