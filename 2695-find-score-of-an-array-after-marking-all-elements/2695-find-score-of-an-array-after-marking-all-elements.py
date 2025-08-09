class Solution:
   from typing import List

class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        indexed_nums = sorted([val, idx] for idx, val in enumerate(nums))
        print(indexed_nums)
        
        visited = set()
        res = 0

        for val, idx in indexed_nums:
            if idx in visited:
                continue
            # Take the value
            res += val
            # Mark current and neighbors as visited
            visited.add(idx)
            if idx - 1 >= 0:
                visited.add(idx - 1)
            if idx + 1 < n:
                visited.add(idx + 1)

        return res


        
        