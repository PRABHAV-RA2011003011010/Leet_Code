class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        rows=len(obstacleGrid)
        cols=len(obstacleGrid[0])
        if obstacleGrid[0][0]==1:
            return 0
        obstacleGrid[0][0]=1
        obstaclefound=False
        for c in range(1,cols):
            if obstaclefound:
                obstacleGrid[0][c]=0

            elif obstacleGrid[0][c]==1:
                obstacleGrid[0][c]=0
                obstaclefound=True
            else:    
                obstacleGrid[0][c]=1
        obstaclefound=False        
        for r in range(1,rows):
            if obstaclefound:
                obstacleGrid[r][0]=0
            elif obstacleGrid[r][0]==1:
                obstacleGrid[r][0]=0
                obstaclefound=True
            else:    
                obstacleGrid[r][0]=1
        

        for r in range(1,rows):
            for c in range(1,cols):
                if obstacleGrid[r][c]==1:
                    obstacleGrid[r][c]=0
                else:
                    obstacleGrid[r][c]=obstacleGrid[r-1][c]+obstacleGrid[r][c-1]


        return obstacleGrid[-1][-1]
        
        