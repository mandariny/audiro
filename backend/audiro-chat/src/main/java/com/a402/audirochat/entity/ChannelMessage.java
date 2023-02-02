package com.a402.audirochat.entity;

import java.time.LocalDateTime;

import lombok.*;

@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
@ToString
@Builder
public class ChannelMessage {

    private String userId;
    private String userNickname;
    private ContentType contentType;
    private String content;
    LocalDateTime sendTime;

    public ChannelMessage(String userId, String userNickname, ContentType type, String content){
        this.userId = userId;
        this.userNickname = userNickname;
        this.contentType = type;
        this.content = content;
        this.sendTime = LocalDateTime.now();
    }
}