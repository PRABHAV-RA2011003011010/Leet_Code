class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
       
        while k:
            min1=min(nums)
            for x in range(len(nums)):
                if nums[x]==min1:
                    nums[x]=nums[x]*multiplier
                    break
            k-=1
        return nums
        