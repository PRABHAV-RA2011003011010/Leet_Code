class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        seqlen=1
        length=1
        nums.sort()
        for i in range(len(nums)-1):
            diff=nums[i+1]-nums[i]

            if diff==1:
                seqlen+=1
            elif diff>1:
                seqlen=1
            length=max(length,seqlen)
        return length
        