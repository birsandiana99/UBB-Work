import {Component, Input, OnInit} from '@angular/core';
import {Book} from "../shared/book.model";
import {BookService} from "../shared/boook.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-book-list',
  templateUrl: './book-list.component.html',
  styleUrls: ['./book-list.component.css']
})
export class BookListComponent implements OnInit {
  @Input() sortBook: string;
  errorMessage: string;
  books: Array<Book>;
  selectedBook: Book;
  currentPage: number;
  constructor(private bookService: BookService,
              private router: Router) { }

  ngOnInit(): void {
    this.sortBook = "Sort key..";
    this.currentPage = 0;
    this.getBooks();
  }

  getBooks(){
    this.bookService.getBooks()
      .subscribe(
        books => this.books = books,
        error => this.errorMessage = error
      );
  }

  onSelect(book: Book){
    this.selectedBook = book;
  }

  removeBook(book: Book){
    this.bookService
      .deleteBook(book.id)
      .subscribe( _ => {
        this.books = this.books.filter(b => b.id !== book.id);
      });
  }

  goToBookDetail(){
    this.router.navigate(['/books/detail', this.selectedBook.id]);
  }

  prevPage() {
    if(this.currentPage===0){
      alert("FIRST PAGE");
      return;
    }
    this.currentPage--;
    this.bookService.getBooksOnPage(this.currentPage,"author")
      .subscribe(
        books => this.books = books,
        error => this.errorMessage = error
      );

  }

  nextPage() {
    this.currentPage++;
    this.bookService.getBooksOnPage(this.currentPage,"author")
      .subscribe(
        books => {
          if(books.length===0){
            alert("LAST PAGE");
            this.currentPage--;
            return;
          }
          this.books = books
        }
        ,
        error => this.errorMessage = error
      );
  }

  doFiltering(val: string): void {
      this.sortBook =val;
      console.log("entered do filtering with:"+this.sortBook);
      if(this.sortBook===""){
        this.currentPage=0;
        this.getBooks();
        return;
      }
      console.log(this.sortBook);
      this.bookService
        .getBooksOnPage(0,this.sortBook)
        .subscribe(
          (resp) =>{
            if(resp.length === 0){
               alert("No books meet the sorting criteria");
               this.currentPage=0;
               return;
            }
            this.currentPage=0;
            this.books = resp;
          }
        )
  }
}

