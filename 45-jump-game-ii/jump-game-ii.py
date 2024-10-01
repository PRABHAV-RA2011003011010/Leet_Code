class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps=0
        max_index=0
        left=0
        right=0
        n=len(nums)

        while right<n-1:

            
            for num in range(left,right+1):
                max_index=max(max_index,num+nums[num])
            
            left=right+1
            right=max_index
            jumps+=1

        return jumps
        

