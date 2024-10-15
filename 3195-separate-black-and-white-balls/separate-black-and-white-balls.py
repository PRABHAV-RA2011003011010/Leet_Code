class Solution:
    def minimumSteps(self, s: str) -> int:

        zeroes=0
        p1=len(s)-1
        res=0

        while p1>=0 and s[p1]!='0':
            p1-=1

        for p2 in range(p1,-1,-1):

            if s[p2]=='0':
                zeroes+=1
            else:
                res+=zeroes

        return res
       
                

        