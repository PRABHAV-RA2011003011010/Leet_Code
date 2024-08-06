class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        rang=[]
        if not nums:
            return []
        first=nums[0]
        for i in range(1,len(nums)):
            if(nums[i]!=nums[i-1]+1):
                if(first==nums[i-1]):
                    rang.append(f'{first}')
                else:
                    rang.append(f'{first}->{nums[i-1]}')
                first=nums[i]
        if(first==nums[-1]):
            rang.append(f'{first}')
        else:
            rang.append(f'{first}->{nums[-1]}')


        return rang