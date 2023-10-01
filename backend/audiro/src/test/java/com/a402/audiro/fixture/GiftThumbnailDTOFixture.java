package com.a402.audiro.fixture;

import com.a402.audiro.dto.GiftThumbnailDTO;

public class GiftThumbnailDTOFixture {

    public static final GiftThumbnailDTO GIFT_THUMBNAIL_1 = GiftThumbnailDTO.builder()
            .id(1l)
            .giftImg("gift_img_url")
            .build();

    public static final GiftThumbnailDTO GIFT_THUMBNAIL_2 = GiftThumbnailDTO.builder()
            .id(1l)
            .giftImg("gift_img_url2")
            .build();
}
