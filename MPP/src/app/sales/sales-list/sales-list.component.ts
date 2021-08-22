import { Component, OnInit } from '@angular/core';
import {Router} from "@angular/router";
import {SalesService} from "../shared/sales.service";
import {Sales} from "../shared/sales.model";

@Component({
  selector: 'app-sales-list',
  templateUrl: './sales-list.component.html',
  styleUrls: ['./sales-list.component.css']
})
export class SalesListComponent implements OnInit {
  errorMessage: string;
  salesArr: Array<Sales>;
  selectedSale: Sales;
  currentPage: number;
  constructor(private salesService: SalesService,
              private router: Router) { }


  ngOnInit(): void {
    this.currentPage = 0;
    this.getSales();
  }

   getSales(): void {
    this.salesService
      .getSales(this.currentPage)
      .subscribe(
        response => {
          this.salesArr = response;
        }
      )
  }

  nextPage() {
    this.currentPage ++;
    this.salesService
      .getSales(this.currentPage)
      .subscribe(
        response => {
          if(response.length == 0){
            alert("This is the last page");
            this.currentPage--;
            this.getSales();
          }
          this.salesArr = response;
        }
      )
  }

  prevPage() {
    this.currentPage--;
    if(this.currentPage < 0){
      alert("This is the first page");
      this.currentPage++;
      return;
    }
    this.getSales();
  }
}
