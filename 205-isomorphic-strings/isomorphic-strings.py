class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        new=""
        dict={}
        for i in range(len(s)):

            if(s[i] not in dict and t[i] in dict.values()):
                return False

            if(s[i] not in dict):
                dict[s[i]]=t[i]
            else:
                if dict[s[i]]!=t[i]:
                    return False
        print(dict)
        for i in range(len(t)):
            new+=dict[s[i]]
        if(new==t):
            return True
        else:
            return False
        