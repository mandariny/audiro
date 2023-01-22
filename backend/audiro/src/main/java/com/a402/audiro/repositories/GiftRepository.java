package com.a402.audiro.repositories;

import com.a402.audiro.entity.Gift;
import org.springframework.data.repository.Repository;

public interface GiftRepository extends Repository<Gift, Long> {

    Gift findById(long id);
    Gift findByUserId(long userId);
    void save(Gift gift);
    void delete(Gift gift);
}
