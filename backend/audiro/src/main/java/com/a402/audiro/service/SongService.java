package com.a402.audiro.service;

import java.util.List;
import com.a402.audiro.entity.Song;
import com.a402.audiro.dto.SongDTO;

public interface SongService {

    List<SongDTO> search(String keyword);
    Song isValidSong(long id);
}
