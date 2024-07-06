import { Routes } from '@angular/router';
import { HomepageComponent } from './frontpages/homepage/homepage.component';
import { LoginComponent } from './frontpages/login/login.component';

export const routes: Routes = [
    {
        path: '',
        component: HomepageComponent,
        title: 'Worktorif Homepage'
    },
    {
        path: 'login',
        component: LoginComponent,
        title: 'Login Page'
    }
];