import { Component } from '@angular/core';
import { RouterModule, RouterOutlet } from '@angular/router';
import { HomepageComponent } from './frontpages/homepage/homepage.component';
import { LoginComponent } from './frontpages/login/login.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, HomepageComponent, RouterModule, LoginComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'frontend';
}
