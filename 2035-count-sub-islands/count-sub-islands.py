class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        r=len(grid1)
        c=len(grid1[0])
        visited=set()

        def dfs(r1,c1):
            if r1<0 or c1<0 or r1==r or c1==c or (r1,c1) in visited or grid2[r1][c1]==0:
                return True
            
            visited.add((r1,c1))
            res=True
            if grid1[r1][c1]==0:
                res=False
            
            res = dfs(r1 - 1, c1) and res
            res = dfs(r1 + 1, c1) and res
            res = dfs(r1, c1 - 1) and res
            res = dfs(r1, c1 + 1) and res
            
            return res
          

        count=0
        for row in range(r):
            for col in range(c):
                if grid2[row][col] and (row,col) not in visited and dfs(row,col):
                    count+=1
        return count
        




        