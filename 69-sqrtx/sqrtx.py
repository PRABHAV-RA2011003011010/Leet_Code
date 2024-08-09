class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        elif x<4:
            return 1

        else:
            i=0
            for i in range(x):
                if i*i==x:
                    return i
                    break
                elif i*i>x:
                    return i-1
                    break
                