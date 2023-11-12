import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { AppComponent } from './app.component';
import { SumDirective } from './sum.directive';
@NgModule({
  imports: [BrowserModule, FormsModule],
  declarations: [AppComponent, SumDirective],
  bootstrap: [AppComponent],
})
export class AppModule {}
