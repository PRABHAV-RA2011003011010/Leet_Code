class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        imin=rows
        imax=-1
        jmin=cols
        jmax=-1
        
        area=0

        for i in range(rows):
            for j in range(cols):

                if grid[i][j]==1:
                    imin=min(imin,i)
                    imax=max(imax,i)
                    jmin=min(jmin,j)
                    jmax=max(jmax,j)
        area=(imax-imin+1)*(jmax-jmin+1)
        return area