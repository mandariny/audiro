package com.a402.audiropostcard.service;

import com.a402.audiropostcard.dto.PasswordDTO;
import com.a402.audiropostcard.dto.PostcardDTO;

public interface PostcardService {

    public void isValidPassword(PasswordDTO passwordDTO);

    public void savePostcard(PostcardDTO postcardDTO);

}
