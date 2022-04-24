class Solution:
    def lengthOfLongestSubstring(self, s):
        max_len = 0
        sub_str = ""
        for char in s:
            if char in sub_str:
                sub_str = sub_str[sub_str.index(char)+1:]
            sub_str+=char
            max_len = max(max_len, len(sub_str))
        return max_len