class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n=len(s)
        
        for i in range(n):

            newstr=s[i:]+s[:i]

            if goal==newstr:

                return True


        return False