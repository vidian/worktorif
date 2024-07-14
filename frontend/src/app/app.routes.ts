import { Routes } from '@angular/router';
import { HomepageComponent } from './frontpages/homepage/homepage.component';
import { LoginComponent } from './frontpages/login/login.component';
import { CompanyComponent } from './user/company/company.component';
import { CompanyListComponent } from './user/company-list/company-list.component';

export const routes: Routes = [
  {
    path: '',
    component: HomepageComponent,
    title: 'Worktorif Homepage',
  },
  {
    path: 'login',
    component: LoginComponent,
    title: 'Login Page',
  },
  {
    path: 'company',
    component: CompanyComponent,
    title: 'Company Page',
  },
  {
    path: 'company/list',
    component: CompanyListComponent,
    title: 'Company List',
  },
];
