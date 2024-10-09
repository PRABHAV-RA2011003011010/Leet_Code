class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        brackets=0
        cur=0

        for char in s:

            if char=='(':
                cur+=1
            else:
                cur-=1
            
            if cur==-1:
                brackets+=1
                cur+=1
        
        brackets+=cur    

        return brackets

        