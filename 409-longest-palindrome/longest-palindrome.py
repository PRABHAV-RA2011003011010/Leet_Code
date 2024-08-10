class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict=defaultdict(int)
        max=0
        for x in s:
            dict[x]+=1 
        if(len(dict)==1):
            return len(s)
        for key,value in dict.items():
            if(value%2==0):
                max+=value
            elif(value>2):
                n=value-1
                max=max+n
                value=value-n
        for key,value in dict.items():
            if(value%2==1):
                max+=1
                break
        return max