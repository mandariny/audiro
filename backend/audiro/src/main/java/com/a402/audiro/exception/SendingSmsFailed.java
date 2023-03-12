package com.a402.audiro.exception;

public class SendingSmsFailed extends RuntimeException{
    public SendingSmsFailed(String className, String code){
        super("sms 메세지 보내기에 실패했습니다, 구현체 : " + className + ", status code : " + code);
    }
}
