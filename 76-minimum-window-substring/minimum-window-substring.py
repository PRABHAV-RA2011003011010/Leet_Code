class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        sub=defaultdict(int)

        for char in t:
            sub[char]+=1
        
        remaining_chars=len(t)
        range_start=0
        range_end=len(s)
        start=0 
        for end_index,char in enumerate(s):

            if sub[char]>0:
                remaining_chars-=1
            sub[char]-=1
            
            if remaining_chars==0:

                while True:
                    if sub[s[start]]==0:
                        break
                    sub[s[start]]+=1
                    start+=1
                
                if (end_index-start)<(range_end-range_start):
                    range_start=start
                    range_end=end_index
                
                
                remaining_chars+=1
                sub[s[start]]+=1
                start+=1

        return "" if range_end > len(s)-1 else s[range_start:range_end+1]


            

                



            
