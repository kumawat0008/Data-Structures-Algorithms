class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        last_index = {c: i for i, c in enumerate(s)}
        size = end = 0
        out = []

        for i, c in enumerate(s):
            size += 1
            end = max(end, last_index[c])
            if i == end:
                out.append(size)
                size = 0

        return out

