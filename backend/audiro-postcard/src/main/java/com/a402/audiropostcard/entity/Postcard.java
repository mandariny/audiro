package com.a402.audiropostcard.entity;

import java.time.LocalDateTime;
import javax.persistence.Entity;
import javax.persistence.Id;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Entity
@Getter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Postcard {

    @Id
    private long Id;

    private long sendId;
    private long songId;
    private long spotId;
    private String password;
    private String postcardImg;
    private LocalDateTime regTime;

}
