class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        target=len(s)
        if(target!=0):
            sub=0
            for i in range(len(t)):
                if(t[i]==s[sub]):
                    sub+=1
                if(sub==target):
                    return True
                    break
            return False
        return True
        