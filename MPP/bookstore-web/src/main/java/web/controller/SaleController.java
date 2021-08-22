package web.controller;

import core.model.Books;
import core.model.Clients;
import core.model.Sales;
import core.service.BookService;
import core.service.ClientService;
import core.service.SaleService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.web.bind.annotation.*;
import web.dto.SaleDto;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;


@RestController
public class SaleController {
    public static final Logger logger = LoggerFactory.getLogger(SaleController.class);

    @Autowired
    private ClientService clientService;

    @Autowired
    private BookService bookService;


    @RequestMapping(value = "/sales", method = RequestMethod.GET)
    public List<SaleDto> getSales(@RequestParam Optional<Integer> page,@RequestParam Optional<Integer> perPage){
        try {
            logger.trace("getSales:  method entered --- noPage={}",page);
            List<SaleDto> salesDto = new ArrayList<>();
            int pageNo = 0;
            while(clientService.getAllClients(pageNo,"id",1).size() != 0){
                clientService.getAllClients(pageNo, "id", 1)
                        .forEach(client ->
                                client.getSales()
                                        .forEach(sale -> {
                                            salesDto.add(
                                                    SaleDto.builder()
                                                            .authorName(sale.getBook().getAuthor())
                                                            .bookName(sale.getBook().getTitle())
                                                            .clientName(sale.getClient().getName())
                                                            .bookid(sale.getBook().getId())
                                                            .clientid(sale.getClient().getId())
                                                            .build()
                                            );

                                        }));
                pageNo++;
            }
            logger.trace("getSales: method finished --- return value List={}", salesDto);
            return salesDto;
        }
        catch (Exception e){
            logger.trace("getSale: FAILED , error={}",e.getMessage());
            return new ArrayList<>();
        }
    }

    @RequestMapping(value = "/sales", method = RequestMethod.POST)
    @Transactional
    public Boolean saveSale(@RequestBody ArrayList<Long> data){
        try {

            Long bookID = data.get(0);
            Long clientID = data.get(1);
            logger.trace("saveSale: method entered --- bookID={}, clientID={}", bookID, clientID);
            Boolean result= false;
            Optional<Clients> client = clientService.findOne(clientID);
            if(client.isPresent()){
                Sales sale = new Sales();
                sale.setClient(client.get());
                Optional<Books> book = bookService.findOne(bookID);
                if(book.isPresent()){
                    sale.setBook(book.get());
                    result=true;
                    bookService.findOne(bookID).get().addSale(sale);
                    client.get().addSale(sale);
                }
            }
            logger.trace("saveSale: method finished --- return value Boolean={}", result);
            return result;
        }
        catch (Exception e){
            logger.trace("saveSale: FAILED, error={}",e.getMessage());
            return false;
        }
    }
}
