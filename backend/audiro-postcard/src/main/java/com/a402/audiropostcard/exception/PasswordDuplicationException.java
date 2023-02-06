package com.a402.audiropostcard.exception;

public class PasswordDuplicationException extends RuntimeException{
    public PasswordDuplicationException(){
        super("비밀번호가 중복됩니다.");
    }
}
