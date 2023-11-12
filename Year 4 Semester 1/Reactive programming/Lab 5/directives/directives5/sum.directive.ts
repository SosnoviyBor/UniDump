import { Directive, Input, TemplateRef, ViewContainerRef } from '@angular/core';

@Directive({
  selector: '[sum]',
})
export class SumDirective {
  constructor(
    private templateRef: TemplateRef<any>,
    private viewContainer: ViewContainerRef
  ) {}

  @Input() sumFrom = 0;
  @Input() sumTo = 0;

  ngOnInit() {
    let result = 0;
    for (let i = this.sumFrom; i <= this.sumTo; i++) {
      result += i;
    }
    this.viewContainer.createEmbeddedView(this.templateRef, {
      $implicit: result,
    });
  }
}
