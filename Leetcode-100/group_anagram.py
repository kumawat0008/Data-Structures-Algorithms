class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        temp = dict()
        for word in strs:
            word = str(word)
            try:
                temp[''.join(sorted(word))].append(word)
            except:
                temp[''.join(sorted(word))] = [word]

        return list(temp.values())

