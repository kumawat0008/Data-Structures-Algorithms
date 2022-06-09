class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        days_wait = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while len(stack) != 0 and temperatures[i] > temperatures[stack[-1]]:
                days_wait[stack[-1]] = i - stack[-1]
                stack.pop(-1)
            stack.append(i)

        return days_wait
