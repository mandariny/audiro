package com.a402.audiro.service;

import com.a402.audiro.entity.Spot;
import com.a402.audiro.exception.SpotNotExistException;
import com.a402.audiro.repository.SpotRepository;
import lombok.RequiredArgsConstructor;

@RequiredArgsConstructor
public class SpotServiceImpl implements SpotService{

    private final SpotRepository spotRepository;

    @Override
    public Spot isValid(long id) {
        Spot spot = spotRepository.findById(id);

        if(spot == null) throw new SpotNotExistException();

        return spot;
    }
}
