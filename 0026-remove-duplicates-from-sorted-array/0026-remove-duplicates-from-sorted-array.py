class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        cur=nums[0]
        s=1
        for i in range(1,len(nums)):
            if cur!=nums[i]:
                nums[s]=nums[i]
                cur=nums[i]
                s+=1
                
        return s

            
        