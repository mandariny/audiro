package com.a402.audiro.service;

import com.a402.audiro.dto.JwtDTO;
import com.a402.audiro.entity.Spot;
import com.a402.audiro.exception.SpotNotExistException;
import com.a402.audiro.repository.SpotRepository;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

@Slf4j
@Service
@RequiredArgsConstructor
public class SpotServiceImpl implements SpotService{

    private final SpotRepository spotRepository;

    @Override
    public Spot isValidSpot(long id) {
        Spot spot = spotRepository.findById(id);

        if(spot == null) throw new SpotNotExistException();

        return spot;
    }

    @Override
    public JwtDTO isTokenExist(long id) {
        Spot spot = spotRepository.findById(id);
        String token = spot.getToken();

        if(token == null || token.equals("")){
            throw new SpotNotExistException();
        }

        return JwtDTO.builder().token(token).build();
    }

    @Override
    public void eraseToken(long id) {
        log.info("토큰을 삭제합니다....");
        Spot spot = spotRepository.findById(id);
        spot.setToken("");
        spotRepository.save(spot);
    }

    @Override
    public void saveToken(long id, String token) {
        log.info("토큰을 저장합니다 : " + token);
        Spot spot = spotRepository.findById(id);
        spot.setToken(token);
        spotRepository.save(spot);
    }
}
