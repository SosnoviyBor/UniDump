import { Pipe, PipeTransform } from '@angular/core';
@Pipe({
  name: 'square',
})
export class SquarePipe implements PipeTransform {
  transform(squareNum: number): number {
    return Math.sqrt(squareNum);
  }
}
