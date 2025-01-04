class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        def dfs(grid, i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                return
            grid[i][j] = '0'  # Mark the land as visited by sinking the island
            dfs(grid, i + 1, j)  # Visit down
            dfs(grid, i - 1, j)  # Visit up
            dfs(grid, i, j + 1)  # Visit right
            dfs(grid, i, j - 1)  # Visit left
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    dfs(grid, i, j)
        
        return count

