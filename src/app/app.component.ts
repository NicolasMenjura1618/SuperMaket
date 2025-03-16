import { Component, OnInit } from '@angular/core';
import { ProductService } from './product.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'superMarket';
  productos: any[] = [];

  constructor(private productService: ProductService) {}

  ngOnInit() {
    this.productService.getProducts().subscribe({
      next: (data) => {
        this.productos = data.productos; // Adjust based on the API response structure
      },
      error: (error) => {
        console.error('Error fetching products:', error);
        this.productos = []; // Handle the error case
      }
    });
  }
}
