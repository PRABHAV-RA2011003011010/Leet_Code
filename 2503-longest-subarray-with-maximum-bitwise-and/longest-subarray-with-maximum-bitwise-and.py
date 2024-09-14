class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        max_number=max(nums)
        max_length=0
        i=0
        while i<len(nums):
            if nums[i]==max_number:
                length=0
                while i<len(nums) and nums[i]==max_number:
                    length+=1
                    i+=1
                max_length=max(max_length,length)
            else:
                i+=1
        return max_length
                    