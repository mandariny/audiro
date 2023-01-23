package com.a402.audiro.service;

import com.a402.audiro.dto.GiftDTO;
import com.a402.audiro.dto.ManitoDTO;
import com.a402.audiro.entity.Gift;
import com.a402.audiro.entity.Song;
import com.a402.audiro.entity.Spot;
import com.a402.audiro.entity.User;
import com.a402.audiro.repository.GiftRepository;
import com.a402.audiro.repository.SongRepository;
import com.a402.audiro.repository.SpotRepository;
import com.a402.audiro.repository.UserRepository;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
@Slf4j
@RequiredArgsConstructor
public class ManitoServiceImpl implements ManitoService{

    private final GiftRepository giftRepository;
    private final UserRepository userRepository;
    private final SongRepository songRepository;
    private final SpotRepository spotRepository;

    @Override
    public List<GiftDTO> getManitoList() {
        List<Gift> manito;
        List<GiftDTO> manitoList;

        try{
            manito = giftRepository.findManitos();
            manitoList = manito.stream()
                    .map(m -> GiftDTO.builder()
                            .id(m.getId())
                            .giftImg(m.getGiftImg())
                            .build())
                    .collect(Collectors.toList());
        }catch(Exception e){
            log.error(e.getMessage());
            throw e;
        }

        return manitoList;
    }

    @Override
    public void addManito(ManitoDTO manitoDTO) {
        try{
            // 기존 마니토를 밀어냄
            Gift beforeManito = giftRepository.findById(manitoDTO.getBeforeManitoId());
            beforeManito.setManito(Boolean.FALSE);

            // 새로운 마니토를 추가함
            User user = userRepository.findById(manitoDTO.getUserId());
            Song song = songRepository.findById(manitoDTO.getSongId());
            Spot spot = spotRepository.findById(manitoDTO.getSpotId());

            Gift manito = Gift.builder()
                    .user(user)
                    .song(song)
                    .spot(spot)
                    .giftImg(manitoDTO.getGiftImg())
                    .giftTag(manitoDTO.getGiftTag())
                    .isManito(Boolean.TRUE)
                    .build();
            giftRepository.save(manito);
        }catch (Exception e){
            log.error(e.getMessage());
            throw e;
        }
    }
}
