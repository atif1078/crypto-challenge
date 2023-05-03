import { Component } from '@angular/core';
import axios from 'axios';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  currency: any = 'bitcoin';
  data: any[] = [];

  onClick() {
    if (this.currency === 'bitcoin') {
      this.currency = 'ethereum';
    } else {
      this.currency = 'bitcoin';
    }
    this.hitApi()
  }

  hitApi() {
    axios.get(`http://localhost:8000/api/crypto?currency=${this.currency}`)
      .then(response => {
        this.data = response.data[0];
        console.log(this.data)
      })
      .catch(error => {
        console.error(error);
      });
  }

  ngOnInit() {
    this.hitApi();
  }
}
