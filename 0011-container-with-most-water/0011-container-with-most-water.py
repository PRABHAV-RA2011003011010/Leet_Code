class Solution:
    def maxArea(self, height: List[int]) -> int:

        left=0
        right=len(height)-1
        res=0

        while left<right:

            h=min(height[left],height[right])
            w=right-left
            area=h*w
            res=max(res,area)

            if height[left] > height[right]:
                right -=1
            else:
                left +=1  
        return res      