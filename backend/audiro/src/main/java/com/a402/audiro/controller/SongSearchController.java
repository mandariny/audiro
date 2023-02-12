package com.a402.audiro.controller;

import com.a402.audiro.dto.SongDTO;
import com.a402.audiro.service.SongService;
import lombok.Builder;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@CrossOrigin(origins = "*")
@RequiredArgsConstructor
@Builder
@Slf4j
@RequestMapping("/song/search")
public class SongSearchController {

    SongService songService;

    public ResponseEntity<?> getSongList(@RequestParam String keyword){
        List<SongDTO> songList = songService.search(keyword);
        return ResponseEntity.ok().body(songList);
    }
}
