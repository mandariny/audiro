package com.a402.audiro.db;

import com.a402.audiro.entity.Gift;
import com.a402.audiro.entity.Song;
import com.a402.audiro.entity.Spot;
import com.a402.audiro.entity.User;
import com.a402.audiro.repositories.GiftRepository;
import com.a402.audiro.repositories.SongRepository;
import com.a402.audiro.repositories.SpotRepository;
import com.a402.audiro.repositories.UserRepository;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
public class GiftRepositoryTest {

    @Autowired
    GiftRepository giftRepository;

    @Autowired
    UserRepository userRepository;

    @Autowired
    SongRepository songRepository;

    @Autowired
    SpotRepository spotRepository;

    @Test
    @DisplayName("GiftRepository save 확인")
    void giftTableSaveCheck(){
        User user = userRepository.findById(2);
        Song song = songRepository.findById(1);
        Spot spot = spotRepository.findById(1);

        Gift gift = Gift.builder()
                .user(user)
                .spot(spot)
                .song(song)
                .giftImg("img path~~~")
                .build();

        giftRepository.save(gift);
    }

    @Test
    @DisplayName("GiftRepository findByGiftId 확인")
    void giftRepositoryFindByGiftIdCheck(){
        Gift gift = giftRepository.findById(1);
        Assertions.assertThat(gift.getUser().getName()).isEqualTo("gaok");
    }
}
