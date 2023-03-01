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
    void add1000Like() throws InterruptedException{
        Gift gift = giftService.getGift(1);
        ExecutorService executorService = Executors.newFixedThreadPool(5);
        CountDownLatch countDownLatch = new CountDownLatch(5);
        for(int i=0; i<5; i++){
            executorService.execute(()->{
                giftService.addLike(1);
            });
            countDownLatch.countDown();
        }
        countDownLatch.await();
        Assertions.assertThat(gift.getLike() + 5).as("좋아요가 5 증가해야 함").isEqualTo(giftService.getGift(1).getLike());
    }
}
