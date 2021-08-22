package core.repository;

import core.model.Books;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.Query;

public interface BookRepository  extends BookStoreRepo<Books,Long>{

    // FILTER BY AUTHOR, USING PAGING
    // RESULTS SORTED in ascending order
    // based on a user given criteria
    @Query("select  b from Books b where b.author like %?1%")
    Page<Books>  findByAuthor(String author, Pageable pageable);

    // FILTER BY TITLE, USING PAGING
    // RESULTS SORTED IN ASCENDING ORDER
    // BASED ON A USER GIVEN CRITERIA
    @Query("select b from Books b where b.title like %?1%")
    Page<Books> findByTitle(String title, Pageable pageable);


    // GET ALL BOOKS USING PAGING
    // RESULT WILL BE SORTED IN
    // ASC ORDER AND BASED ON SOME
    // USER ENTERED CRITERIA
    // DEFAULT SORT CRITERIA: ID
    @Query("select b from Books b")
    Page<Books> getBooks(Pageable pageable);


    // GET MAX ID
    @Query("select max(b.id) from Books b")
    Integer getMaxId();
}
