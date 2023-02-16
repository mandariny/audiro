package com.a402.audiro.exception;

public class TokenNotExist extends RuntimeException{
    public TokenNotExist(){
        super("토큰이 존재하지 않습니다.");
    }

}
