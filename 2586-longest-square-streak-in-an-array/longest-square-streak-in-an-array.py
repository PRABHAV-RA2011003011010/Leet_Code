class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        sortednums=sorted(nums)
        newnum=set(sortednums)
        res=-1
        
        for num in sortednums:
            cur=num
            count=0
            while cur in newnum:

                newnum.remove(cur)
                count+=1
                cur=cur**2

            res=max(res,count)

        return res if res>1 else -1


        