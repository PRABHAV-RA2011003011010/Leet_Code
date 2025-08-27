class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        res=0
        rows=len(matrix)
        cols=len(matrix[0])
       

        for i in range(rows):
            if int(matrix[i][0])==1:
                res=1
                break
        if not res:
            for j in range(cols):
                if int(matrix[0][j])==1:
                    res=1
                    break
        
        for i in range(1,rows):
            for j in range(1,cols):
                if int(matrix[i][j])==1:
                    matrix[i][j]=1+min(int(matrix[i-1][j]),int(matrix[i][j-1]),int(matrix[i-1][j-1]))
                    res=max(res,matrix[i][j])
        return res*res        



        
        
        