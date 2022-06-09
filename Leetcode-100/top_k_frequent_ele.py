class Maxheap(object):
    def __init__(self, arr):
        self.heap = arr
        self.heap_size = len(self.heap)

    def build_max_heap(self):
        for i in range(self.heap_size // 2, -1, -1):
            self.max_heapify(i)

    def max_heapify(self, i):
        left = (2 * i) + 1
        right = (2 * i) + 2
        largest = i
        if left < self.heap_size and self.heap[left][1] > self.heap[i][1]:
            largest = left
        if right < self.heap_size and self.heap[right][1] > self.heap[largest][1]:
            largest = right
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.max_heapify(largest)


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        m = {}
        for i in nums:
            try:
                m[i] += 1
            except:
                m[i] = 1
        arr = []
        for key, f in m.items():
            arr.append((key, f))
        h = Maxheap(arr)
        h.build_max_heap()
        res = []
        for i in range(k):
            res.append(h.heap[0][0])
            h.heap[0] = h.heap[-1]
            h.heap.pop(-1)
            h.heap_size = len(h.heap)
            h.max_heapify(0)
        return res

