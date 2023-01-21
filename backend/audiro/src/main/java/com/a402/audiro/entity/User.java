package com.a402.audiro.entity;

import lombok.NoArgsConstructor;
import org.hibernate.annotations.ColumnDefault;
import org.hibernate.annotations.DynamicInsert;

import javax.persistence.*;

@Entity
@DynamicInsert
@NoArgsConstructor
public class User {

    @Id
    @Column(name = "user_id")
    @GeneratedValue(strategy = GenerationType.AUTO)
    private long userId;
    private String name;
    private String token;
    private String nickname;

    @Column(name = "profile_message")
    private String msg;
    @Column(name = "profile_img")
    private String img;

    public User(String name, String token, String nickname) {
        this.name = name;
        this.token = token;
        this.nickname = nickname;
    }

    @Override
    public String toString(){
        return String.format("User[id=%d, name='%s', token='%s', nickname='%s']", userId, name, token, nickname);
    }

    public long getUserId() {
        return userId;
    }

    public String getName() {
        return name;
    }

    public String getToken() {
        return token;
    }

    public String getNickname() {
        return nickname;
    }

    public String getMsg() {
        return msg;
    }

    public String getImg() {
        return img;
    }
}
