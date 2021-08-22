package web.controller;

import core.model.Clients;
import core.service.ClientService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;

import org.springframework.web.bind.annotation.*;
import web.converter.ClientConverter;
import web.dto.ClientDto;

import javax.swing.text.html.Option;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

@RestController
public class ClientController {
    public static final Logger logger = LoggerFactory.getLogger(ClientController.class);

    @Autowired
    private ClientService clientService;

    @Autowired
    private ClientConverter clientConverter;


    @RequestMapping(value = "/clients", method = RequestMethod.GET)
    public List<ClientDto> getAll(@RequestParam Optional<Integer> page,
                                  @RequestParam Optional<String> sortBy,
                                  @RequestParam Optional<Integer> perPage){

        logger.trace("getAll:  method entered ---page={},sortBy={}",page,sortBy);
        List<ClientDto>  clientsDto;
        try {
            clientsDto = clientService
                    .getAllClients(page.orElse(0), sortBy.orElse("id"), perPage.orElse(4))
                    .stream()
                    .map(c -> clientConverter.convertModelToDto(c))
                    .collect(Collectors.toList());
        }
        catch (Exception exc){
            logger.trace("clientsDto: FAILED errorMsg={}",exc.getMessage());
            return new ArrayList<>();
        }
        logger.trace("getAll:  method finished --- return value List={}", clientsDto);
        return clientsDto;
    }

    @RequestMapping(value = "/clients", method = RequestMethod.POST)
    public Boolean saveClient(@RequestBody ClientDto clientDto){
        logger.trace("saveClient:   method entered  --- saveClient(clientDto={})",clientDto);
        Boolean result;
        try {
            result = clientService.addClient(clientConverter.convertDtoToModel(clientDto));
        }
        catch (Exception e){
            logger.trace("saveClient: FAILED, msg={}",e.getMessage());
            return false;
        }
        logger.trace("saveClient:   method finished --- return value Boolean={}",result);
        return result;
    }

    @RequestMapping(value = "/clients/{id}", method = RequestMethod.PUT)
    public Boolean updateClient(@PathVariable Long id, @RequestBody ClientDto clientDto){
        logger.trace("updateClient:  method entered --- updateClient(id={}, clientDto={})", id, clientDto);
        Boolean result;
        try {
            result = clientService.updateClient(clientConverter.convertDtoToModel(clientDto));
        }
        catch (Exception e){
            logger.trace("updateClient: FAILED, msg={}",e.getMessage());
            return false;
        }
        logger.trace("updateClient:  method finished --- return value Boolean={}", result);
        return result;
    }

    @RequestMapping(value = "/clients/{id}", method = RequestMethod.DELETE)
    public Boolean removeClient(@PathVariable Long id){
        logger.trace("removeClient:  method entered --- removeClient(id={})", id);
        Boolean result;
        try {
            result = clientService.removeClient(id);
        }
        catch (Exception e){
            logger.trace("removeClient: FAILED, msg={}",e.getMessage());
            return false;
        }
        logger.trace("removeClient:  method finished --- return value boolean={}",result);
        return result;
    }

    @RequestMapping(value = "/clients-sorted", method = RequestMethod.GET)
    public List<ClientDto> clientsSortedAlphabetically(@RequestParam Optional<Integer> page,
                                                       @RequestParam Optional<String> sortBy,
                                                       @RequestParam Optional<Integer> perPage){
        logger.trace("clientsSortedAlphabetically:  method entered -page={},sortBy={}",page,sortBy);
        List<ClientDto> clientsDto;
        try {
            clientsDto = clientService
                    .getAllClients(page.orElse(0), sortBy.orElse("id"),perPage.orElse(4))
                    .stream()
                    .map(c -> clientConverter.convertModelToDto(c))
                    .collect(Collectors.toList());
        }
        catch (Exception e){
            logger.trace("saveClient: FAILED, msg={}",e.getMessage());
            return new ArrayList<>();
        }
        logger.trace("clientsSortedAlphabetically: method finished --- return value List={}", clientsDto);
        return clientsDto;
    }



    @RequestMapping(value = "/clients-filter-name/{name}", method = RequestMethod.GET)
    public List<ClientDto> filterByName(@PathVariable String name,
                                        @RequestParam Optional<Integer> page,
                                        @RequestParam Optional<String> sortBy,
                                        @RequestParam Optional<Integer> perPage){
        logger.trace("filterByName: method entered --- filterByName(name={},page={},sortBy={})",
                name, page, sortBy);
        List<ClientDto> clientsDto;
        try {
            clientsDto = clientService.filterByName(name, page.orElse(0), sortBy.orElse("name"),perPage.orElse(4))
                    .stream()
                    .map(c -> clientConverter.convertModelToDto(c))
                    .collect(Collectors.toList());
        }
        catch (Exception e){
            logger.trace("filterByName: FAILED, msg={}",e.getMessage());
            return new ArrayList<>();
        }
        logger.trace("filterByName: method finished --- return value List={}", clientsDto);
        return clientsDto;
    }

    @RequestMapping(value = "/clients-ret", method = RequestMethod.GET)
    public ClientDto getClient(@RequestParam Optional<Long> id){
        Optional<Clients> cl = clientService.findOne(id.orElse(-1L));
        if(cl.isPresent()){
            ClientDto  d = ClientDto.builder()
                    .name(cl.get().getName())
                    .moneySpent(cl.get().getMoneySpent())
                    .build();
            d.setId(cl.get().getId());
            return d;
        }
        ClientDto  d= new ClientDto("  ", -10);
        d.setId(-1L);
        return d;
    }
}
