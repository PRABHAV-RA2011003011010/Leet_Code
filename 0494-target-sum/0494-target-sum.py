class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total=sum(nums)
        if (total+target)%2!=0 or total<abs(target):
            return 0
        
        positivearraysum= (total+target)//2
        dp=[0]*(positivearraysum+1)
        dp[0]=1

        for num in nums:
            for j in range(positivearraysum,num-1,-1):
                dp[j]+=dp[j-num]

        return dp[-1]
        