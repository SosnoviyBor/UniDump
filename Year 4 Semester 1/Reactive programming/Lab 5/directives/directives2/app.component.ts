import { Component } from '@angular/core';
@Component({
  selector: 'my-app',
  template: ` <div>
      <p bold>Вивчаю директиви</p>
      <p>Створення атрибутивних директив</p>
    </div>
    <div>
      <p italic>Вивчаю директиви</p>
      <p>Створення атрибутивних директив</p>
    </div>
    <div>
      <p mousebold>Робота з декоратором @HostListener</p>
      <p>Реагування на покажчик миші</p>
    </div>
    <div>
      <p mouseitalic>Робота з декоратором @HostListener</p>
      <p>Реагування на покажчик миші за допомогою @HostBinding</p>
    </div>
    <div>
      <p hostmousebold>Робота з властивістю host</p>
      <p>Реагування на покажчик миші за допомогою властивості host</p>
    </div>`,
})
export class AppComponent {}
