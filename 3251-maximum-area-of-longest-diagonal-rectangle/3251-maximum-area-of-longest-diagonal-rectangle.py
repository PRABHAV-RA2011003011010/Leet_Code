class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        l=3
        b=3
        max_diagonal=0
        area=0
        
        for rectangle in dimensions:
            cur_diagonal=(rectangle[0]**2+rectangle[1]**2)**(1/2)
            if cur_diagonal>max_diagonal:
                max_diagonal=cur_diagonal
                area=rectangle[0]*rectangle[1]
            elif cur_diagonal==max_diagonal:
                area=max(area,rectangle[0]*rectangle[1])
        

        return area
        