import { Component } from '@angular/core';
@Component({
  selector: 'my-app',
  template: `
    <div>Без форматування: {{ myDate }}</div>
    <div>З форматуванням: {{ myDate | date }}</div>
    <div>{{ welcome | uppercase }}</div>
    <div>{{ welcome | lowercase }}</div>
    <div>{{ persentage | percent }}</div>
    <div>{{ persentage | currency }}</div>
    <div>{{ welcome | slice : 3 }}</div>
    <div>{{ welcome | slice : 6 : 11 }}</div>
    <div>{{ myNewDate | date : 'dd/MM/yyyy' }}</div>
    <div>{{ pi | number : '2.1-2' }}</div>
    <div>{{ pi | number : '3.5-5' }}</div>
    <div>{{ money | currency : 'UAH' : 'code' }}</div>
    <div>{{ money | currency : 'UAH' : 'symbol-narrow' }}</div>
    <div>{{ money | currency : 'UAH' : 'symbol' : '1.1-1' }}</div>
    <div>{{ money | currency : 'UAH' : 'symbol-narrow' : '1.1-1' }}</div>
    <div>{{ money | currency : 'UAH' : 'Тільки сьогодні за ціною ' }}</div>
    <div>{{ message | slice : 6 : 11 | uppercase }}</div>
    <div>
      Число до форматування: {{ x }}<br/>
      Число після форматування: {{ x | format }}
    </div>
    <hr />
    <div>{{ users | join }}</div>
    <div>{{ users | join : 1 }}</div>
    <div>{{ users | join : 1 : 3 }}</div>
    <hr />
    <div>
      Число: {{ squareNum }}<br/>
      Квадратний корінь числа: {{ squareNum | square }}
    </div>
  `,
})
export class AppComponent {
  myDate = new Date(1961, 3, 12);
  welcome: string = 'Hello World!';
  persentage: number = 0.14;
  pi: number = 3.1415;
  myNewDate = Date.now();
  money: number = 23.45;
  message: string = 'Hello  World!';
  x: number = 15.45;
  users = ['Tom', 'Alice', 'Sam', 'Kate', 'Bob'];

  squareNum: number = 256;
}
