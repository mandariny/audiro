package com.a402.audiro.exception;

public class RetrialFailedException extends RuntimeException{
    public RetrialFailedException(){
        super("sms retry failed");
    }
}
