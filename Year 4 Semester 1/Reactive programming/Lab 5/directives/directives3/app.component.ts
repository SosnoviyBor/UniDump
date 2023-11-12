import { Component } from '@angular/core';

@Component({
  selector: 'my-app',
  template: `<div>
    <p
      valuesize
      [selectedSize]="'28px'"
      [defaultSize]="'14px'"
      [parentFontSize]="parentFontSize"
    >
      Hello Angular
    </p>
    <p>Angular представляє модульну архітектуру додатку</p>
    <p>
      Введіть розмір шрифта:
      <input
        type="text"
        [(ngModel)]="parentFontSize"
        placeholder="Enter font size"
      />
    </p>
    <p
      valuesize
      [parentFontSize]="parentFontSize + 'px'"
      [defaultSize]="'14px'"
    >
      Розмір шрифта зараз {{ parentFontSize }}px
    </p>
  </div>`,
})
export class AppComponent {
  parentFontSize: string;
}
