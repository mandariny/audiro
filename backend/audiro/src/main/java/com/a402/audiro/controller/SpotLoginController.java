package com.a402.audiro.controller;

import com.a402.audiro.dto.JwtDTO;
import com.a402.audiro.service.SpotService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.messaging.simp.SimpMessagingTemplate;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@Slf4j
@RequiredArgsConstructor
@RestController("/api/spot/token")
public class SpotLoginController {

    private final SpotService spotService;

    @GetMapping
    public ResponseEntity<?> getToken(@RequestParam long spotId){
        try{
            log.info("토큰을 조회합니다.");
            JwtDTO token = spotService.isTokenExist(spotId);
            return ResponseEntity.ok().body(token);
        }catch(Exception e){
            log.error(e.getMessage());
            return ResponseEntity.badRequest().body(e.getMessage());
        }
    }
    
    @GetMapping("/logout")
    public ResponseEntity<?> logout(@RequestParam long spotId){
        try{
            log.info("토큰을 삭제합니다.");
            spotService.eraseToken(spotId);
            return ResponseEntity.ok().body("성공");
        }catch(Exception e){
            log.error(e.getMessage());
            return ResponseEntity.badRequest().body(e.getMessage());
        }
    }

}
