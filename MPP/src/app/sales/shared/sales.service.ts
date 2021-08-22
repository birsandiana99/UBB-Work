import {Injectable} from "@angular/core";
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Sales} from "./sales.model";

@Injectable()
export class SalesService {
  private salesURL = 'http://localhost:8080/api/sales';

  constructor(private  httpClient: HttpClient) {
  }

  getSales(noPage: number): Observable<Sales[]>{
    return this.httpClient
      .get<Array<Sales>>(`${this.salesURL}?page=${noPage}`);
  }

  addSale(bookID: number, clientID: number): Observable<any>{
    return this.httpClient
      .post(this.salesURL, [bookID,clientID]);
  }
}
