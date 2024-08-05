class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp=[0]*(len(nums))
        prefix=1
        suffix=1
        
        for i in range(len(temp)):
            temp[i]=prefix
            prefix=prefix*nums[i]
        for j in range(len(temp)-1,-1,-1):
            temp[j]=suffix*temp[j]
            suffix=suffix*nums[j]
        
        return temp
            
