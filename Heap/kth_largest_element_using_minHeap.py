class MinHeap(object):

    def __init__(self, arr):

        self.arr = arr
        self.heap_size = len(arr)

    def build_min_heap(self):

        for i in reversed(range(int(self.heap_size/2))):
            self.min_heapify(i)

    def min_heapify(self, i):

        left_child = 2*i+1
        right_child = 2*i+2
        smallest = i

        if left_child < self.heap_size and self.arr[left_child] < self.arr[i]:
            smallest = left_child
        if right_child < self.heap_size and self.arr[right_child] < self.arr[smallest]:
            smallest = right_child

        if i is not smallest:
            self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
            self.min_heapify(smallest)


if __name__ == '__main__':

    arr = [6, 2, 4, 5, 7, 1, 0, 5, 3, 8]
    k = 3
    heap = MinHeap(arr[0:k])
    heap.build_min_heap()
    # print(arr, heap.arr)
    for i in range(k, len(arr), 1):
        if arr[i] > heap.arr[0]:
            heap.arr[0] = arr[i]
            heap.min_heapify(0)

    print(heap.arr[0])
