class Solution:
    def makeFancyString(self, s: str) -> str:
        if not s:
            return s
        res=""
        temp=s[0]
        count=0
        
        for char in s:

            if char==temp:
                count+=1
                if count<3:
                    res+=char
            else:
                temp=char
                count=1
                res+=char

        return res