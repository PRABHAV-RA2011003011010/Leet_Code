class Trienode:
    def __init__(self):
        self.childrens={}
        self.endofword=False
class Trie:
    def __init__(self):
        self.root=Trienode()
    
    def add(self,number):
        cur=self.root
        for num in number:
            if num not in cur.childrens:
                cur.childrens[num]=Trienode()
            cur=cur.childrens[num]
        cur.endofword=True
    def check_prefix(self,number):
        cur=self.root
        count=0
        for num in number:
            if num not in cur.childrens:
                return count
            count+=1
            cur=cur.childrens[num]
        return count



class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:

        longest=0
        trie1=Trie()
        trie2=Trie()

        for num in arr1:
            trie1.add(str(num))
        for num in arr2:
            trie2.add(str(num))
        
        for num in arr1:
            longest=max(longest,trie2.check_prefix(str(num)))
        for num in arr2:
            longest=max(longest,trie1.check_prefix(str(num)))
        
        return longest
        