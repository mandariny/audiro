package com.a402.audiro.postcard;

import com.a402.audiro.dto.PostcardDTO;
import com.a402.audiro.repository.PostcardRepository;
import com.a402.audiro.service.PostcardService;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
public class SmsRetryTest {
    private PostcardDTO postcardDTO;
    @Value("${naver-cloud-sms.senderPhone}")
    private String phone;
    private String passwd = "123";

    @Autowired
    private PostcardRepository postcardRepository;
    @Autowired
    private PostcardService postcardService;

    @BeforeEach
    void initPostcardDTO(){
        postcardRepository.deleteByPassword(passwd);

        postcardDTO = PostcardDTO.builder()
                .sendId(2)
                .nickname("sohee")
                .phoneNumber(phone)
                .passwd(passwd)
                .songId(1)
                .spotId(1)
                .spotName("키오스크 장소")
                .postcardImg("엽서 파일 path")
                .build();
    }

    @Test
    @DisplayName("메세지 전송 확인")
    void sendMessage(){
        postcardService.savePostcard(postcardDTO);
    }

    @Test
    @DisplayName("변경된 SmsService 구현체가 유지되는지 확인")
    void sendMessages(){
        for(int i=0; i<3; i++){
            postcardService.savePostcard(postcardDTO);
        }
    }
}
