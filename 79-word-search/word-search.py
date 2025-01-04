class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False

        def dfs(row, col, index):
            if index == len(word):
                return True

            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[index]:
                return False

            # Mark the cell as visited by temporarily changing its value
            temp = board[row][col]
            board[row][col] = '#'

            # Traverse the neighbors
            found = (dfs(row + 1, col, index + 1) or  # down
                     dfs(row - 1, col, index + 1) or  # up
                     dfs(row, col + 1, index + 1) or  # right
                     dfs(row, col - 1, index + 1))    # left

            # Restore the cell's original value
            board[row][col] = temp

            return found

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if dfs(row, col, 0):
                        return True

        return False