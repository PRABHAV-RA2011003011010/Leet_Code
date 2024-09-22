class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        rows=len(grid)
        cols=len(grid[0])
        if rows==1:
            return sum(grid[0])
        if cols==1:
            sum1=0
            for x in grid:
                sum1+=sum(x)
            return sum1

        for col in range(1,cols):
            grid[0][col]+=grid[0][col-1]
        
        for row in range(1,rows):
            grid[row][0]+=grid[row-1][0]
        
        for row in range(1,rows):
            for col in range(1,cols):
                min_value=min(grid[row][col-1],grid[row-1][col])
                grid[row][col]+=min_value

        return grid[-1][-1]