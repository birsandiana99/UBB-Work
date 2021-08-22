import { Component, OnInit } from '@angular/core';
import {Client} from "../shared/clients.model";
import {ClientsService} from "../shared/clients.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-client-list',
  templateUrl: './client-list.component.html',
  styleUrls: ['./client-list.component.css']
})
export class ClientListComponent implements OnInit {
  errorMessage: string;
  clients: Array<Client>;
  selectedClient: Client;
  currentPage: number;
  constructor(private clientService: ClientsService,
              private router: Router) { }

  ngOnInit(): void {
    this.currentPage = 0;
    this.getClients();
  }

  getClients() {
    this.clientService.getClients()
      .subscribe(
        clients => {console.log(clients);
          this.clients = clients},
        error => this.errorMessage = <any> error
      );
  }

  onSelect(client: Client): void{
    this.selectedClient = client;
  }

  goToClientDetail(){
    console.log(this.selectedClient);
    this.router.navigate(['/clients/detail', this.selectedClient.id]);
  }

  removeClient(client: Client){
    this.clientService.deleteClient(client.id)
      .subscribe(_ =>{
        this.clients = this.clients.filter(c=> c.id !== client.id);
      })
  }

  nextPage() {
    this.currentPage++;
    this.clientService.getClientsOnPage(this.currentPage, "name")
      .subscribe(
        clients => {console.log(clients);
          if(clients.length === 0){
            alert("LAST PAGE");
            this.currentPage--;
            return;
          }
          this.clients = clients
        },
        error => this.errorMessage = <any> error
      );
  }

  prevPage() {
    if(this.currentPage===0){
      alert("FIRST PAGE");
      return;
    }
    this.currentPage--;
    this.clientService.getClientsOnPage(this.currentPage,"name")
      .subscribe(
        clients => {console.log(clients);
          this.clients = clients},
        error => this.errorMessage = <any> error
      );
  }
}
