package com.a402.audiro.dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class SongChartDTO {

    private long song_meta_id;
    private long song_id;
    private long song_liked;
    private long gift_cnt;
    private long update_time;
    private String song_title;
    private String singer;
    private String song_url;
    private String song_img;

}
