package com.a402.audirochat.entity;

import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.ToString;
import org.springframework.data.annotation.Id;
import org.springframework.data.redis.core.RedisHash;

@RedisHash("channel")
@AllArgsConstructor
@Getter
@Setter
@ToString
public class Channel {
    @Id
    private String Id;
    private List<ChannelMessage> messages = new ArrayList<>();

    public Channel(){
        this.Id = UUID.randomUUID().toString();
    }

    public void addChannelMessage(ChannelMessage message){
        this.messages.add(message);
    }

    public String getLastMessage(){
        if(this.messages.size() == 0) return null;
        return this.messages.get(this.messages.size() - 1).getContent();
    }
}
