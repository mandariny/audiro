package com.a402.audiro.service;

import com.a402.audiro.dto.PostcardDTO;
import com.a402.audiro.dto.PostcardDetailDTO;
import com.a402.audiro.exception.PasswordDuplicationException;
import java.time.LocalDateTime;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
public class PostcardServiceTest {

    @Autowired
    PostcardService postcardService;

    @Test
    @DisplayName("비밀번호 중복 검사 - PasswordDuplicationException")
    void passwordDuplicationCheck(){
        Assertions.assertThrows(PasswordDuplicationException.class, () ->{
           postcardService.isValidPassword("ㅎㅎㅎㅎㅎ");
        });
    }

    @Test
    @DisplayName("비밀번호 중복 검사 - pass")
    void passwordPassCheck(){
        postcardService.isValidPassword("ㅎㅎㅎㅎㅎㅋㅋㅋㅋㅋ");
    }

    @Test
    @DisplayName("포스트카드 저장")
    void savePostcard(){
        PostcardDTO postcardDTO = new PostcardDTO(1, "sohee", "111122223333", "1234", 1, 1, "멀캠점", "포스트카드 이미지 주소",
                LocalDateTime.now(), "message");

        postcardService.savePostcard(postcardDTO);
    }

    @Test
    @DisplayName("포스트 카드 정보 받기")
    void getPostcardDetail(){
        PostcardDetailDTO postcardDetailDTO = postcardService.getPostcardDetail(1);

        System.out.println(postcardDetailDTO.toString());
    }
}