package com.a402.audirochat.entity;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.ToString;

import java.io.Serializable;

@AllArgsConstructor
@NoArgsConstructor
@Getter
public class ChannelInfo implements Serializable {
    private Channel channel;
    private String memberNickname;
}
