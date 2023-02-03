package com.a402.audirochat.entity;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;

@Entity
public class UserNickname {

    @Id
    @Column(name = "user_id")
    private String id;

    private String nickname;
}
