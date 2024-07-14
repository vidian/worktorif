import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-company-list',
  standalone: true,
  imports: [HttpClientModule, CommonModule],
  templateUrl: './company-list.component.html',
  styleUrl: './company-list.component.css',
})
export class CompanyListComponent implements OnInit {
  constructor(private http: HttpClient) {}

  companies: any[] = [];

  ngOnInit(): void {
    this.http
      .get('http://localhost:8000/api/companies/')
      .subscribe((response: any) => {
        this.companies = response;
      });
  }
}
