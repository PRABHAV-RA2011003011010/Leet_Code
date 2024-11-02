class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        directions=((0,1),(-1,1),(1,1))
        memo={}

        def dfs(row,col):

            if (row,col) in memo:
                return memo[(row,col)]
            curmoves=0
            for nr,nc in directions:
                newrow=row+nr
                newcol=col+nc

                if 0<=newrow<m and newcol<n and grid[row][col]<grid[newrow][newcol]:
                    curmoves=max(curmoves,dfs(newrow,newcol)+1)

            memo[(row,col)]=curmoves
            return curmoves
            

        moves=0
        for i in range(m):
            moves=max(moves,dfs(i,0))
        return moves





        