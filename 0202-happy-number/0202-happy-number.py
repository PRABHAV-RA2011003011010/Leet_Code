class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while n not in seen and n!=1:
            seen.add(n)
            sum=0
            while(n!=0):
                last_digit=n%10
                sum+=last_digit**2
                n=int(n/10)
            n=sum
        return n==1

        