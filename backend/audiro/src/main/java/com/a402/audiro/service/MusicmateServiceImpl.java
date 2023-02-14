package com.a402.audiro.service;

import com.a402.audiro.dto.GiftThumbnailDTO;
import com.a402.audiro.dto.MusicmateDTO;
import com.a402.audiro.dto.MusicmateListDTO;
import com.a402.audiro.entity.Musicmate;
import com.a402.audiro.entity.User;
import com.a402.audiro.exception.MusicmateAlreadyExistException;
import com.a402.audiro.exception.MusicmateNotExistException;
import com.a402.audiro.repository.MusicmateRepository;
import com.a402.audiro.repository.UserRepository;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
@Slf4j
@RequiredArgsConstructor
public class MusicmateServiceImpl implements MusicmateService{

    private final MusicmateRepository musicmateRepository;
    private final UserRepository userRepository;
    private final UserService userService;


    @Override
    public List<MusicmateListDTO> getMusicmateList(long userId) {
        List<Long> musicmates;
        List<MusicmateListDTO> musicmateList;
        User user;

        try {
            musicmates = musicmateRepository.findByUserId(userId);
            musicmateList = musicmates.stream()
                    .map(m -> MusicmateListDTO.builder()
                            .id(userRepository.findById(m).getId())
                            .nickname(userRepository.findById(m).getNickname())
                            .img(userRepository.findById(m).getImg())
                            .build())
                    .collect(Collectors.toList());
        } catch (Exception e) {
            log.error(e.getMessage());
            throw e;
        }

        return musicmateList;
    }

    @Override
    public void followMusicmate(long mateId) {
        User user = userService.getUser();
        User mate = userService.getUser(mateId);

        isAlreadyMusicmate(user, mate);

        Musicmate musicmate = Musicmate.builder()
                .user(user)
                .mateUser(mate)
                .build();

        musicmateRepository.save(musicmate);
    }

    @Override
    public void isAlreadyMusicmate(User user, User mate) {
        Musicmate musicmate = musicmateRepository.findByUserIdAndMateId(user.getId(), mate.getId());
        if(musicmate != null) throw new MusicmateAlreadyExistException();
    }

    @Override
    public Musicmate getMusicmate(User user, User mate) {
        Musicmate musicmate = musicmateRepository.findByUserIdAndMateId(user.getId(), mate.getId());
        if(musicmate == null) throw new MusicmateNotExistException();
        return musicmate;
    }

    @Override
    public void unfollowMusicmate(long mateId) {
        User user = userService.getUser();
        User mate = userService.getUser(mateId);

        Musicmate musicmate = getMusicmate(user, mate);

        musicmateRepository.delete(musicmate);
    }

}
