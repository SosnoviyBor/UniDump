import { Directive, HostListener, Input, HostBinding } from '@angular/core';

@Directive({
  selector: '[changesize]',
})
export class ChangesizeDirective {
  @Input() selectedSize = 18;
  @Input() defaultSize = 16;

  private fontSize: string;

  constructor() {
    this.fontSize = this.defaultSize + "px";
  }

  @HostBinding('style.fontSize') get getFontSize() {
    return this.fontSize;
  }

  @HostListener('mouseenter') onMouseEnter() {
    this.fontSize = this.selectedSize + "px";
  }

  @HostListener('mouseleave') onMouseLeave() {
    this.fontSize = this.defaultSize + "px";
  }
}
