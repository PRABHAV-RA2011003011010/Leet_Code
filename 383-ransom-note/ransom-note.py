class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict1=defaultdict(int)
        dict2=defaultdict(int)
        for x in ransomNote:
            dict1[x]+=1
        for y in magazine:
            dict2[y]+=1
        for x in dict1:
            if x not in dict2:
                return False
            if dict1[x]>dict2[x]:
                return False
        return True

        