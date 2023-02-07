package com.a402.audiro.service;

import com.a402.audiro.dto.SongChartDTO;
import com.a402.audiro.entity.Song;
import java.util.List;

public interface SongChartService {
    List<SongChartDTO> getSongListByGiftCnt(long spotId);
    List<SongChartDTO> getSongListByTime(long spotId);
    List<SongChartDTO> getSongListByRandom(long spotId);
}
