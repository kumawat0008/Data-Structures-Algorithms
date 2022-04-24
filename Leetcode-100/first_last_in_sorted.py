class Solution(object):

    def first(self, arr, low, high, x, n):
        if (high >= low):
            mid = (low + high) // 2
            if ((mid == 0 or x > arr[mid - 1]) and arr[mid] == x):
                return mid
            elif (x > arr[mid]):
                return self.first(arr, (mid + 1), high, x, n)
            else:
                return self.first(arr, low, (mid - 1), x, n)

        return -1

    def last(self, arr, low, high, x, n):
        if (high >= low):
            mid = (low + high) // 2
            if ((mid == n - 1 or x < arr[mid + 1]) and arr[mid] == x):
                return mid
            elif (x < arr[mid]):
                return self.last(arr, low, (mid - 1), x, n)
            else:
                return self.last(arr, (mid + 1), high, x, n)

        return -1

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first = self.first(nums, 0, len(nums) - 1, target, len(nums))
        last = self.last(nums, 0, len(nums) - 1, target, len(nums))
        return [first, last]
