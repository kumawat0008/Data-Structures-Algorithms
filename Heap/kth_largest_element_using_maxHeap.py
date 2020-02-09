class MaxHeap(object):

    def __init__(self, arr):

        self.arr = arr
        self.heap_size = len(arr)

    def build_max_heap(self):

        for i in reversed(range(int(self.heap_size/2))):
            self.max_heapify(i)

    def max_heapify(self, i):

        left_child = 2*i+1
        right_child = 2*i+2
        largest = i

        if left_child < self.heap_size and self.arr[left_child] > self.arr[i]:
            largest = left_child
        if right_child < self.heap_size and self.arr[right_child] > self.arr[largest]:
            largest = right_child

        if i is not largest:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.max_heapify(largest)

    def extract_max(self):

        if self.heap_size < 1:
            return "underflow"

        max_ = self.arr[0]
        self.arr[0] = self.arr[self.heap_size-1]
        del self.arr[self.heap_size-1]
        self.heap_size -= 1
        self.max_heapify(0)
        return max_


if __name__ == '__main__':

    arr = [2, 6, 4, 5, 7, 1, 0, 5, 3, 8]

    heap = MaxHeap(arr)
    heap.build_max_heap()

    k = 3

    for i in range(k):

        print(heap.extract_max())
