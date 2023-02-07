package com.a402.audiro.service;

import com.a402.audiro.dto.GiftDTO;
import com.a402.audiro.dto.GiftEmojiDTO;
import com.a402.audiro.dto.GiftThumbnailDTO;
import com.a402.audiro.entity.Gift;
import com.a402.audiro.repository.GiftRepository;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
@Slf4j
@RequiredArgsConstructor
public class GiftServiceImpl implements GiftService{

    private final GiftRepository giftRepository;

    @Override
    public List<GiftThumbnailDTO> getGiftList(String nickname){
        List<Gift> gift;
        List<GiftThumbnailDTO> giftDTOList;

        log.warn("gift before");
        gift = giftRepository.findByNickname(nickname);
        log.warn("gift log: " +gift.get(0).toString());

        gift = giftRepository.findByNickname(nickname);
        giftDTOList = gift.stream()
                .map(g -> GiftThumbnailDTO.builder()
                        .id(g.getId())
                        .giftImg(g.getGiftImg())
                        .build())
                .collect(Collectors.toList());

        return giftDTOList;
    }

    @Override
    public GiftDTO getGiftDetail(long giftId) {
        Gift gift;
        gift = giftRepository.findById(giftId);

        return GiftDTO.builder()
                .id(gift.getId())
                .giftImg(gift.getGiftImg())
                .song(gift.getSong().getSongTitle())
                .singer(gift.getSong().getSinger())
                .songUrl(gift.getSong().getSongUrl())
                .regDate(gift.getRegTime())
                .emoji(GiftEmojiDTO.builder()
                        .emo1(gift.getFeed1())
                        .emo2(gift.getFeed2())
                        .emo3(gift.getFeed3())
                        .emo4(gift.getFeed4())
                        .build())
                .build();
    }

    @Override
    public void deleteGift(long giftId) {
        giftRepository.deleteById(giftId);
    }

    @Override
    public void addFeedbackCnt(long giftId, int idx) {
        Gift gift = giftRepository.findById(giftId);
        switch (idx){
            case 1:
                gift.addFeed1();
                break;
            case 2:
                gift.addFeed2();
                break;
            case 3:
                gift.addFeed3();
                break;
            case 4:
                gift.addFeed4();
                break;
        }
        giftRepository.save(gift);
    }
}
