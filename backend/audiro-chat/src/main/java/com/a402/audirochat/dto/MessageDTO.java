package com.a402.audirochat.dto;

import com.a402.audirochat.entity.ContentType;
import com.a402.audirochat.exception.IdNullException;
import com.sun.istack.NotNull;
import lombok.*;

import java.time.LocalDateTime;

@Builder
@AllArgsConstructor
@NoArgsConstructor
@Getter
@ToString
public class MessageDTO {

    @NotNull
    private String userId;
    private String receiverId;
    @NotNull
    private String userNickname;
    @NotNull
    private ContentType contentType;
    @NotNull
    private String content;
    LocalDateTime sendTime;

    public void isReceiverValid(){
        if(receiverId == null) throw new IdNullException();
    }
}
