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

@RedisHash("channel")
@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
@ToString
public class Channel {
    @Id
    private String Id;
    private List<ChannelMessage> messages = new ArrayList<>();
}
