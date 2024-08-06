class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1=defaultdict(int)
        
        for i in s:
            dict1[i]+=1      
        for i in t:
            dict1[i]-=1
        
        for x in dict1:
            if(dict1[x]!=0):
                return False
        return True