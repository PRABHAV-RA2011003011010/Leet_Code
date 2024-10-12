class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:

        events=defaultdict(int)
        cur=0
        groups=0

        for start,end in intervals:
            events[start]+=1
            events[end+1]-=1
        
        for key in sorted(events.keys()):
            cur+=events[key]
            groups=max(cur,groups)
        
        return groups
        









                
        