import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { AppComponent } from './app.component';
import { WhileDirective } from './while.directive';
@NgModule({
  imports: [BrowserModule, FormsModule],
  declarations: [AppComponent, WhileDirective],
  bootstrap: [AppComponent],
})
export class AppModule {}
