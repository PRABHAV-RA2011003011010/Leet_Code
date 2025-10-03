class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n=len(s)
        start_index=0
        if n==1:
            return s
        max_len=1
        dp= [[False]*n for _ in range(n)]
        
        for i in range(n):
            dp[i][i]=True

        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1]=True
                max_len=2
                start_index=i
        

        for length in range(3,n+1):
            for start in range(n-length+1):
                end=start+length-1

                if s[start]==s[end] and dp[start+1][end-1]:
                    dp[start][end]=True
                    max_len=length
                    start_index=start
                    
        return s[start_index:start_index+max_len]       