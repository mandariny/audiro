package com.a402.audiro.fixture;

import com.a402.audiro.entity.*;

import static com.a402.audiro.fixture.SongFixture.SONG_1;
import static com.a402.audiro.fixture.SpotFixture.SPOT_1;
import static com.a402.audiro.fixture.UserFixture.USER_1;

public class GiftFixture {

    public static final Gift GIFT_1 = Gift.builder()
            .id(1l)
            .user(USER_1)
            .spot(SPOT_1)
            .song(SONG_1)
            .giftImg("gift_img_url")
            .giftTag(GiftTag.SUNNY)
            .build();

    public static final Gift GIFT_2 = Gift.builder()
            .id(1l)
            .user(USER_1)
            .spot(SPOT_1)
            .song(SONG_1)
            .giftImg("gift_img_url2")
            .giftTag(GiftTag.CLOUDY)
            .build();
}