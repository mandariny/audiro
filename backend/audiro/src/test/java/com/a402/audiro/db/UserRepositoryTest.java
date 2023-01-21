package com.a402.audiro.db;

import com.a402.audiro.entity.User;
import com.a402.audiro.repositories.UserRepository;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
public class UserRepositoryTest {

    @Autowired
    UserRepository userRepository;

    @Test
    @DisplayName("User 테이블 정보 저장 확인")
    void userTableSaveCheck(){
        User user = new User("sohee3", "123456567889", "sohee3 닉네임");
        userRepository.save(user);
    }

    @Test
    @DisplayName("UserRepository findByNickname 확인")
    void userRepositoryFindByNicknameCheck(){
        User user = userRepository.findByNickname("sohee");
        Assertions.assertThat(user.getName()).isEqualTo("sohee");
    }
}
