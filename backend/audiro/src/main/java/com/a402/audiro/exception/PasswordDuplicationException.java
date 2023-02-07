package com.a402.audiro.exception;

public class PasswordDuplicationException extends RuntimeException{
    public PasswordDuplicationException(){
        super("비밀번호가 중복됩니다.");
    }
}
