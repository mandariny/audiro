package com.a402.audiropostcard.entity;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Entity
@Getter
@NoArgsConstructor
@AllArgsConstructor
public class Song {

    @Id
    @Column(name = "song_id")
    private long Id;

    @Column(name = "song_title")
    private String title;
    private String singer;
    @Column(name = "song_url")
    private String url;
}
