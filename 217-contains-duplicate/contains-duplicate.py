class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        len1=len(nums)
        nums2=list(set(nums))
        len2=len(nums2)
        print(len2)
        return False if len1==len2 else True

        