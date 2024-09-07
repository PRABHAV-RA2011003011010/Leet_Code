class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)
        col=len(matrix[0])
        r=0
        while r<row:
            if matrix[r][col-1]>=target:
                break
            r+=1
        if r>row-1:
            return False
        
        left=0
        right=col-1
        while left<=right:
            mid=(left+right)//2

            if matrix[r][mid]==target:
                return True
            if matrix[r][mid]<target:
                left=mid+1
            else:
                right=mid-1
        return False
        