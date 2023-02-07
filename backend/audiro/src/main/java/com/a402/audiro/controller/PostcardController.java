package com.a402.audiro.controller;

import com.a402.audiro.dto.PasswordDTO;
import com.a402.audiro.dto.PostcardDTO;
import com.a402.audiro.exception.PasswordDuplicationException;
import com.a402.audiro.service.PostcardService;
import com.a402.audiro.service.SmsService;
import javax.transaction.Transactional;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequiredArgsConstructor
@CrossOrigin("*")
@RequestMapping("/postcard")
@Slf4j
public class PostcardController {

    private final PostcardService postcardService;
    private final SmsService smsService;

    @PostMapping
    @Transactional
    public ResponseEntity<?> sendPostcard(@RequestBody PostcardDTO postcardDTO){
        try{
            postcardService.savePostcard(postcardDTO);
            smsService.sendMessage(postcardDTO);

            return ResponseEntity.ok().body("sucess: 메세지를 성공적으로 전송했습니다.");

        }catch(Exception e){
            log.error(e.getMessage());
            return ResponseEntity.badRequest().body(e.getMessage());
        }
    }

    @PostMapping("/pw")
    public ResponseEntity<?> passwordValidationCheck(@RequestBody PasswordDTO passwordDTO){
        try{
            postcardService.isValidPassword(passwordDTO.getPasswd());
            return ResponseEntity.ok().body("success: 사용 가능한 암호입니다.");
        }catch (Exception e){
            log.error(e.getMessage());
            return ResponseEntity.badRequest().body(e.getMessage());
        }
    }
}
