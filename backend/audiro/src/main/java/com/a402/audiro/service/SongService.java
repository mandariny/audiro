package com.a402.audiro.service;

import com.a402.audiro.dto.SongSearchDTO;
import com.a402.audiro.entity.Song;

import java.util.List;

public interface SongService {

    List<SongSearchDTO> searchSong(String keyword);
    Song isValidSong(long id);
}
