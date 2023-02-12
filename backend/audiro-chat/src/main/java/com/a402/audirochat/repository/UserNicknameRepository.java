package com.a402.audirochat.repository;

import com.a402.audirochat.entity.UserNickname;
import org.springframework.data.repository.Repository;

public interface UserNicknameRepository extends Repository<UserNickname, Long> {

    String findUserNicknameById(long id);
}
