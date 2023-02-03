package com.a402.audirochat.dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;

@Builder
@AllArgsConstructor
@Getter
public class ChannelThumbnailDTO {

    private String channelId;
    private String nickname;
    private String lastMessage;
}
