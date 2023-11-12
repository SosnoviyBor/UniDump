import { Directive, Input, TemplateRef, ViewContainerRef } from '@angular/core';

@Directive({
  selector: '[appOtherIf]',
})
export class OtherIfDirective {
  constructor(
    private templateRef: TemplateRef<any>,
    private viewContainer: ViewContainerRef
  ) {}

  @Input() set appOtherIf(condition: boolean) {
    if (!condition) { this.viewContainer.createEmbeddedView(this.templateRef); }
    else { this.viewContainer.clear(); }
  }
}
