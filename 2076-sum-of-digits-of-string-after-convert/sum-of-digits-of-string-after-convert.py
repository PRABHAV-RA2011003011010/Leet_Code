class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num=""
        for char in s:
            pos=ord(char)-ord('a')+1
            num=num+str(pos)
        
        while k>0:
            sum1=0
            for x in num:
                sum1+=int(x)
            num=str(sum1)
            k-=1




        
        return int(num)
            

        