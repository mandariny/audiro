package com.a402.audiropostcard.repository;

import com.a402.audiropostcard.entity.Spot;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.Repository;
import org.springframework.data.repository.query.Param;

public interface SpotRepository extends Repository<Spot, Long> {

    @Query(value = "select spot_id, name from Spot where spot_id = :spot_id", nativeQuery = true)
    Spot findById(@Param("song_id") long id);
}
