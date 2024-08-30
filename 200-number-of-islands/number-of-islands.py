class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row=len(grid)
        col=len(grid[0])
        visited=set()
        count=0

        def dfs(r,c):

            if r<0 or c<0 or r==row or c==col or grid[r][c]=="0" or (r,c) in visited:
                return
            visited.add((r,c))
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        
        for r in range(row):
            for c in range(col):
                if (r,c) not in visited and grid[r][c]=="1":
                    dfs(r,c)
                    count+=1
        return count

        