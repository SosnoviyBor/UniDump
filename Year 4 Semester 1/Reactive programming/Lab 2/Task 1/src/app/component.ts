import { Component } from '@angular/core';

@Component({
    selector: 'my-app-1',
    // template: `
    //     <label>Введіть ім’я:</label>
    //     <input [(ngModel)]="name" placeholder="name">
    //     <h1>Ласкаво просимо {{name}}!</h1>
    //     <h2>Hello Angular</h2>
    //     <p>Angular представляє модульну архітектуру додатку</p>
    //     <child-comp>
    //         <h2>Ласкаво просимо {{name}}!</h2>
    //     </child-comp>
    //     <p>Hello {{name}}</p>
    // `,
    templateUrl: './component.html',
    // styles: [`
    //     h2,h3{color:navy;}
    //     p{font-size:13px; font-family:Verdana;}
    //     h1, h2{color:navy;}
    //     p{font-size:13px;}
    //     :host {
    //         font-family: Verdana;
    //         color: #555;
    //     }`],
    styleUrls: [
        './component.css'
    ]
})

export class AppComponent {
    name: "Петро";
    name2:string="Tom";
    age:number = 24;
}
