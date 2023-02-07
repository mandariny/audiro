package com.a402.audiro.service;

import com.a402.audiro.dto.PasswordDTO;
import com.a402.audiro.dto.PostcardDTO;
import com.a402.audiro.entity.Postcard;
import com.a402.audiro.entity.Song;
import com.a402.audiro.entity.Spot;
import com.a402.audiro.exception.PasswordDuplicationException;
import com.a402.audiro.repository.PostcardRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class PostcardServiceImpl implements PostcardService{

    private final PostcardRepository postcardRepository;
    private final SongService songService;
    private final SpotService spotService;

    @Override
    public void isValidPassword(PasswordDTO passwordDTO) {
        Postcard postcard = postcardRepository.findByPasswrod(passwordDTO.getPasswd());

        if(postcard != null) throw new PasswordDuplicationException();
    }

    @Override
    public void savePostcard(PostcardDTO postcardDTO) {
        Song song = songService.isValidSong(postcardDTO.getSongId());
        Spot spot = spotService.isValid(postcardDTO.getSpotId());
    }
}
