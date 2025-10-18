class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        
        start=0
        res=1
        count=1

        for i in range(1,len(s)):

            if s[i] in s[start:i]:
                for j in range(start,i):
                    if s[j]==s[i]:
                        start=j+1
                        count=i-start+1
                        break
            else:
                count+=1
                res=max(count,res)   
      
        return res


        