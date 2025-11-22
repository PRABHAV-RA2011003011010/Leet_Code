class Solution:
    def isHappy(self, n: int) -> bool:

        while(n>=10):
            
            sum=0
            while(n!=0):
                last_digit=n%10
                sum+=last_digit**2
                n=int(n/10)
            n=sum
        return True if(n==1 or n==7) else False

        