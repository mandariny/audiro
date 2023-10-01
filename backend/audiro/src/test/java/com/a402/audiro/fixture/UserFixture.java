package com.a402.audiro.fixture;

import com.a402.audiro.entity.User;

public class UserFixture {
    public static final User USER_1 = User.builder()
            .id(1l)
            .name("USER 1")
            .token("access token")
            .nickname("USER 1 nickname")
            .role("ROLE_USER")
            .email("www@www.www")
            .refreshToken("refresh token")
            .msg("profile message")
            .img("profile image")
            .build();
}