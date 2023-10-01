package com.a402.audiro.fixture;

import com.a402.audiro.entity.Song;

import javax.persistence.Column;
import javax.persistence.Id;

public class SongFixture {
    public static final Song SONG_1 = Song.builder()
            .id(1l)
            .songImg("song_img_url")
            .songTitle("song title")
            .singer("singer")
            .songUrl("song_url")
            .build();
}