class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def isSafe(row,col,board,n):
            duplicateRow = row
            duplicateCol = col
            
            while row >=0 and col >=0:
                if board[row][col] == "Q": return False
                row -= 1
                col -= 1
            
            row = duplicateRow
            col = duplicateCol 
            while col >= 0:
                if board[row][col] == "Q": return False
                col -= 1
                
            row = duplicateRow
            col = duplicateCol 
            while row < n and col >= 0:
                if board[row][col] == "Q": return False
                row += 1
                col -=1
            
            return True
                
            
        
        def solve( col,board,ans,n):
            if col == n:
                temp = list()
                for x in board:
                    temp.append(x)
                ans.append(temp)
                return 
            
            for y in range(0,n):
                if isSafe(y,col,board,n):
                    board[y] = board[y][0:col]+"Q"+board[y][col+1:]
                    solve(col+1,board,ans,n)
                    board[y] = board[y][0:col]+"."+board[y][col+1:]
                    # board[y][col] = "."
        
        
        ans = []
        s = "."*n
        board =[]
        for x in range(n):
            board.append(s)
            
        solve(0,board,ans,n)
        return ans
            