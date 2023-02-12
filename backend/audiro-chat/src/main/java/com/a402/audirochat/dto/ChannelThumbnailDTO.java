package com.a402.audirochat.dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;

import java.time.LocalDateTime;

@Builder
@AllArgsConstructor
@Getter
public class ChannelThumbnailDTO {

    private String channelId;
    private String nickname;
    private String lastMessage;
    private LocalDateTime lastMessageTime;
}
