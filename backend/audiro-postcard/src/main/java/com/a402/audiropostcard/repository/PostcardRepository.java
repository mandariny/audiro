package com.a402.audiropostcard.repository;

import com.a402.audiropostcard.entity.Postcard;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.Repository;
import org.springframework.data.repository.query.Param;

public interface PostcardRepository extends Repository<Postcard, Long> {

    @Query(value = "select * from postcard where password = :password", nativeQuery = true)
    Postcard findByPasswrod(@Param("password") String pw);

    void save(Postcard postcard);
}
