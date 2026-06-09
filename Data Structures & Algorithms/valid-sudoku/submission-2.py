class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = defaultdict(set)
        """
         rowset = {
            0 : set()
            1 : set()
            2 : set()
            3 : set()
            4 : set()
            5 : set()
        }
        """
        colSet = defaultdict(set)
        boxSet = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rowSet[r]:
                    return False
                if board[r][c] in colSet[c]:
                    return False
                if board[r][c] in boxSet[(r//3,c//3)]:
                    return False
                rowSet[r].add(board[r][c])
                colSet[c].add(board[r][c])
                boxSet[(r//3,c//3)].add(board[r][c])
        
        return True
                
"""
have a list of set for each row
have a list set for each column
have a list set for each box
iterate trough list and place each num in respective sets
if a number is already in a set its an invalid sudoku, return false
return true




"""