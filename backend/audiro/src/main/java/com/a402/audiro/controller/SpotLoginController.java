package com.a402.audiro.controller;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.messaging.simp.SimpMessagingTemplate;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@Slf4j
@RequiredArgsConstructor
@RestController
public class SpotLoginController {

    private final SimpMessagingTemplate template;

    @GetMapping("/login/spot")
    public void sendMessage(long spotId, String token){
      template.convertAndSend("/sub/spot/" + spotId, token);
      log.info("토큰 전송이 완료되었습니다 : " + token);
    }
}
