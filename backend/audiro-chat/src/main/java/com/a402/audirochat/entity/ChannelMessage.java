package com.a402.audirochat.entity;

import java.time.LocalDateTime;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.ToString;

@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
@ToString
public class ChannelMessage {
    public enum ContentType{
        MESSAGE, IMAGE
    }

    public ChannelMessage(String userId, String userNickname, ContentType type, String content){
        this.userId = userId;
        this.userNickname = userNickname;
        this.contentType = type;
        this.content = content;
        this.sendTime = LocalDateTime.now();
    }

    private String userId;
    private String userNickname;
    private ContentType contentType;
    private String content;
    LocalDateTime sendTime;
}