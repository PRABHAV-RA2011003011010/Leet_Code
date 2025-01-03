class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:

        leftsum=0
        rightsum=sum(nums)
        res=0

        for num in nums:
            leftsum+=num
            rightsum-=num
            if leftsum>=rightsum:
                res+=1
        if leftsum>=rightsum:
            res-=1
        return res


        