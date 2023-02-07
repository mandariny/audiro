package com.a402.audiro.service;

import com.a402.audiro.dto.PostcardDTO;

public interface SmsService {

    void sendMessage(PostcardDTO postcardDTO);
}
