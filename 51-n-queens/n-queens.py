class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col=[]
        diagonal=[]
        antidiagonal=[]
        res=[["."]*n for x in range(n)]
        result=[]
        def backtrack(currow):
            if currow==n:
                result.append(["".join(row) for row in res])
                return 
            

            for curcol in range(n):
                dia=curcol-currow
                anti=curcol+currow
                
                if curcol not in col and dia not in diagonal and anti not in antidiagonal:
                    col.append(curcol)
                    diagonal.append(dia)
                    antidiagonal.append(anti)
                    res[currow][curcol]='Q'
                    
                    backtrack(currow+1)

                    col.pop()
                    diagonal.pop()
                    antidiagonal.pop()
                    res[currow][curcol]='.'
        
        backtrack(0)
        return result
                    




        