class Solution(object):
    def check_valid(self, s):
        stack = []
        for char in s:
            if char == "(":
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    stack.pop()
        if stack:
            return False
        return True

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = dict()
        for length in range(len(s), 0, -1):
            for i in range(len(s) - length + 1):
                my_str = s[i:i + length]
                if my_str not in dp:
                    flag = self.check_valid(my_str)
                    dp[my_str] = True
                    if flag:
                        return length
        return 0

