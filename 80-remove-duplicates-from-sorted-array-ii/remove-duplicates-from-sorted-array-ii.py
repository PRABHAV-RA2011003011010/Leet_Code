class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index=1
        o=1

        for i in range(1,len(nums)):
            if(nums[i]==nums[i-1]):
                o+=1
            else:
                o=1
            
            if(o<=2):
                nums[index]=nums[i]
                index=index+1
        return index
        