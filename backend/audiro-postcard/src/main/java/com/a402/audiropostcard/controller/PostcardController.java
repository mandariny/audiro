package com.a402.audiropostcard.controller;

import com.a402.audiropostcard.dto.PasswordDTO;
import com.a402.audiropostcard.dto.PostcardDTO;
import com.a402.audiropostcard.exception.PasswordDuplicationException;
import com.a402.audiropostcard.service.PostcardService;
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

    @PostMapping()
    @Transactional
    public ResponseEntity<?> sendMessage(@RequestBody PostcardDTO postcardDTO){
        try{
            postcardService.savePostcard(postcardDTO);
            postcardService.sendMessage(postcardDTO);

            return ResponseEntity.ok().body("sucess: send a message");

        }catch(Exception e){
            log.error(e.getMessage());
            return ResponseEntity.badRequest().body(e.getMessage());
        }
    }

    @PostMapping("/pw")
    public ResponseEntity<?> passwordValidationCheck(@RequestBody PasswordDTO passwordDTO){
        try{
            postcardService.isValidPassword(passwordDTO);
            return ResponseEntity.ok().body("success");
        }catch(PasswordDuplicationException e){
            log.error(e.getMessage());
            return ResponseEntity.badRequest().body(e.getMessage());
        }catch (Exception e){
            log.error(e.getMessage());
            return ResponseEntity.badRequest().body(e.getMessage());
        }
    }
}
