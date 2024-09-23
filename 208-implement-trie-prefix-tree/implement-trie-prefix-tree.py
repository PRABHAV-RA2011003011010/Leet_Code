class TrieNode:
    def __init__(self):
        self.childrens={}
        self.endofword=False

class Trie:

    def __init__(self):

        self.root=TrieNode()
        

    def insert(self, word: str) -> None:
        cur=self.root
        for char in word:
            if char not in cur.childrens:
                cur.childrens[char]=TrieNode()
            cur=cur.childrens[char]
        cur.endofword=True
        

    def search(self, word: str) -> bool:
        cur=self.root
        for char in word:
            if char not in cur.childrens:
                return False
            cur=cur.childrens[char]
        return cur.endofword

        

    def startsWith(self, prefix: str) -> bool:
        cur=self.root
        for char in prefix:
            if char not in cur.childrens:
                return False
            cur=cur.childrens[char]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)