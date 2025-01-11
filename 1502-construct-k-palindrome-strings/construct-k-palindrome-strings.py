class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s)<k:
            return False
        count= Counter(s)
        odd=0
        for val in count.values():
            if val%2==1:
                odd+=1

        if k==1 and odd<=1:
            return True
        elif k<odd:
            return False
            
        return True
        
        