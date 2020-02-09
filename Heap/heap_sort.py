class MaxHeap(object):

    def __init__(self, arr):

        self.arr = arr
        self.heap_size = len(self.arr)

    def build_max_heap(self):
        for i in reversed(range(int(self.heap_size/2))):
            self.max_heapify(i)

    def max_heapify(self, i):

        left_child = (2*i)+1
        right_child = (2*i)+2
        largest = i

        if left_child < self.heap_size and self.arr[left_child] > self.arr[i]:
            largest = left_child
        if right_child < self.heap_size and self.arr[right_child] > self.arr[largest]:
            largest = right_child

        if largest is not i:
            self.arr[largest], self.arr[i] = self.arr[i], self.arr[largest]
            self.max_heapify(largest)


class HeapSort(object):

    def heap_sort(self, arr):

        heap = MaxHeap(arr)
        heap.build_max_heap()

        for i in reversed(range(heap.heap_size)):
            heap.arr[i], heap.arr[0] = heap.arr[0], heap.arr[i]
            heap.heap_size -= 1
            heap.max_heapify(0)


if __name__ == '__main__':

    arr = [1, 4, 3, 7, 8, 9, 10]

    HeapSort().heap_sort(arr)
    print(arr)
