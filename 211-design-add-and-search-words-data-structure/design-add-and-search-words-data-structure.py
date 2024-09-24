class TriesNode:
    def __init__(self):
        self.childrens={}
        self.endofword=False

class WordDictionary:

    def __init__(self):

        self.root=TriesNode()
        

    def addWord(self, word: str) -> None:
        cur=self.root
        for char in word:
            if char not in cur.childrens:
                cur.childrens[char]=TriesNode()
            cur=cur.childrens[char]
        cur.endofword=True

    def search(self, word: str) -> bool:
        cur=self.root

        def dfs(i,node):

            if i==len(word):
                if node.endofword==True:
                    return True
                return False
            
            if word[i] in node.childrens:
                return dfs(i+1,node.childrens[word[i]])
                    
            else:
                if word[i]=='.':
                    for letter in node.childrens:
                       if dfs(i+1,node.childrens[letter]):
                            return True

                
            return False
            
        
        return dfs(0,cur)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)