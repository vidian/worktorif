import { Component } from '@angular/core';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-company',
  standalone: true,
  imports: [FormsModule, HttpClientModule],
  templateUrl: './company.component.html',
  styleUrl: './company.component.css',
})
export class CompanyComponent {
  constructor(private http: HttpClient, private router: Router) {}

  companyname = '';
  companyreg = '';
  companyurl = '';
  companynumber = '';
  companyaddress = '';

  warnings = {
    companyname: false,
    companyreg: false,
    companyurl: false,
    companynumber: false,
    companyaddress: false,
  };

  submitCompany() {
    this.warnings.companyname = !this.companyname.trim();
    this.warnings.companyreg = !this.companyreg.trim();
    this.warnings.companyurl = !this.companyurl.trim();
    this.warnings.companynumber = !this.companynumber.toString().trim();
    this.warnings.companyaddress = !this.companyaddress.trim();

    const allValid = Object.values(this.warnings).every((warning) => !warning);

    if (allValid) {
      console.log('Form submitted successfully!');
      const data = {
        company_name: this.companyname,
        company_registration_number: this.companyreg,
        portal_url: this.companyurl,
        phone_number: this.companynumber,
        address: this.companyaddress,
      };

      this.http
        .post('http://localhost:8000/api/company_reg/', data)
        .subscribe((response: any) => {
          console.log(response.pesan);
        });

      this.router.navigate(['/company/list']);
    }
  }

  cancel() {
    window.location.reload();
  }
}
