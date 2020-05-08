class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set() for i in range(9)]
        cols=[set() for i in range(9)]
        
        threeby3=[set() for i in range(9)]
        for row in range(len(board)):
            for col in board[row]:
                if col!=".":
                    if col in rows[row]:
                        return False
                    else:
                        
                        rows[row].add(col)
        
        for col in range(len(board[0])):
            for row in range(len(board)):
                if board[row][col]!=".":
                    if board[row][col] in cols[col]:
                        return False
                    else:
                        
                        cols[col].add(board[row][col])
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col]!='.':
                    if row<=2 and col<=2:
                        if board[row][col] in threeby3[0]:
                            return False
                        else:
                            threeby3[0].add(board[row][col])
                            continue
                            
                    elif row<=2 and col>2 and col<=5:
                        if board[row][col] in threeby3[1]:
                            return False
                        else:
                            threeby3[1].add(board[row][col])
                            continue
                    elif row<=2 and col>5:
                        if board[row][col] in threeby3[2]:
                            return False
                        else:
                            threeby3[2].add(board[row][col])
                            continue
                    elif row>2 and row<=5 and col<=2:
                        if board[row][col] in threeby3[3]:
                            return False
                        else:
                            threeby3[3].add(board[row][col])
                            continue
                    elif row>2 and row<=5 and col>2 and col<=5:
                        if board[row][col] in threeby3[4]:
                            return False 
                        else:
                            threeby3[4].add(board[row][col])
                            continue
                    elif row>2 and row<=5 and col>5:
                        if board[row][col] in threeby3[5]:
                            return False    
                        else:
                            threeby3[5].add(board[row][col])
                            continue
                    elif row>5 and col<=2:
                        if board[row][col] in threeby3[6]:
                            return False    
                        else:
                            threeby3[6].add(board[row][col])
                            continue
                    elif row>5 and col>2 and col<=5:
                        if board[row][col] in threeby3[7]:
                            return False    
                        else:
                            threeby3[7].add(board[row][col])
                            continue
                    elif row>5 and col>5:
                        if board[row][col] in threeby3[8]:
                            return False    
                        else:
                            threeby3[8].add(board[row][col])
                            continue
                        
        return True