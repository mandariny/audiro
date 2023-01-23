package com.a402.audiro.dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.LocalDate;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class GiftDTO {

    private long id;
    private String giftImg;
    private String song;
    private String singer;
    private String songUrl;
    private LocalDate regDate;
    private GiftEmojiDTO emoji;
}
