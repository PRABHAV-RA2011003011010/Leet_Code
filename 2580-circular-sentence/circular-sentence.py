class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        
        if sentence[0]!=sentence[-1]:
            return False
        words=sentence.split()
        n=len(words)

        if n==1:
            return True
        for i in range(n-1):
            if words[i][-1]!=words[i+1][0]:
                return False
        return True
