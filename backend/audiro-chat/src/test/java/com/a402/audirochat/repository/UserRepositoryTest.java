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

    @Test
    @DisplayName("User를 만들어보자~~")
    void createUser(){
        User user = new User();
        user.setId("sohee");
        Channel channel = new Channel();
        channel.setId("ch2");
        user.addChannels(channel);

        userRepository.save(user);
    }

    @Test
    @DisplayName("User의 채널을 찾아보자!")
    void readUser(){
        Optional<User> user = userRepository.findById("sohee");
        Assertions.assertThat(user.get().getChannelList()).contains("ch2");
    }

    @Test
    @DisplayName("User에 채널을 추가해 업데이트 하깅")
    void updateUser(){
        Optional<User> user = userRepository.findById("sohee");
        Channel channel = new Channel();
        channel.setId("ch3");
        user.get().addChannels(channel);

        userRepository.save(user.get());

        user = userRepository.findById("sohee");
        Assertions.assertThat(user.get().getChannelList()).contains("ch2", "ch3");
    }

    @Test
    @DisplayName("User 삭제!!")
    void deleteUser(){
        userRepository.deleteById("sohee");
        Assertions.assertThat(userRepository.findById("sohee")).isEqualTo(Optional.empty());
    }
}
