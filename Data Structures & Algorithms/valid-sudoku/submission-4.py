class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        subBoxes = defaultdict(set)
        for i in range(9):
            colSet = set()
            rowSet = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in rowSet:
                        return False
                    rowSet.add(board[i][j])
                    if board[i][j] in subBoxes[(i//3,j//3)]:
                        return False
                    subBoxes[(i//3,j//3)].add(board[i][j])
                if board[j][i] != '.':
                    if board[j][i] in colSet:
                        return False
                    colSet.add(board[j][i])
        return True

