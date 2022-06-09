class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        def is_palin(s, start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        def partition_helper(s, index, n, part, res, hm):

            if s[index:n] in hm and s[index:n] == 2:
                print('++++here')
                return
            if index >= n:
                res.append(list(part))

            for i in range(index, n):
                if is_palin(s, index, i):
                    part.append(s[index:i + 1])
                    partition_helper(s, i + 1, n, part, res, hm)
                    part.pop(-1)
                    try:
                        hm[s[i + 1:n]] += 1
                    except:
                        hm[s[i + 1:n]] = 1

        part = []
        res = []
        n = len(s)
        hm = {}
        partition_helper(s, 0, n, part, res, hm)
        return res
