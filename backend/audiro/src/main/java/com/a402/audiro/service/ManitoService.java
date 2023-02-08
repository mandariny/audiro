package com.a402.audiro.service;

import com.a402.audiro.dto.GiftThumbnailDTO;
import com.a402.audiro.dto.ManitoDTO;

import com.a402.audiro.dto.ManitoImagePairDTO;
import java.io.FileNotFoundException;
import java.util.List;

public interface ManitoService {
    List<GiftThumbnailDTO> getManitoList();

    List<ManitoImagePairDTO> getManitoImagePairList();

    void addManito(ManitoDTO manitoDTO);

    byte[] imageToByte(String pathInString) throws FileNotFoundException;
}
