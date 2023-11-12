import { Pipe, PipeTransform } from '@angular/core';
@Pipe({
    name: 'square'
})
export class SquarePipe implements PipeTransform {
    transform(squareNum: any): any {
        let result = Math.sqrt(squareNum);
        return result;
    }
}