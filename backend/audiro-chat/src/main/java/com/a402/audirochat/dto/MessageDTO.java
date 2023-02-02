package com.a402.audirochat.dto;

import com.a402.audirochat.entity.ContentType;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;

import java.time.LocalDateTime;

@Builder
@AllArgsConstructor
@Getter
public class MessageDTO {

    private String userId;
    private String userNickname;
    private ContentType contentType;
    private String content;
    LocalDateTime sendTime;
}
