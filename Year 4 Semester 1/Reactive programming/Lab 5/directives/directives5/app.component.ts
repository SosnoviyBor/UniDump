import { Component } from '@angular/core';

@Component({
  selector: 'my-app',
  template: `<div *sum="let result; from: 20; to: 30">
    Сума = {{ result }}
  </div>`,
})
export class AppComponent {}
