package com.a402.audiro.gift;

import com.a402.audiro.entity.Gift;
import com.a402.audiro.service.GiftService;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import java.util.concurrent.CountDownLatch;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

@SpringBootTest
public class GiftLikeTest {

    @Autowired
    private GiftService giftService;

    @DisplayName("기프드 좋아요 수 증가 한 번")
    @Test
    void addOneLike(){
        Gift gift = giftService.getGift(1);

        giftService.addLike(1);

        Assertions.assertThat(gift.getLike() + 1).as("좋아요가 1 증가해야 함").isEqualTo(giftService.getGift(1).getLike());
    }

    @DisplayName("기프트 좋아요 수 10번 증가")
    @Test
    void add10Like() throws InterruptedException{
        final int CNT = 10;
        final int GIFT_Id = 1;
        Gift gift = giftService.getGift(GIFT_Id);
        ExecutorService executorService = Executors.newFixedThreadPool(CNT);
        CountDownLatch countDownLatch = new CountDownLatch(CNT);
        for(int i=0; i<CNT; i++){
            executorService.execute(()->{
                giftService.addLike(GIFT_Id);
                countDownLatch.countDown();
            });
        }
        countDownLatch.await();
        Assertions.assertThat(gift.getLike() + CNT).as("좋아요가 " + CNT + " 증가해야 함").isEqualTo(giftService.getGift(GIFT_Id).getLike());
    }
}
