package com.a402.audiro.service;

import com.a402.audiro.dto.GiftThumbnailDTO;
import com.a402.audiro.dto.ManitoDTO;
import com.a402.audiro.dto.ManitoImagePairDTO;
import com.a402.audiro.entity.*;
import com.a402.audiro.repository.*;
import java.awt.image.BufferedImage;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStream;
import javax.imageio.ImageIO;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDateTime;
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
    private final SongMetaRepository songMetaRepository;

    @Override
    public List<GiftThumbnailDTO> getManitoList() {
        List<Gift> manito;
        List<GiftThumbnailDTO> manitoList;

        try{
            manito = giftRepository.findManitos();
            manitoList = manito.stream()
                    .map(m -> GiftThumbnailDTO.builder()
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
    public List<ManitoImagePairDTO> getManitoImagePairList() {
        log.info("Manito리스트 이미지+객체 추출 시작");
        List<Gift> manitos;
        List<ManitoImagePairDTO> manitoImagePairList;

        try{
            manitos = giftRepository.findManitos();
            manitoImagePairList = manitos.stream()
                    .map(m -> ManitoImagePairDTO.builder()
                            .id(m.getId())
                            .imageInBytes(imageToByte(m.getGiftImg()))
                            .build())
                    .collect(Collectors.toList());
        }catch(Exception e){
            log.error(e.getMessage());
            throw e;
        }

        return manitoImagePairList;
    }

    @Override
    public byte[] imageToByte(String pathInString) {
        log.info("파일 읽기 시작. 파일 경로 : {}",pathInString);
        byte[] imageBytes;
        try {
            File imageFile = new File(pathInString);
            InputStream inputStream = new FileInputStream(imageFile);
            imageBytes = new byte[(int) imageFile.length()];

        }
        catch (Exception e){
            log.error("파일을 읽을 수 없습니다.");
            return null;
        }
        return imageBytes;
    }

    @Transactional
    @Override
    public void addManito(ManitoDTO manitoDTO) {
        try{
            // 기존 마니토를 밀어냄
            Gift beforeManito = giftRepository.findById(manitoDTO.getBeforeManitoId());
            beforeManito.setManito(Boolean.FALSE);
            log.info("삭제된 마니또 : {}",beforeManito);

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

            // 노래 추천 횟수 수정
            SongMeta beforeManitoMeta = songMetaRepository.findBySongAndSpot(beforeManito.getSong(), beforeManito.getSpot());
            SongMeta manitoMeta = songMetaRepository.findBySongAndSpot(manito.getSong(), manito.getSpot());

            if(manitoMeta == null){
                manitoMeta = SongMeta.builder()
                        .song(song)
                        .spot(spot)
                        .updateTime(LocalDateTime.now())
                        .liked(0)
                        .build();
            }

            if(beforeManito.getId() != manito.getId()){
                beforeManitoMeta.minusCnt();
                manitoMeta.plusCnt();
                songMetaRepository.save(beforeManitoMeta);
            }

            manitoMeta.setUpdateTime();

            songMetaRepository.save(manitoMeta);

        }catch (Exception e){
            log.error(e.getMessage());
            throw e;
        }
    }
}
