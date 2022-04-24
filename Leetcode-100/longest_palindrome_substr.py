class Solution:
    def check_palin(self, s):
        return s == s[::-1]

    def longestPalindrome(self, s):
        for length in range(len(s), 0, -1):
            for i in range(len(s) - length + 1):
                if self.check_palin(s[i:(i + length)]):
                    return s[i:(i + length)]