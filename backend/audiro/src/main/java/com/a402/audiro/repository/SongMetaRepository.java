package com.a402.audiro.repository;

import com.a402.audiro.entity.Song;
import com.a402.audiro.entity.SongMeta;
import com.a402.audiro.entity.Spot;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.Repository;
import org.springframework.data.repository.query.Param;

import java.util.List;

public interface SongMetaRepository extends Repository<SongMeta, Long> {

    void save(SongMeta songMeta);

    @Query(value = "select * from song_meta where song_meta.song_id = :song_id and song_meta.spot_id = :spot_id",
            nativeQuery = true)
    SongMeta findBySongIdAndSpotId(@Param("song_id") long SongId, @Param("spot_id")long SpotId);

    @Query(value = "select * from song_meta join song on song_meta.song_id=song.song_id where song_meta.spot_id = :spot_id order by gift_cnt DESC",
            nativeQuery = true)
    List<SongMeta> findBySpotIdGiftCnt(@Param("spot_id")long SpotId);

    @Query(value = "select * from song_meta join song on song_meta.song_id=song.song_id where song_meta.spot_id = :spot_id order by update_time DESC",
            nativeQuery = true)
    List<SongMeta> findBySpotIdTime(@Param("spot_id")long SpotId);

    SongMeta findBySongAndSpot(Song song, Spot spot);
}
