class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        livecells=[]
        for i in range(len(board)):
            for j in range(len(board[0])):
            
                sum=0
                start_row=i-1
                start_col=j-1
                for x in range(start_row,start_row+3):
                    for y in range(start_col,start_col+3):

                        if(x>=0 and y>=0 and x<len(board) and y<(len(board[0]))):
                            sum+=board[x][y]
                livecells.append(sum)
        n=0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j]==1):
                    livecells[n]-=1
                    if(livecells[n]<2):
                        board[i][j]=0
                    elif(livecells[n]==2 or livecells[n]==3):
                        board[i][j]=1
                    elif(livecells[n]>3):
                        board[i][j]=0
                else:
                    if(livecells[n]==3):
                        board[i][j]=1
                n+=1
                    



                
            