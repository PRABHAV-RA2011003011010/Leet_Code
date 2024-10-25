class Trienode:

    def __init__(self):
        self.children={}
        self.endoffolder=False

class Trie:

    def __init__(self):

        self.root=Trienode()

    def addfolder(self,path):
        cur=self.root
        path = [dir for dir in path.split('/') if dir]
        print(path)
        for char in path:
            if char not in cur.children:
                cur.children[char]=Trienode()
            cur=cur.children[char]
            if cur.endoffolder==True:
                return False
        cur.endoffolder=True
        return True




class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:

        res=[]

        trie=Trie()
        sorted_path = sorted(folder, key=len)
        for path in sorted_path:

            if trie.addfolder(path):
                res.append(path)

        return res


        

        