package com.a402.audirochat.entity;

import java.util.ArrayList;
import java.util.List;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.ToString;
import org.springframework.data.annotation.Id;
import org.springframework.data.redis.core.RedisHash;

@RedisHash("user")
@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
@ToString
public class User {

    @Id
    private String Id;
    private List<ChannelInfo> channels = new ArrayList<>();

    public void addChannels(Channel channel, String memberNickname){
        this.channels.add(new ChannelInfo(channel, memberNickname));
    }

}
