class PriorityQueue(object):

    def __init__(self, arr):

        self.arr = arr
        self.heap_size = len(self.arr)
        self.build_max_heap()

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

    def maximum(self):

        return self.arr[0]

    def extract_maximum(self):

        if self.heap_size < 1:
            return -1
        else:
            max_ = self.arr[0]
            self.arr[0] = self.arr[self.heap_size-1]
            del self.arr[self.heap_size-1]
            self.heap_size -= 1
            self.max_heapify(0)
            return max_

    def increase_value(self, i, val):

        self.arr[i] = val

        while i > 0 and self.arr[i] > self.arr[int((i-1)/2)]:
            self.arr[i], self.arr[int(
                (i-1)/2)] = self.arr[int((i-1)/2)], self.arr[i]
            i = int((i-1)/2)

    def insert_value(self, val):
        self.arr.append(-1)
        self.heap_size += 1
        self.increase_value(self.heap_size-1, val)


if __name__ == '__main__':

    arr = [1, 4, 3, 7, 8, 9, 10]

    pq = PriorityQueue(arr)
    pq.insert_value(2)
    pq.insert_value(22)
    print(arr)
