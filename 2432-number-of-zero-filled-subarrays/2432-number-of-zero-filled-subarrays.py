class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res=0
        curlen=0
        for i in range(len(nums)):
            if nums[i]==0:
                curlen+=1
            else:
                res+=(curlen*(curlen+1))//2
                curlen=0
        if curlen!=0:
            res+=(curlen*(curlen+1))//2

        return res
        