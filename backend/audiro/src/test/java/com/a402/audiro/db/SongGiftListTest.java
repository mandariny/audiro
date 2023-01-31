package com.a402.audiro.db;

import com.a402.audiro.entity.Gift;
import com.a402.audiro.entity.Song;
import com.a402.audiro.entity.Spot;
import com.a402.audiro.entity.User;
import com.a402.audiro.repository.GiftRepository;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import java.util.List;

@SpringBootTest
public class SongGiftListTest {

    @Autowired
    GiftRepository giftRepository;

    @Test
    @DisplayName("GiftRepository songId로 찾기")
    void findBySongIdCheck(){
        List<Gift> gifts = giftRepository.findBySongId(1, 1);
        Assertions.assertThat(gifts.size()).isEqualTo(2);
    }
}
