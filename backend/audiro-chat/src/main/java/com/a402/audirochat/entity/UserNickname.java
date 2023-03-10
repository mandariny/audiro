package com.a402.audirochat.entity;

import lombok.Getter;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name = "user_nickname")
@Getter
public class UserNickname {

    @Id
    @Column(name = "user_id")
    private long id;

    private String nickname;
}
