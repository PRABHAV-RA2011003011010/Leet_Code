class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        frequencies=defaultdict(int)
        n=len(nums)

        for num in nums:
            frequencies[num]+=1
            if frequencies[num]>(n//2):
                return num
        