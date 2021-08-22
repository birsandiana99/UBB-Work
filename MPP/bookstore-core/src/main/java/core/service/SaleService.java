package core.service;

import core.model.Sales;

import java.util.List;

public interface SaleService {
    List<Sales> getAllSales();

    Boolean buyBook(Long clientID, Long bookId);
}
