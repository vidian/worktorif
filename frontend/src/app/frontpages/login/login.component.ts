import { Component } from '@angular/core';
import { HttpClient, HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [HttpClientModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css',
})
export class LoginComponent {
  constructor(private http: HttpClient) {}

  signInWithGoogle() {
    this.nyelokLink();
  }

  public nyelokLink() {
    this.http
      .get('http://localhost:8000/api/login')
      .subscribe((response: any) => {
        console.log(response.pesan);
      });
  }

  username: string = '';

  signInLogin() {
    this.linkLogin();
  }

  public linkLogin() {
    const data = { text: this.username };
    this.http
      .post('http://localhost:8000/api/logout/', data)
      .subscribe((response: any) => {
        console.log(response.pesan);
      });
  }
}
