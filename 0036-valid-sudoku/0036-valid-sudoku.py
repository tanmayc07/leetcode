class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = defaultdict(set)
        box = defaultdict(set)

        for i in range(len(board)):
            row = set()
            for j in range(len(board[i])):
                if board[i][j] != ".":
                    if board[i][j] in row: return False
                    if board[i][j] in col[j]: return False
                    if board[i][j] in box[(i//3, j//3)]: return False

                    row.add(board[i][j]) 
                    col[j].add(board[i][j])
                    box[(i//3,j//3)].add(board[i][j])

        return True