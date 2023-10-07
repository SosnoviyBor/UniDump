pub fn bubble_sort<T: PartialOrd>(array: &mut [T]) {
    let size = array.len();
    if size <= 1 {
        return;
    }
    for i in 0..(size-1) {
        let mut swapped = false;        
        for j in 1..(size - i) {
            if array[j - 1]  > array[j] {
                array.swap(j - 1, j);
                swapped = true;
            }
        }
        if !swapped {
            break;
        }
    }
}
pub fn main() {
    let mut vec = vec![7, 49, 73, 58, 30, 72, 44, 78, 23, 9];
    bubble_sort(&mut vec);
}