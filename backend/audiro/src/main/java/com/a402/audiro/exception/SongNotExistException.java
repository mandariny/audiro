package com.a402.audiro.exception;

public class SongNotExistException extends RuntimeException{
    public SongNotExistException(){
        super("존재하지 않는 노래입니다.");
    }
}
