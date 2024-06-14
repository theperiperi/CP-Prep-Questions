class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def currently_live(board):
            live=[]
            dead=[]
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j]==1:
                        live.append([i,j])
                    else:
                        dead.append([i,j])
            return live,dead
        
        live,dead=currently_live(board)

        def count_live_neighbours(row,column,live):
            live_count=0
            if row+1<len(board) and [row+1,column] in live:
                live_count+=1
            if row-1>=0 and [row-1,column] in live:
                live_count+=1
            if column+1<len(board[0]) and [row,column+1] in live:
                live_count+=1
            if column-1>=0 and [row,column-1] in live:
                live_count+=1
            
            if column-1>=0 and row-1>=0 and [row-1,column-1] in live:
                live_count+=1
            if row+1<len(board) and column+1<len(board[0]) and [row+1,column+1] in live:
                live_count+=1
            if row-1>=0 and column+1<len(board[0]) and [row-1,column+1] in live:
                live_count+=1
            if row+1<len(board) and column-1>=0 and [row+1,column-1] in live:
                live_count+=1
            return live_count

        for element in live:            
            row=element[0]
            column=element[1]        
            live_count=count_live_neighbours(row,column,live)
            if live_count<2 or live_count>3:
                board[row][column]=0
        
        for element in dead:
            row=element[0]
            column=element[1]          
            live_count=count_live_neighbours(row,column,live)
            if live_count==3:
                board[row][column]=1
        


            

            
            
            
        
