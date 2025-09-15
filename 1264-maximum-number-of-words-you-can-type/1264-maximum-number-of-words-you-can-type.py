class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:

        words=text.split(" ")
        res=0
        if not brokenLetters:
            return len(words)
        for word in words:
            count=0
            for letter in brokenLetters:
                if letter not in word:
                    count+=1
                if count==len(brokenLetters):
                    res+=1
                
        
        return res
        