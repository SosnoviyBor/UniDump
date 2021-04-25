/**
 *  Java Program to Implement Binary Heap
 */

import java.util.Arrays;
import java.util.NoSuchElementException;

public class BinaryHeap {
    private static final int d = 2;
    private int heapSize;
    private int[] heap;

    public BinaryHeap(int capacity){
        heapSize = 0;
        heap = new int[capacity];
        Arrays.fill(heap, -1);
    }

    /**==============================
     *          PUBLIC METHODS
     * ==============================**/

    public boolean isEmpty( )
    {
        return heapSize == 0;
    }

    public boolean isFull( )
    {
        return heapSize == heap.length;
    }

    public void makeEmpty( )
    {
        heapSize = 0;
    }

    public void insert(int x) {
        if (isFull( ) ) {
            throw new NoSuchElementException("Overflow Exception");
        }
        heap[heapSize++] = x;
        heapifyUp(heapSize - 1);
    }

    public int findPosition(int x) {
        if (isEmpty() ) {
            throw new NoSuchElementException("Underflow Exception");
        }
        for (int i = 0; i <= heapSize; i++) {
            if (x == heap[i]) {
                return i;
            }
        }
        throw new NoSuchElementException("There is no such value");
    }

    public int delete(int ind) {
        if (isEmpty() ) {
            throw new NoSuchElementException("Underflow Exception");
        }
        int keyItem = heap[ind];
        heap[ind] = heap[heapSize - 1];
        heapSize--;
        heapifyDown(ind);
        return keyItem;
    }

    public void printHeap() {
        System.out.print("\nHeap = ");
        for (int i = 0; i < heapSize; i++) {
            System.out.print(heap[i] + " ");
        }
        System.out.println();
    }

    public void printSorted() {
        int[] arr = Arrays.copyOf(heap, heapSize);
        int n = arr.length;

        /**Selection sort**/
        for (int i = 0; i < n-1; i++) {
            int min_idx = i;
            for (int j = i+1; j < n; j++)
                if (arr[j] < arr[min_idx])
                    min_idx = j;

            int temp = arr[min_idx];
            arr[min_idx] = arr[i];
            arr[i] = temp;
        }

        System.out.print("\nSorted view of heap = ");
        for (int j : arr) {
            System.out.print(j + " ");
        }
        System.out.println();
    }

    public void randomFill (String inp) {
        String[] strParts = inp.split(" ");
        int min = Integer.parseInt(strParts[0]);
        int max = Integer.parseInt(strParts[1]);

        if (min < 0 || max < 0) {
            throw new ArrayStoreException("Heap can't store negative values");
        }
        while (heapSize != heap.length) {
            heap[heapSize++] = min + (int)(Math.random() * ((max - min) + 1));
            heapifyUp(heapSize - 1);
        }
    }

    public void sortedFill (int i) {
        if (i < 0) {
            throw new ArrayStoreException("Heap can't store negative values");
        }
        while (heapSize != heap.length) {
            heap[heapSize++] = i++;
            heapifyUp(heapSize - 1);
        }
    }

    /**==============================
     *          PRIVATE METHODS
     * ==============================**/

    private void heapifyUp(int childInd) {
        int tmp = heap[childInd];
        while (childInd > 0 && tmp < heap[parent(childInd)]) {
            heap[childInd] = heap[ parent(childInd) ];
            childInd = parent(childInd);
        }
        heap[childInd] = tmp;
    }

    private void heapifyDown(int ind) {
        int child;
        int tmp = heap[ ind ];
        while (kthChild(ind, 1) < heapSize) {
            child = minChild(ind);
            if (heap[child] < tmp) {
                heap[ind] = heap[child];
            }
            else {
                break;
            }
            ind = child;
        }
        heap[ind] = tmp;
    }

    private int minChild(int ind) {
        int bestChild = kthChild(ind, 1);
        int k = 2;
        int pos = kthChild(ind, k);
        while ((k <= d) && (pos < heapSize)) {
            if (heap[pos] < heap[bestChild]) {
                bestChild = pos;
            }
            pos = kthChild(ind, k++);
        }
        return bestChild;
    }

    private int parent(int i) {
        return (i - 1)/d;
    }

    private int kthChild(int i, int k) {
        return d * i + k;
    }
}