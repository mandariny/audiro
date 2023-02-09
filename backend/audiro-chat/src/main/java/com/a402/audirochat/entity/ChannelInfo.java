package com.a402.audirochat.entity;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.ToString;

@AllArgsConstructor
@NoArgsConstructor
@Getter
public class ChannelInfo {
    private Channel channel;
    private String memberNickname;
}
