class Solution:
    def maxScore(self, s: str) -> int:

        zeros=0
        ones=0
        cur=0
        score=0

        for i in range(len(s)-1):

            if s[i]=='0':
                zeros+=1
            else:
                ones+=1
            if zeros>=ones:
                cur=i
                zeros=0
                ones=0
        
        for i in range(cur+1):
            if s[i]=='0':
                score+=1
        for i in range(cur+1,len(s)):
            if s[i]=='1':
                score+=1
        

        return score
        