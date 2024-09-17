class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        res=[]
        dict1=defaultdict(int)

        words1=s1.split(" ")+s2.split(" ")
        

        for word in words1:
            dict1[word]+=1
        for word,count in dict1.items():
            if count==1:
                res.append(word)
        return res
        


        