class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        tab=[[0]*n for _ in range(m)]
        res=0
        for row in range(m):
            for col in range(n):
                if matrix[row][col]==1:

                    if row==0 or col==0:
                        tab[row][col]=1
                    else:
                        tab[row][col]=min(tab[row-1][col],tab[row][col-1],tab[row-1][col-1])+1
                res+=tab[row][col]


        return res