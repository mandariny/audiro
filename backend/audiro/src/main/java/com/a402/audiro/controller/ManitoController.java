package com.a402.audiro.controller;

import com.a402.audiro.dto.GiftThumbnailDTO;
import com.a402.audiro.dto.ManitoDTO;
import com.a402.audiro.dto.ManitoImagePairDTO;
import com.a402.audiro.service.ManitoService;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.io.DataInput;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import lombok.Builder;
import lombok.Data;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import org.springframework.web.multipart.MultipartFile;

@RestController
@RequestMapping("api/manito")
@CrossOrigin(origins = "*")
@RequiredArgsConstructor
@Builder
@Slf4j
public class ManitoController {

    private final ManitoService manitoService;

    private final String UPLOADED_FOLDER = "C:\\Users\\SSAFY\\Desktop\\Git-space\\S08P12A402\\backend\\gift_images\\";

    @GetMapping
    public ResponseEntity<?> getManitoList(){
        try{
            log.info("마니또 리스트 요청을 받았습니다.");
            List<ManitoImagePairDTO> manitoImagePairDTOS = manitoService.getManitoImagePairList();
            return ResponseEntity.ok().body(manitoImagePairDTOS);
        }catch (Exception e){
            return ResponseEntity.badRequest().body(e.getMessage());
        }
    }

    @PostMapping
    public ResponseEntity<?> addManito(@RequestParam(value = "giftImg") MultipartFile giftImg, @RequestParam(value ="manito", required = true) String manito){
        try{
            log.info("새로운 마니또가 들어왔습니다. 마니또 정보 : {}", manito);
            //해당 경로에 manito 이미지 저장
            byte[] bytes = giftImg.getBytes();
            Path path = Paths.get(UPLOADED_FOLDER + giftImg.getOriginalFilename());
            Files.write(path, bytes);
            //마니또 이미지 경로 및 마니또 객체 정보 저장
            ObjectMapper objectMapper = new ObjectMapper();
            ManitoDTO manitoDTO = objectMapper.readValue(manito, ManitoDTO.class);
            manitoDTO.setGiftImg(path.toString());
            log.info("등록된 마니또 : {}", manitoDTO);
            manitoService.addManito(manitoDTO);
            return ResponseEntity.ok().body("Manito is uploaded");
        }catch (Exception e){
            return ResponseEntity.badRequest().body(e.getMessage());
        }
    }
}
