class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        t=n*[1]

        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    t[i]=max(t[i],t[j]+1)
                    
        print(t)
        return max(t)

        