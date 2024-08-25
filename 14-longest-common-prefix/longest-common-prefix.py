class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=strs[0]
        for x in strs[1:]:
            comon=""
            i=0
            m=min(len(x),len(prefix))
            while i<m and prefix[i]==x[i]:
                comon+=prefix[i]
                i+=1
            prefix=comon
        return prefix

        