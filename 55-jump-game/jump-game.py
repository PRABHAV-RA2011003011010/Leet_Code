class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        index=len(nums)-1
       

        for i in range(index-1,-1,-1):
            if(index<=i+nums[i]):
                index=i
            
        
        return True if(index==0) else False
