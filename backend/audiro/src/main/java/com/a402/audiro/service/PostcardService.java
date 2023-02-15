package com.a402.audiro.service;


import com.a402.audiro.dto.PasswordDTO;
import com.a402.audiro.dto.PostcardDTO;
import com.a402.audiro.dto.PostcardDetailDTO;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;

public interface PostcardService {

    public void isValidPassword(String password);

    public void savePostcard(MultipartFile postcardImg, PostcardDTO postcardDTO) throws IOException;

    PostcardDetailDTO getPostcardDetail(long postcardId);
}
