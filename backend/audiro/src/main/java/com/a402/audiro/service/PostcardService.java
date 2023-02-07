package com.a402.audiro.service;


import com.a402.audiro.dto.PasswordDTO;
import com.a402.audiro.dto.PostcardDTO;

public interface PostcardService {

    public void isValidPassword(PasswordDTO passwordDTO);

    public void savePostcard(PostcardDTO postcardDTO);

}
