class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        temp=s.split()
        new1=[]
        new2=[]
        dict1={}
        dict2={}
        count=1
        for i in range(len(pattern)):
            if pattern[i] not in dict1:
                dict1[pattern[i]]=count
                count+=1
            new1.append(dict1[pattern[i]])
        count=1
        for i in range(len(temp)):
            if temp[i] not in dict2:
                dict2[temp[i]]=count
                count+=1
            new2.append(dict2[temp[i]])
            
        
        if(new1==new2):
            return True
        else:
            return False
        

        


        