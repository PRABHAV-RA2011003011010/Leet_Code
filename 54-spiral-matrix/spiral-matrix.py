class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral=[]
        m=len(matrix)
        n=len(matrix[0])
        x=0
        y=0
        x1=1
        y1=0

        for _ in range(m*n):
            spiral.append(matrix[y][x])
            matrix[y][x]="."
            

            if not 0<=x+x1<n or not 0<=y+y1<m or matrix[y+y1][x+x1]==".":
                x1,y1=-y1,x1

            x+=x1
            y+=y1
        return spiral


        