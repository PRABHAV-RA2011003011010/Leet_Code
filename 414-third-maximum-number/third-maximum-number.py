class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s1=set(nums)
        s1=list(s1)
        s1.sort()
        
        if(len(s1)==0):
            return 0
        elif(len(s1)==1):
            return s1[0]
        elif(len(s1)==2):
            return s1[1]
        else:
            return s1[-3]

        