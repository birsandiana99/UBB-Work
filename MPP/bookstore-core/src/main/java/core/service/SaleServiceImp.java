package core.service;

import core.model.Books;
import core.model.Clients;
import core.model.Sales;
import core.repository.BookRepository;
import core.repository.ClientRepository;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.ArrayList;
import java.util.List;

@Service
public class SaleServiceImp implements SaleService {
    public static final Logger  logger = LoggerFactory.getLogger(SaleServiceImp.class);

    @Autowired
    private BookRepository bookRepository;

    @Autowired
    private ClientRepository clientRepository;


    @Override
    public List<Sales> getAllSales() {
        logger.trace("getAllSales: method entered");
        List<Sales> res = new ArrayList<>();
        try{
           clientRepository.findAll()
                   .forEach(c -> {
                       c.getSales().forEach(s->res.add(s));
                   });
        }
        catch (Exception e){
            logger.trace("getAllSales: exception={}",e.getMessage());
            return new ArrayList<>();
        }
        return res;
    }

    @Override
    @Transactional
    public Boolean buyBook(Long clientID, Long bookId) {
        logger.trace("buyBook: entered with: {},{}",clientID,bookId);
        try{
            Sales sale = new Sales();
            Books b = bookRepository.findById(bookId).get();
            Clients c = clientRepository.findById(clientID).get();
            c.setMoneySpent(b.getPrice()+c.getMoneySpent());
            sale.setBook(b);
            sale.setClient(c);
            b.addSale(sale);
            c.addSale(sale);
        }
        catch (Exception e){
            logger.trace("buyBook: failed, err={}",e.getMessage());
            return false;
        }
        logger.trace("buyBook: finished,returned={}",false);
        return true;
    }

}
