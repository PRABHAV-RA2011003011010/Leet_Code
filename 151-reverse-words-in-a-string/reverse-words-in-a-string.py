class Solution:
    def reverseWords(self, s: str) -> str:
        temp=""
        temp_li=[]
        for i in s:
            
            if(i!=" "):
                temp=temp+i
            else:
                if(len(temp)!=0):

                    temp_li.append(temp)
                    temp=""
        if(len(temp)!=0):
            temp_li.append(temp)
        
        temp=temp_li[-1]
        for x in range(len(temp_li)-2,-1,-1):
            temp=temp+" "+temp_li[x]

        return temp       

        