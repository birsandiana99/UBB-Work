package core.service;

import core.model.Clients;
import core.model.validators.ClientValidator;
import core.repository.ClientRepository;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.concurrent.atomic.AtomicBoolean;


@Service
public class ClientServiceImp implements ClientService {
    public static final Logger logger = LoggerFactory.getLogger(ClientServiceImp.class);

    @Autowired
    private ClientValidator validator;

    @Autowired
    private ClientRepository repository;

    @Override
    public Boolean addClient(Clients client) {
        try {
            logger.trace("addClient:  entered method --- addClient(client={})", client);
            AtomicBoolean val = new AtomicBoolean(true);
            validator.validate(client);
            client.setId(getNextId());
            repository.findById(client.getId()).ifPresentOrElse((i) -> val.set(true), () -> val.set(false));
            if (val.get()) {
                logger.trace("addClient:  finished method --- return value boolean={} --- id already exists", !val.get());
                return !val.get();
            }
            repository.save(client);
            repository.findById(client.getId()).ifPresentOrElse((i) -> val.set(true), () -> val.set(false));
            logger.trace("addClient:  finished method --- return value boolean={}", val.get());
            return val.get();
        }
        catch (Exception exc){
            logger.trace("addClient -- failed with Exception: {}", exc.getMessage());
            return false;
        }
    }

    @Override
    public Boolean removeClient(Long id) {
        try {
            logger.trace("removeClient:  entered method --- removeClient(id={})", id);
            repository.deleteById(id);
            AtomicBoolean val = new AtomicBoolean(true);
            repository.findById(id).ifPresentOrElse((i) -> val.set(false), () -> val.set(true));
            logger.trace("removeClient:  finished method --- return value boolean={}", val.get());
            return val.get();
        }
        catch (Exception exc){
            logger.trace("removeClient -- failed with Exception: {}", exc.getMessage());
            return false;
        }
    }

    @Override
    @Transactional
    public Boolean updateClient(Clients updatedClient) {
        try {
            logger.trace("updateClient:  entered method updateClient(updatedClient={})", updatedClient);
            AtomicBoolean atomicBoolean = new AtomicBoolean(false);
            repository.findById(updatedClient.getId())
                    .ifPresentOrElse((client) -> {
                        client.setMoneySpent(updatedClient.getMoneySpent());
                        client.setName(updatedClient.getName());
                        atomicBoolean.set(true);
                    }, () -> atomicBoolean.set(false));
            logger.trace("updateClient:  method finished --- return value boolean={}", atomicBoolean.get());
            return atomicBoolean.get();
        }
        catch (Exception exc){
            logger.trace("updateClient -- failed with Exception: {}", exc.getMessage());
            return false;
        }
    }

    @Override
    public List<Clients> getAllClients(Integer pageNo, String sortBy, Integer noPerPage){
        logger.trace("getAllClients:  method entered --- getAllClients(pageNo={},sortBy={},noPerPage={})",pageNo,sortBy,noPerPage);
        List<Clients> clients;
        try {
            clients = repository.getClients(PageRequest.of(pageNo,noPerPage, Sort.Direction.ASC, sortBy))
                    .getContent();
        }
        catch (Exception exc){
            logger.trace("getAllClients -- failed with Exception: {}", exc.getMessage());
            return new ArrayList<>();
        }
        logger.trace("getAllClients:  method finished --- return value list<client>={}",clients);
        return clients;
    }

    /*
    @Override
    public List<Clients> clientsSortedAlphabetically() {
        logger.trace("clientsSortedAlphabetically:   method entered --- clientsSortedAlphabetically()");
        List<Clients> clients = repository
                .findAll()
                .stream()
                .sorted(Comparator.comparing(Clients::getName))
                .collect(Collectors.toList());
        logger.trace("clientsSortedAlphabetically:  method finished --- return value list<client>={}", clients);
        return clients;
    }
    */
    /*
    @Override
    public List<Clients> clientsSortedByMoneySpent() {
        logger.trace("clientsSortedByMoneySpent:  method entered --- clientsSortedByMoneySpent()");
        List<Clients> clients = repository
                .findAll()
                .stream()
                .sorted(Comparator.comparing(Clients::getMoneySpent).reversed())
                .collect(Collectors.toList());
        logger.trace("clientsSortedByMoneySpent:  method finished --- return value list<client>={}",clients);
        return clients;
    }
    */

    @Override
    public List<Clients> filterByName(String searchString, Integer pageNo, String sortBy,Integer noPerPage) {
        logger.trace("filterByName: method entered --- filterByName(searchString={},pageNo={},sortBy={},noPerPage={})"
                ,searchString, pageNo, sortBy,noPerPage);

        List<Clients> clients;
        try {
            clients = repository.filterByName(searchString, PageRequest.of(pageNo,4, Sort.Direction.ASC, sortBy))
                    .getContent();
        }
        catch (Exception exc){
            logger.trace("filterByName -- failed with Exception: {}", exc.getMessage());
            return new ArrayList<>();
        }
        logger.trace("filterByName: method finished --- return value list<client>={}", clients);
        return clients;
    }
    /*
    @Override
    public List<Clients> sortByNameAndID(I) {
        logger.trace("sortByNameAndID:  method entered  --- sortByNameAndID()");
        Sort sortObject = new Sort(Boolean.FALSE,"name")
                .and(new Sort("id"));
        SortAlgorithm<Long, Clients> algorithm = new SortAlgorithm<>(repository.findAll(), sortObject);
        List<Clients> sorted = algorithm.sort();
        logger.trace("sortByNameAndID:  method finished --- return value list<client>={}", sorted);
        return sorted;
    }*/

    @Override
    @Transactional
    public Optional<Clients> findOne(Long id) {
        logger.trace("findOne:  entered method  --- id={}", id);
        Optional<Clients> r;
        try {
            r = repository.findById(id);
            logger.trace("findOne:  method finished --- return value optional<client>=}{}", r);
        }
        catch (Exception e){
            logger.trace("findOne: FAILED, error={}",e.getMessage());
            return Optional.empty();
        }
        return r;
    }

    private Long getNextId(){
        try {
            if (getAllClients(1, "id",2).size() == 0)
                return 1L;
        /*
        Long id = getAllClients()
                .stream()
                .map(c->c.getId())
                .max(Comparator.naturalOrder())
                .get();*/
            return Long.valueOf(repository.getMaxId()) + 1;
        }
        catch (Exception e){
            return -2L;
        }
    }
}
