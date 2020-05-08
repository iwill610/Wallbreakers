class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if len(board)<=1:
            return
        
        row = len(board)
        col = len(board[0])
        
        #fix row 0
        for j in range(col):
            if board[row-row][j]=="O":
                self.check(board,row,col,row-row,j)
        for j in range(col):
            if board[row-1][j]=="O":
                self.check(board,row,col,row-1,j)       
        for i in range(row):
            if board[i][col-col]=="O":
                self.check(board,row,col,i,col-col)
        for i in range(row):
            if board[i][col-1]=="O":
                self.check(board,row,col,i,col-1)
        
        for i in range(row):
            for j in range(col):
                if board[i][j]!=8:
                    board[i][j]='X'
        for i in range(row):
            for j in range(col):
                if board[i][j]==8:
                    board[i][j]='O'   
    
    
    def check(self,board,row,col,x,y):
        if board[x][y]=="X" or board[x][y]==8:
            return
        board[x][y]=8
        if x==row-row:
            self.check(board,row,col,x+1,y)
        if x==row-1:
            self.check(board,row,col,x-1,y)
        if y==col-col:
            self.check(board,row,col,x,y+1)
        if y==col-1:
            self.check(board,row,col,x,y-1)
        if x!=row-row and x!=row-1 and y!=col-col and y!=col-1:
            self.check(board,row,col,x+1,y)
            self.check(board,row,col,x-1,y)
            self.check(board,row,col,x,y+1)
            self.check(board,row,col,x,y-1)    
        
        
        
        ###Attempt1
        # for i in range(len(board)):
        #     if len(board)==2:
        #         break
        #     elif i==(len(board)-(len(board)-1)):
        #         for j in range(len(board[i])):
        #             if j==1 and board[i][j-1]!="O" and board[i-1][j]!="O":
        #                 board[i][j]="X"
        #             elif j==(len(board)-(len(board)-2)) and board[i][j+1]!="O" and board[i+1][j]!="O":
        #                 board[i][j]="X"
        #     elif i == (len(board)-(len(board)-2)):
        #         for j in range(len(board[i])):
        #             if j==1 and board[i][j-1]!="O" and board[i+1][j]!="O":
        #                 board[i][j]="X"
        #             elif j==(len(board)-(len(board)-2)) and board[i][j+1]!="O" and board[i+1][j]!="O":
        #                 board[i][j]="X"
                