package core.repository;

import core.model.Clients;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.Query;

public interface ClientRepository extends BookStoreRepo<Clients, Long> {

    // RETRIEVES CLIENTS USING PAGING
    // CLIENTS WILL BE SORTED BASED ON
    // GIVEN CRITERIA, DEFAULT = ID
    @Query("select c from Clients c")
    Page<Clients> getClients(Pageable pageable);


    // RETRIEVES CLIENTS FILTERED BY NAME
    // USING PAGING AND SORTED BASES ON
    // GIVEN CRITERIA, DEFAULT = ID
    @Query("select c from Clients c where  c.name like %?1%")
    Page<Clients> filterByName(String name, Pageable pageable);

    // RETRIEVES MAXIMUM CLIENT ID
    @Query("select max(c.id) from  Clients  c")
    Integer getMaxId();
}
