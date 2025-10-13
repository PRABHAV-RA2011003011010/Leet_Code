class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        n=len(needle)
        
        if len(needle)==len(haystack):
            return 0 if needle==haystack else -1

        for i in range(len(haystack)-n+1):
            s=haystack[i:i+n]
            if s==needle:
                return i
        return -1