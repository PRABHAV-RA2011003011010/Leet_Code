class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        res=0
        points.sort()
        prev=points[0]

        for point in points[1:]:

            if point[0]<=prev[1]:
                prev[1]=min(point[1],prev[1])
            else:
                res+=1
                prev=point
        res+=1
        return res
        
        