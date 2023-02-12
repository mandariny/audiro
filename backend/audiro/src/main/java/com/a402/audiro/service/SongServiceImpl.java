package com.a402.audiro.service;

import java.util.List;
import com.a402.audiro.dto.SongDTO;
import com.a402.audiro.entity.Song;
import com.a402.audiro.exception.SongNotExistException;
import com.a402.audiro.repository.SongRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
@RequiredArgsConstructor
public class SongServiceImpl implements SongService{

    private final SongRepository songRepository;

    public Song isValidSong(long id){
        Song song = songRepository.findById(id);

        if(song == null) throw new SongNotExistException();

        return song;
    }

    @Transactional
    public List<SongDTO> search(String keyword){
        List<SongDTO> songList = songRepository.findByTitle(keyword);
        return songList;
    }
}
