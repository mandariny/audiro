package com.a402.audiro.service;

import com.a402.audiro.entity.Song;
import com.a402.audiro.exception.SongNotExistException;
import com.a402.audiro.repository.SongRepository;
import lombok.RequiredArgsConstructor;

@RequiredArgsConstructor
public class SongServiceImpl implements SongService{

    private final SongRepository songRepository;

    public Song isValidSong(long id){
        Song song = songRepository.findById(id);

        if(song == null) throw new SongNotExistException();

        return song;
    }
}
