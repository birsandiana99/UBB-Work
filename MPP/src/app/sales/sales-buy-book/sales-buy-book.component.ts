import { Component, OnInit } from '@angular/core';
import {Client} from "../../clients/shared/clients.model";
import {ClientsService} from "../../clients/shared/clients.service";
import {Router} from "@angular/router";
import {BookService} from "../../books/shared/boook.service";
import {Book} from "../../books/shared/book.model";
import {SalesService} from "../shared/sales.service";
import {Location} from "@angular/common";

@Component({
  selector: 'app-sales-buy-book',
  templateUrl: './sales-buy-book.component.html',
  styleUrls: ['./sales-buy-book.component.css']
})
export class SalesBuyBookComponent implements OnInit {

  errorMessage: string;
  clients: Array<Client>;
  selectedClient: Client;
  selectedBook: Book;
  booksArr: Array<Book>;
  currentPageClients: number;
  currentPageBooks: number;
  clientFilter: string;
  bookFilter: string;
  constructor(private clientService: ClientsService,
              private router: Router,
              private bookService: BookService,
              private salesService: SalesService,
              private location: Location) { }


  ngOnInit(): void {
    this.clientFilter = "";
    this.currentPageClients = 0;
    this.currentPageBooks = 0;
    this.getClients();
    document
      .getElementById("book-cont-buy")
      .style
      .display ="none";
  }

  getClients(): void {
    this.clientService
      .getClients()
      .subscribe(result =>{
        this.clients = result;
      },
      error => {
        this.errorMessage = error;
      });
  }

  getBooks(): void{
    this.bookService
      .getBooks()
      .subscribe(result =>{
          this.booksArr = result;
        },
        error => {
          this.errorMessage = error;
        });
  }


  onSelect(client: Client) {
    document
      .getElementById("cl-cont-buy")
      .style
      .display = "none";
    this.selectedClient = client;
    document
      .getElementById("book-cont-buy")
      .style
      .display ="block";
    this.getBooks();
  }

  buyBook(): void{
      this.salesService
        .addSale(this.selectedBook.id, this.selectedClient.id)
        .subscribe(result =>{
          alert("Operation result: "+result);
        });
      this.location.back();
  }

  onSelectBook(book: Book): void {
    this.selectedBook = book;
  }

  nextPageClients(): void {
    this.currentPageClients++;
    if(/[a-z]/i.test(this.clientFilter)){
      console.log(`next page for filter value: ${this.clientFilter}`);
      this.clientService
        .getClientsFilteredByName(this.currentPageClients,this.clientFilter)
        .subscribe(result=> {
          if (result.length === 0) {
            alert("Last result page!");
            this.currentPageClients--;
            return;
          }
          this.clients = result;
        });
      return;
    }
    this.clientService
      .getClientsOnPage(this.currentPageClients, "name")
      .subscribe(result =>{
          if(result.length===0){
            alert("Last result page!");
            this.currentPageClients--;
            return;
          }
          this.clients = result;
        },
        error => {
          this.errorMessage = error;
        });

  }

  prevPageClients(): void{
    if(this.currentPageClients === 0){
      alert("First result page");
      return;
    }
    this.currentPageClients --;
    if(/[a-z]/i.test(this.clientFilter)){
      console.log(`prev page for filter value: ${this.clientFilter}`);
      this.clientService
        .getClientsFilteredByName(this.currentPageClients,this.clientFilter)
        .subscribe(resp=>this.clients=resp);
      return;
    }
    this.clientService
      .getClientsOnPage(this.currentPageClients, "name")
      .subscribe(result =>{
          this.clients = result;
        },
        error => {
          this.errorMessage = error;
        });
  }

  nextPageBooks() {
    //TODO
    this.currentPageBooks ++;
    if(/[a-z]/i.test(this.bookFilter)){
      console.log("NEXT PAGE: SHOULD DO FILTER BASED ON"+this.bookFilter);
      this.bookService
        .getBooksFiltered(this.currentPageBooks,this.bookFilter)
        .subscribe(resp=>{
          if(resp.length===0){
            alert("Last result page");
            this.currentPageBooks--;
            return;
          }
          this.booksArr=resp;
        });
      return;
    }

    this.bookService
      .getBooksOnPage(this.currentPageBooks, "title")
      .subscribe(result =>{
          if(result.length === 0){
            alert("This is the last result page!");
            this.currentPageBooks--;
            return;
          }
          this.booksArr = result;
        },
        error => {
          this.errorMessage = error;
        });
  }

  prevPageBooks() {
    if(this.currentPageBooks === 0){
      alert("First result page");
      return;
    }
    this.currentPageBooks--;
    if(/[a-z]/i.test(this.bookFilter)){
      console.log("PREV PAGE: SHOULD DO FILTER BASED ON"+this.bookFilter);
      this.bookService
        .getBooksFiltered(this.currentPageBooks,this.bookFilter)
        .subscribe(resp=>this.booksArr=resp);
      return;
    }
    this.bookService
      .getBooksOnPage(0,"title")
      .subscribe(resp=>this.booksArr=resp);
  }

  doClientFilter(value: string) {
    console.log(`Entered with value=${value}`);
    this.currentPageClients = 0;
    if(/[a-z]/i.test(value)){
      console.log(`${value}Should be filtered`);
      this.clientFilter = value;
      this.clientService
        .getClientsFilteredByName(0,value)
        .subscribe( resp => this.clients=resp);
      return;
    }
    else{
      this.clientFilter="";
      this.clientService
        .getClientsOnPage(0,"name")
        .subscribe(resp => this.clients=resp);
    }
  }

  doBookFilter(filterValue: string) {
    console.log(`Entered with title filter=${filterValue}`);
    this.currentPageBooks=0;
    if(/[a-z]/i.test(filterValue)){
      console.log("SHOULD DO FILTER BASED ON"+filterValue);
      this.bookFilter=filterValue;
      this.bookService
        .getBooksFiltered(0,this.bookFilter)
        .subscribe(resp=>this.booksArr=resp);
      return;
    }
    this.bookFilter="";
    this.bookService
      .getBooksOnPage(0,"title")
      .subscribe(resp=>this.booksArr=resp);
  }
}



