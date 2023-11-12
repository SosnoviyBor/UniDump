import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
import { BoldDirective } from './bold.directive';
import { ItalicDirective } from './italic.directive';
import { MouseboldDirective } from './mousebold.directive';
import { MouseitalicDirective } from './mouseitalic.directive';
import { HostmouseboldDirective } from './hostmousebold.directive';

@NgModule({
  imports: [BrowserModule],
  declarations: [
    AppComponent,
    BoldDirective,
    ItalicDirective,
    MouseboldDirective,
    MouseitalicDirective,
    HostmouseboldDirective,
  ],
  bootstrap: [AppComponent],
})
export class AppModule {}
