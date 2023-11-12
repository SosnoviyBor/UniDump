import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { AppComponent } from './app.component';
import { ValueDirective } from './value.directive';
@NgModule({
  imports: [BrowserModule, FormsModule],
  declarations: [AppComponent, ValueDirective],
  bootstrap: [AppComponent],
})
export class AppModule {}
