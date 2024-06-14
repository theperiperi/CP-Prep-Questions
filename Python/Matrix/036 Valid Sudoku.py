class Solution(object):
    def isValidSudoku(self, board):
        sq = []
        for row in range(9):
            for column in range(9):
                ele = board[row][column]
                if ele != '.':
                    sq+= [(row, ele), (ele, column), (row// 3, column // 3, ele)]
        return len(sq) == len(set(sq))
