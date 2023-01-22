package com.a402.audiro.db;

import com.a402.audiro.entity.Gift;
import com.a402.audiro.repositories.GiftRepository;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
public class GiftRepositoryTest {

    @Autowired
    GiftRepository giftRepository;

    @Test
    @DisplayName("GiftRepository findByGiftId 확인")
    void giftTableSaveCheck(){
        Gift gift = giftRepository.findById(1);
        Assertions.assertThat(gift.getUser().getName()).isEqualTo("gaok");
    }
}
