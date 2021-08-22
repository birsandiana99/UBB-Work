package web.controller;

import core.model.Books;
import core.service.BookService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import web.converter.BookConverter;
import web.dto.BookDto;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

@RestController
public class BookController {
    public static final Logger logger = LoggerFactory.getLogger(BookController.class);

    @Autowired
    private BookService bookService;

    @Autowired
    private BookConverter bookConverter;

    @RequestMapping(value = "/books", method = RequestMethod.GET)
    public List<BookDto> getBooks(@RequestParam Optional<Integer> page,
                                  @RequestParam Optional<String> sortBy,
                                  @RequestParam Optional<Integer> perPage){
       logger.trace("getBooks: method entered --- pageNo={},sortBy={},perPage={}",page,sortBy,perPage);
       List<BookDto> booksDto;
       try {
           booksDto = bookService.getAllBooks(page.orElse(0), sortBy.orElse("id"), perPage.orElse(4))
                   .stream()
                   .map(b -> bookConverter.convertModelToDto(b))
                   .collect(Collectors.toList());
       }
       catch (Exception e){
           logger.trace("getBooks: FAILED, excMsg={}",e.getMessage());
           return new ArrayList<>();
       }
       logger.trace("getBooks: method finished --- return value List<BookDto>={}",booksDto);
       return booksDto;
    }

    @RequestMapping(value = "/books", method = RequestMethod.POST)
    public Boolean saveBook(@RequestBody BookDto bookDto){
        logger.trace("saveBook: method entered --- bookDto={}",bookDto);
        Boolean result;
        try {
            result = bookService.addBook(bookConverter.convertDtoToModel(bookDto));
        }
        catch (Exception e){
            logger.trace("saveBook: FAILED, excMsg={}",e.getMessage());
            return false;
        }
        logger.trace("saveBook: method finished --- result value Boolean={}", result);
        return result;
    }

    @RequestMapping(value = "/books/{id}", method = RequestMethod.PUT)
    public Boolean updateBook(@PathVariable Long id, @RequestBody BookDto bookDto){
        logger.trace("updateBook: method entered --- id ={}, bookDto={}",id,bookDto);
        Boolean result;
        try {
            result = bookService.updateBook(bookConverter.convertDtoToModel(bookDto));
        }
        catch (Exception e){
            logger.trace("updateBook: FAILED, excMsg={}",e.getMessage());
            return false;
        }
        logger.trace("updateBook: method finished --- result value Boolean={}", result);
        return result;
    }

    @RequestMapping(value ="/books/{id}", method = RequestMethod.DELETE)
    public Boolean removeBook(@PathVariable Long id){
        logger.trace("removeBook: method entered --- id ={}",id);
        Boolean result;
        try {
            result = bookService.removeBook(id);
        }
        catch (Exception e){
            logger.trace("removeBook: FAILED, excMsg={}",e.getMessage());
            return false;
        }
        logger.trace("removeBook: method finished --- result value Boolean={}", result);
        return result;
    }

    @RequestMapping(value = "/books-filter-title/{title}", method = RequestMethod.GET)
    public List<BookDto> getBooksFilterByTitle(@PathVariable String title,
                                               @RequestParam Optional<Integer> page,
                                               @RequestParam Optional<String> sortBy,
                                               @RequestParam Optional<Integer> perPage){
        logger.trace("getBooksFilterByTitle: method entered --- title={},page={},sortBy={}, perPage={}"
                ,title,page,sortBy,perPage);
        List<BookDto> booksDto;
        try {
            booksDto = bookService.filterByTitle(title,
                    page.orElse(0),
                    sortBy.orElse("title"),
                    perPage.orElse(4))
                    .stream()
                    .map(b -> bookConverter.convertModelToDto(b))
                    .collect(Collectors.toList());
        }
        catch (Exception e){
            logger.trace("getBooksFilteredByTitle: FAILED, eMSG={}",e.getMessage());
            return new ArrayList<>();
        }
        logger.trace("getBooksFilterByTitle: method finished --- return value List={}",booksDto);
        return booksDto;
    }

    @RequestMapping(value = "/books-filter-author/{author}", method = RequestMethod.GET)
    public List<BookDto> getBooksFilteredByAuthor(@PathVariable String author,
                                                  @RequestParam Optional<Integer> page,
                                                  @RequestParam Optional<String> sortBy,
                                                  @RequestParam Optional<Integer> perPage){
        logger.trace("getBooksFilterByAuthor: method entered --- author={},pageNo={},sortBy={}"
                ,author,page,sortBy);
        List<BookDto> booksDto;
        try {
            booksDto = bookService.filterByAuthor(author,page.orElse(0),sortBy.orElse("author"),perPage.orElse(4))
                    .stream()
                    .map(b -> bookConverter.convertModelToDto(b))
                    .collect(Collectors.toList());
        }
        catch (Exception e){
            logger.trace("getBooksFilteredByAuthor: FAILED, eMSG={}",e.getMessage());
            return new ArrayList<>();
        }
        logger.trace("getBooksFilterByAuthor: method finished --- return value List={}",booksDto);
        return booksDto;
    }

    @RequestMapping(value = "/books-sorted-ati", method = RequestMethod.GET)
    public List<BookDto> getBooksSortedByAuthorTitleAndId(@RequestParam Optional<Integer> page,@RequestParam Optional<Integer> perPage){
        logger.trace("getBooksSortedByAuthorTitleAndId: method entered --- pageNo={}",page);
        List<BookDto> booksDto =bookService.sortByAuthorAndTitle(page.orElse(0),perPage.orElse(4))
                .stream()
                .map(b->bookConverter.convertModelToDto(b))
                .collect(Collectors.toList());
        logger.trace("getBooksSortedByAuthorTitleAndId: method finished --- return value List={}",booksDto);
        return booksDto;
    }

    @RequestMapping(value = "/books-ret", method = RequestMethod.GET)
    public BookDto getBook(@RequestParam Optional<Long> id){
        Optional<Books> b = bookService.findOne(id.orElse(-1L));
        if(b.isPresent()){
            BookDto bookDto = BookDto.builder()
                    .author(b.get().getAuthor())
                    .title(b.get().getTitle())
                    .price(b.get().getPrice())
                    .build();
            bookDto.setId(b.get().getId());
            return bookDto;
        }
        BookDto s = new BookDto(""," sss",-2);
        s.setId(-1L);
        return s;
    }
}
