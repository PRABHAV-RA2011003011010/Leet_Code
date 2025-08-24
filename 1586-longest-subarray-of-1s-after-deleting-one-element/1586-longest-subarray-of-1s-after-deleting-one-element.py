class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start=0
        zero=-1
        curlen=0
        res=0
        for i in range(len(nums)):
            if nums[i]==0 and zero!=-1:
                res=max(res,curlen-1)
                curlen+=1
                curlen=curlen-(zero-start+1)
                start=zero+1
                zero=i
            elif nums[i]==0:
                zero=i
                curlen+=1
            else:
                curlen+=1

        return max(res,curlen-1)  

        