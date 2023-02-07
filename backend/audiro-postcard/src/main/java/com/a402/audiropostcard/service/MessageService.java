package com.a402.audiropostcard.service;

import com.a402.audiropostcard.dto.PostcardDTO;

public interface MessageService {

    void sendMessage(PostcardDTO postcardDTO);

}
