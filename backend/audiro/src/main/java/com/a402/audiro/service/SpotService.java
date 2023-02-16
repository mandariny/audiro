package com.a402.audiro.service;

import com.a402.audiro.dto.JwtDTO;
import com.a402.audiro.entity.Spot;

public interface SpotService {
    Spot isValidSpot(long id);
    JwtDTO isTokenExist(long id);
    void eraseToken(long id);
    void saveToken(long id, String token);
}
