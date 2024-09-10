class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        n=len(matrix)
        inplace=set()
        
        for row in range(n):
            for col in range(n):
                if (row,col) not in inplace:
                    r1=col
                    c1=(n-1)-row
                    

                    matrix[row][col],matrix[r1][c1]=matrix[r1][c1],matrix[row][col]
                    inplace.add((r1,c1))
        