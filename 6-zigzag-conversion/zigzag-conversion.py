class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows==1:
            return s
        res=[[] for row in range(numRows)] 

        cur=0
        forward=True
        for char in s:

            res[cur].append(char)
            
            if forward:
                if cur+1>=numRows:
                    forward=False
                    cur-=1
                else:
                    cur+=1
   
            else:
                if cur-1<0:
                    forward=True
                    cur+=1
                else:
                    cur-=1
        for i in range(numRows):
            res[i]=''.join(res[i])

        return ''.join(res)
        
           
            
            
            
            





        