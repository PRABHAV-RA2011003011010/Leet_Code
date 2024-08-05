class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        li=[]
        for i in range(9):
            for j in range(9):
                if(board[i][j]!="."):
                    li+=[(i,board[i][j]),(board[i][j],j),(board[i][j],i//3,j//3)]
        return True if(len(li)==len(set(li))) else False

        