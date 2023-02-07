package com.a402.audiro.exception;

public class SpotNotExistException extends RuntimeException{
    public SpotNotExistException(){
        super("존재하지 않는 지점입니다.");
    }
}
