package com.a402.audiro.service;

import com.a402.audiro.dto.PasswordDTO;
import com.a402.audiro.dto.PostcardDTO;
import com.a402.audiro.dto.PostcardDetailDTO;
import com.a402.audiro.entity.Postcard;
import com.a402.audiro.entity.Song;
import com.a402.audiro.entity.Spot;
import com.a402.audiro.entity.User;
import com.a402.audiro.exception.PasswordDuplicationException;
import com.a402.audiro.exception.PostcardNotExistException;
import com.a402.audiro.exception.RetrialFailedException;
import com.a402.audiro.repository.PostcardRepository;

import java.time.LocalDateTime;
import java.util.List;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import javax.annotation.PostConstruct;

@Service
@RequiredArgsConstructor
@Slf4j
public class PostcardServiceImpl implements PostcardService{

    private final PostcardRepository postcardRepository;
    private final UserService userService;
    private final SongService songService;
    private final SpotService spotService;
    private final List<SmsService> smsServices;
    private SmsService smsService;
    private final int DELAY = 2000;
    private final int MAX_TRIAL_COUNT = 2;

    @PostConstruct
    private void initSmsService(){
        smsService = this.smsServices.stream()
                .filter(service -> service instanceof SmsServiceCool)
                .findFirst()
                .get();
    }

    private void setAnotherSmsService(){
        smsService =  this.smsServices.stream()
                .filter(service -> service instanceof SmsServiceNaver)
                .findFirst()
                .get();
    }

    private boolean isSmsServiceAlreadyChanged(){
        return this.smsService instanceof SmsServiceNaver;
    }

    @Override
    public void isValidPassword(String password) {
        Postcard postcard = postcardRepository.findByPassword(password);

        if(postcard != null) throw new PasswordDuplicationException();
    }

    private void trySendMessage(PostcardDTO postcardDTO){
        int trialCount = 0;

        while(trialCount < MAX_TRIAL_COUNT){
            try{
                log.info(smsService.getClass().getName() + "???????????? ?????? ??????");
                smsService.sendMessage(postcardDTO);
                return;
            }catch (Exception e){
                trialCount++;
                log.info(trialCount + " trial failed");
                if(trialCount == MAX_TRIAL_COUNT) throw new RetrialFailedException();

                try {
                    Thread.sleep(DELAY);
                    log.info("sms ?????? ????????? retry...");
                } catch (InterruptedException ex) {
                    log.info("sms ?????? ????????? retry ??? delay ??????");
                }
            }
        }
    }

    @Transactional
    @Override
    public void savePostcard(PostcardDTO postcardDTO) {
        Song song = songService.isValidSong(postcardDTO.getSongId());
        Spot spot = spotService.isValidSpot(postcardDTO.getSpotId());
        isValidPassword(postcardDTO.getPasswd());

        User user = userService.getUser();

        Postcard postcard = Postcard.builder()
                .user(user)
                .song(song)
                .spot(spot)
                .password(postcardDTO.getPasswd())
                .postcardImg(postcardDTO.getPostcardImg())
                .regTime(LocalDateTime.now())
                .build();

        postcardRepository.save(postcard);

        boolean smsServiceChangeFlag = isSmsServiceAlreadyChanged();

        try{
            trySendMessage(postcardDTO);
        }catch(RetrialFailedException e){
            // ?????? service ???????????? ????????? ?????? ??????
            if(smsServiceChangeFlag) throw e;

            log.info("sms service ????????? ??????");
            // ?????? ?????? ?????? ???????????? ??????
            setAnotherSmsService();
            try{
                trySendMessage(postcardDTO);
            }catch(RetrialFailedException ee){
                log.error(e.getMessage());
            }
        }catch(Exception e){
            // ?????? ?????? ????????? ??????
            log.error(e.getMessage());
        }

    }

    private Postcard getPostcard(String passwd){
        Postcard postcard = postcardRepository.findByPassword(passwd);

        if(postcard == null) throw new PostcardNotExistException();

        return postcard;
    }

    @Override
    public PostcardDetailDTO getPostcardDetail(PasswordDTO passwordDTO) {
        Postcard postcard = getPostcard(passwordDTO.getPasswd());
        log.info(postcard.toString());

        PostcardDetailDTO postcardDetailDTO = PostcardDetailDTO.builder()
                .id(postcard.getId())
                .postcardImg(postcard.getPostcardImg())
                .songTitle(postcard.getSong().getSongTitle())
                .singer(postcard.getSong().getSinger())
                .songUrl(postcard.getSong().getSongUrl())
                .regTime(postcard.getRegTime())
                .build();

        return postcardDetailDTO;
    }
}
