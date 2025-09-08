class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        num1=1
        num2=n-1
        while '0' in str(num2) or '0' in str(num1):
            num1+=1
            num2-=1
            if '0' not in str(num2)+str(num1):
                return [num1,num2]
        return [num1,num2]
        