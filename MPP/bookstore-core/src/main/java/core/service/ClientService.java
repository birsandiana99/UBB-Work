package core.service;

import core.model.Clients;

import java.util.List;
import java.util.Optional;

public interface ClientService {
    Boolean addClient(Clients client);

    Boolean removeClient(Long id);

    Boolean updateClient(Clients updatedClient);

    List<Clients> getAllClients(Integer pageNo, String sortBy, Integer noPerPage);

    /*
    List<Clients> clientsSortedAlphabetically();

    List<Clients> clientsSortedByMoneySpent();

     */

    List<Clients>  filterByName(String searchString, Integer pageNo, String sortBy, Integer noPerPage);

    // List<Clients> sortByNameAndID(Integer pageNo);

    Optional<Clients> findOne(Long id);
}
