class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res=[]
        intervals.append(newInterval)
        intervals.sort()
        prev=intervals[0]

        for interval in intervals[1:]:

            if interval[0]<=prev[1]:
                prev[1]=max(interval[1],prev[1])
            else:
                res.append(prev)
                prev=interval
        res.append(prev)
        return res
        
        