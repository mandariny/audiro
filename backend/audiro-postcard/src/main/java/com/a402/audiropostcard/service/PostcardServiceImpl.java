package com.a402.audiropostcard.service;

import com.a402.audiropostcard.dto.PasswordDTO;
import com.a402.audiropostcard.dto.PostcardDTO;
import com.a402.audiropostcard.entity.Postcard;
import com.a402.audiropostcard.entity.Song;
import com.a402.audiropostcard.entity.Spot;
import com.a402.audiropostcard.exception.PasswordDuplicationException;
import com.a402.audiropostcard.exception.SongNotExistException;
import com.a402.audiropostcard.exception.SpotNotExistException;
import com.a402.audiropostcard.repository.PostcardRepository;
import com.a402.audiropostcard.repository.SongRepository;
import com.a402.audiropostcard.repository.SpotRepository;
import java.time.LocalDateTime;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class PostcardServiceImpl implements PostcardService{

    private final PostcardRepository postcardRepository;
    private final SongRepository songRepository;
    private final SpotRepository spotRepository;

    private void isValidSong(long id){
        Song song = songRepository.findById(id);

        if(song == null) throw new SongNotExistException();
    }

    private void isValidSpot(long id){
        Spot spot = spotRepository.findById(id);

        if(spot == null) throw new SpotNotExistException();
    }

    @Override
    public void isValidPassword(PasswordDTO passwordDTO) {
        Postcard postcard = postcardRepository.findByPasswrod(passwordDTO.getPasswd());

        if(postcard != null) throw new PasswordDuplicationException();
    }

    @Override
    public void savePostcard(PostcardDTO postcardDTO) {
        isValidSong(postcardDTO.getSongId());
        isValidSpot(postcardDTO.getSpotId());

        Postcard postcard = Postcard.builder()
                .sendId(postcardDTO.getSendId())
                .songId(postcardDTO.getSongId())
                .spotId(postcardDTO.getSpotId())
                .password(postcardDTO.getPasswd())
                .postcardImg(postcardDTO.getPostcardImg())
                .regTime(LocalDateTime.now())
                .build();

        postcardRepository.save(postcard);
    }
}
