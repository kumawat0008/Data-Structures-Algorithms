class Solution(object):

    def generateParenthesisUtil(self, n, Open, close, s, res):
        print('+inside fun', Open, close, s)
        if (Open == n and close == n):
            print('+str', s)
            res.append(s)
            return
        if Open < n:
            print('++open', s, Open)
            self.generateParenthesisUtil(n, Open + 1, close, s + "(", res)
        if close < Open:
            print('++close', s, close)
            self.generateParenthesisUtil(n, Open, close + 1, s + ")", res)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        s = ""
        Open = 0
        close = 0

        self.generateParenthesisUtil(n, Open, close, s, res)
        return res

s = Solution()
s.generateParenthesis(3)