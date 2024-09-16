class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        if len(timePoints)>60*24:
            return 0

        min_distance=60*24
        minute=[]

        for time in timePoints:

            hours,minutes=map(int,time.split(':'))
            minute.append(hours*60+minutes)
            
        minute.sort()

        for i in range(len(minute)-1):
            min_distance=min(min_distance,minute[i+1]-minute[i])
        
        min_distance=min(min_distance,24*60-(minute[-1]-minute[0]))

        return min_distance
        
               
            


        


        