class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum=0
        first=0
        min_len=0
        for i in range(len(nums)):
            sum+=nums[i]
            while(sum>=target):
                if(first==0):
                    min_len=i+1
                min_len=min(min_len,i-first+1)
                sum-=nums[first]
                first+=1
        return min_len

        