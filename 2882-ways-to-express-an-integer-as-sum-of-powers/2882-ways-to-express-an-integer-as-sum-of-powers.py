class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        dp=[0]*(n+1)
        dp[0]=1
        MOD = 10**9 + 7
        limit=int(n**(1/x))+1
        
        for i in range(1,limit+1):
            power=i**x
            for j in range(n, power - 1, -1):
                dp[j] = (dp[j] + dp[j - power]) % MOD

        return dp[-1]