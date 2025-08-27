class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        res=0
        rows=len(matrix)
        cols=len(matrix[0])
        dp=[[0]*cols for _ in range(rows)]

        for i in range(rows):
            if int(matrix[i][0])==1:
                dp[i][0]=int(matrix[i][0])
                if not res:
                    res=1
        for j in range(cols):
            if int(matrix[0][j])==1:
                dp[0][j]=int(matrix[0][j])
                if not res:
                    res=1
        
        for i in range(1,rows):
            for j in range(1,cols):
                if int(matrix[i][j])==1:
                    dp[i][j]=1+min(int(dp[i-1][j]),int(dp[i][j-1]),int(dp[i-1][j-1]))
                    res=max(res,dp[i][j])
        return res*res        



        
        
        