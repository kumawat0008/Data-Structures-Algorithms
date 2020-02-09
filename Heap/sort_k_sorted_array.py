class MinHeap(object):

    def __init__(self, arr):

        self.arr = arr
        self.heap_size = len(arr)

    def build_min_heap(self):

        for i in reversed(range(int(self.heap_size/2))):
            self.min_heapify(i)

    def min_heapify(self, i):

        left = 2*i+1
        right = 2*i+2
        smallest = i

        if left < self.heap_size and self.arr[left] < self.arr[i]:
            smallest = left

        if right < self.heap_size and self.arr[right] < self.arr[smallest]:
            smallest = right

        if i is not smallest:
            self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
            self.min_heapify(smallest)

    def extract_min(self):

        if self.heap_size < 1:
            return -1
        else:
            min_ = self.arr[0]
            self.arr[0] = self.arr[self.heap_size-1]
            del self.arr[-1]
            self.heap_size -= 1
            self.min_heapify(0)
            return min_


if __name__ == '__main__':

    arr = [2, 6, 3, 12, 56, 8]
    k = 2
    heap = MinHeap(arr[0:k+1])
    heap.build_min_heap()
    print(arr, heap.arr)
    new_arr = []
    for i in range(k+1, len(arr), 1):
        new_arr.append(heap.arr[0])
        heap.arr[0] = arr[i]
        heap.min_heapify(0)

    while heap.heap_size is not 0:
        new_arr.append(heap.arr[0])
        heap.extract_min()

    print(new_arr)
