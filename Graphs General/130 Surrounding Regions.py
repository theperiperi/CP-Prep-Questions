class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows=len(board)
        columns=len(board[0])

        def dfs(r,c):
            if r not in range(rows) or c not in range(columns) or board[r][c]!="O":
                return
            #temporary marking
            board[r][c]="T"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        #capture bordering O (O->T)
        for r in range(rows):
            for c in range(columns):
                if board[r][c]=="O" and (r in [0,rows-1] or c in [0,columns-1]):
                    dfs(r,c)
        
        #capture surround regions (O->X)
        for r in range(rows):
            for c in range(columns):
                if board[r][c]=="O":
                    board[r][c]="X"

        #uncapture surroundings(T->O)
        for r in range(rows):
            for c in range(columns):
                if board[r][c]=="T":
                    board[r][c]="O"
    
