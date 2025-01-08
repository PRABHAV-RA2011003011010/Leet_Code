class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        vowels={'a','e','i','o','u'}
        n=len(words)
        prefix=[0]*(n+1)
        ans=[]
        
        for i in range(len(words)):
            prefix[i+1]=prefix[i]
            if words[i][0] in vowels and words[i][-1] in vowels:
                    prefix[i+1]+=1

        

        for start,end in queries:
            ans.append(prefix[end+1]-prefix[start])
            
        return ans
                    



        