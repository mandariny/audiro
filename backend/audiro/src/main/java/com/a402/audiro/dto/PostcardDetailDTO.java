package com.a402.audiro.dto;

import java.time.LocalDateTime;
import lombok.Builder;
import lombok.Getter;

@Builder
@Getter
public class PostcardDetailDTO {
    private long id;
    private String postcardImg;
    private String songTitle;
    private String singer;
    private String songUrl;
    private LocalDateTime regTime;

    @Override
    public String toString() {
        return "PostcardDetailDTO{" +
                "id=" + id +
                ", postcardImg='" + postcardImg + '\'' +
                ", songTitle='" + songTitle + '\'' +
                ", singer='" + singer + '\'' +
                ", songUrl='" + songUrl + '\'' +
                ", regTime=" + regTime +
                '}';
    }
}
