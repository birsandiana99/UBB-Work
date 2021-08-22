package core.repository;
import core.model.Sales;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.Query;


public interface SaleRepository{

    @Query("select s from Sales  s")
    Page<Sales> getSales(Pageable pageable);

    @Query("select max(s.id) from Sales s")
    Integer getMaxId();
}
