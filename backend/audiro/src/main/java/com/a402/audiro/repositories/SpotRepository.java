package com.a402.audiro.repositories;

import com.a402.audiro.entity.Spot;
import org.springframework.data.repository.Repository;

public interface SpotRepository extends Repository<Spot, Long> {

    Spot findById(long id);
}
