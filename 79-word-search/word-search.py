class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        visited=set()
        
        def backtrack(i,j,cur):
            if cur==len(word):
                return True
            if (i<0 or j<0 or i>=len(board) or j>=len(board[0]) or (i,j) in visited or board[i][j]!=word[cur]):
                return False
            
            visited.add((i,j))

            res= (backtrack(i+1,j,cur+1) or backtrack(i,j+1,cur+1) or backtrack(i-1,j,cur+1) or backtrack(i,j-1,cur+1))
           
            visited.remove((i,j))
            
            return res


        for row in range(len(board)):
            for col in range(len(board[0])):
                    if board[row][col]==word[0]:
                        if backtrack(row,col,0):
                            return True
                        
        return False