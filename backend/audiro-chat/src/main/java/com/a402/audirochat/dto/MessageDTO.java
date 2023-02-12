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
    private long userId;
    private long receiverId;

    private String userNickname;

    private ContentType contentType;
    @NotNull
    private String content;
    LocalDateTime sendTime;

//    public void isReceiverValid(){
//        if(receiverId == null) throw new IdNullException();
//    }
    public void setSendTime(){
        this.sendTime = LocalDateTime.now();
    }
}
