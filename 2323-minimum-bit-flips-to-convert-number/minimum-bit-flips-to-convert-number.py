class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:

        bina=bin(goal)[2:]
        bina1=bin(start)[2:]
        diff=0
        small=bina
        big=bina1
        modifications=0

        if len(bina)>len(bina1):
            big=bina
            small=bina1
            diff=len(bina)-len(bina1)
        elif len(bina)<len(bina1):
            big=bina1
            small=bina
            diff=len(bina1)-len(bina)

        while diff:
            small='0'+small
            diff-=1
            
        for i in range(len(big)):
            if big[i]!=small[i]:
                modifications+=1
        
        return modifications

        