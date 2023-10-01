package com.a402.audiro.fixture;

import com.a402.audiro.entity.Spot;

public class SpotFixture {

    public static final Spot SPOT_1 = Spot.builder()
            .id(1l)
            .spotName("역삼점")
            .spotAddr("서울시 강남구 역삼동")
            .token("spot token")
            .build();
}