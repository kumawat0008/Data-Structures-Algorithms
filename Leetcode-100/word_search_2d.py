class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        def helper(rows, cols, board, word, level, n, i, j):
            if level == n:
                return True
            if i < 0 or j < 0 or i >= rows or j >= cols:
                return False
            if board[i][j] == word[level]:
                temp = board[i][j]
                board[i][j] = "*"
                res = helper(rows, cols, board, word, level + 1, n, i - 1, j) or helper(rows, cols, board, word,
                                                                                        level + 1, n, i + 1,
                                                                                        j) or helper(rows, cols, board,
                                                                                                     word, level + 1, n,
                                                                                                     i,
                                                                                                     j - 1) or helper(
                    rows, cols, board, word, level + 1, n, i, j + 1)
                board[i][j] = temp
                return res
            else:
                return False

        rows = len(board)
        cols = len(board[0])
        n = len(word)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if (helper(rows, cols, board, word, 0, n, i, j)):
                        return True

        return False
