import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { AppComponent } from './app.component';
import { OtherIfDirective } from './otherIf.directive';
@NgModule({
  imports: [BrowserModule, FormsModule],
  declarations: [AppComponent, OtherIfDirective],
  bootstrap: [AppComponent],
})
export class AppModule {}
