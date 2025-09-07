class Solution:
    def maximumSwap(self, num: int) -> int:
        
        num_str= list(str(num))
        dp=[0]*len(num_str)
        dp[-1]=len(num_str)-1
        
        
        

        for i in range(len(num_str)-2,-1,-1):
            if int(num_str[i])>int(num_str[dp[i+1]]):
                dp[i]=i
            else:
                dp[i]=dp[i+1]
        for i in range(len(dp)):
            if dp[i]!=i and num_str[dp[i]]!=num_str[i]:
                num_str[i], num_str[dp[i]] = num_str[dp[i]], num_str[i]
                break
        res="".join(num_str)
        
        return int(res)
        