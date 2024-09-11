class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        
        temp=n*[0]
        temp[0]=nums[0]
        temp[1]=max(nums[1],nums[0])
        
        for i in range(2,len(nums)):

            temp[i]=max(temp[i-1],nums[i]+temp[i-2])
        return temp[-1]



        