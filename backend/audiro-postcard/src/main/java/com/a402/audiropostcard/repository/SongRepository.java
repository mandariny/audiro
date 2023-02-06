package com.a402.audiropostcard.repository;

import com.a402.audiropostcard.entity.Song;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.Repository;
import org.springframework.data.repository.query.Param;

public interface SongRepository extends Repository<Song, Long> {

    @Query(value = "select song_id, song_title, singer, song_url from Song where song_id = :song_id", nativeQuery = true)
    Song findById(@Param("song_id")long id);
}
