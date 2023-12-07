import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { AppComponent } from './app.component';
import { ChangesizeDirective } from './changesize.directive';
@NgModule({
  imports: [BrowserModule, FormsModule],
  declarations: [AppComponent, ChangesizeDirective],
  bootstrap: [AppComponent],
})
export class AppModule {}
