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

    private String userId;
    private String userNickname;
    private ContentType contentType;
    private String content;
    LocalDateTime sendTime;
}
