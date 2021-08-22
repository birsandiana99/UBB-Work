package core.service;
import core.model.Books;
import java.util.List;
import java.util.Optional;

public interface BookService {
    Boolean addBook(Books book);

    Boolean removeBook(Long bookID);

    Boolean updateBook(Books updatedBook);

    List<Books> getAllBooks(Integer pageNumber, String sortBy, Integer noPerPage);

    List<Books>  filterByTitle(String searchString, Integer pageNumber, String sortBy,Integer noPerPage);

    List<Books>  filterByAuthor(String author, Integer pageNumber, String sortBy,Integer noPerPage);

    List<Books> sortByAuthorAndTitle(Integer pageNumber, Integer noPerPage);

    Optional<Books> findOne(Long bookId);
}
