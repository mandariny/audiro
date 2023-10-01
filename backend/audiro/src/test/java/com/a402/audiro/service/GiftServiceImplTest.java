package com.a402.audiro.service;

import com.a402.audiro.dto.GiftThumbnailDTO;
import com.a402.audiro.fixture.GiftThumbnailDTOFixture;
import com.a402.audiro.repository.GiftRepository;
import com.a402.audiro.repository.UserRepository;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import javax.transaction.Transactional;

import java.util.List;

import static com.a402.audiro.fixture.GiftThumbnailDTOFixture.GIFT_THUMBNAIL_1;
import static com.a402.audiro.fixture.GiftThumbnailDTOFixture.GIFT_THUMBNAIL_2;
import static org.assertj.core.api.Assertions.assertThat;
import static com.a402.audiro.fixture.GiftFixture.GIFT_1;
import static com.a402.audiro.fixture.GiftFixture.GIFT_2;
import static com.a402.audiro.fixture.UserFixture.USER_1;
import static org.mockito.BDDMockito.given;
import static org.mockito.Mockito.lenient;

@ExtendWith(MockitoExtension.class)
@Transactional
class GiftServiceImplTest {
    @InjectMocks
    private GiftServiceImpl giftService;

    @Mock
    private GiftRepository giftRepository;

    @Mock
    private UserRepository userRepository;

    @Mock
    private UserService userService;

    @BeforeEach
    void setUp(){
        //given(userRepository.findByNickname(USER_1.getNickname()))
        //        .willReturn(USER_1);
        given(userService.isSameUser(USER_1.getNickname()))
                .willReturn(true);
    }

    @DisplayName("유저의 gift를 모두 반환한다.")
    @Test
    void getAllGifts(){
        // given
        given(giftRepository.findByNickname(USER_1.getNickname()))
                .willReturn(List.of(GIFT_1, GIFT_2));

        // when
        final List<GiftThumbnailDTO> expected = giftService.getGiftList(USER_1.getNickname());

        // then
        assertThat(expected).usingRecursiveComparison()
                .isEqualTo(List.of(GIFT_THUMBNAIL_1, GIFT_THUMBNAIL_2));
    }
}