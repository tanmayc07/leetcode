class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = defaultdict(set)
        box = defaultdict(set)

        for i in range(9):
            row = set()
            for j in range(9):
                val = board[i][j]
                if val == ".": continue
                if val in row: return False
                if val in col[j]: return False
                if val in box[(i//3, j//3)]: return False

                row.add(val)
                col[j].add(val)
                box[(i//3, j//3)].add(val)

        return True
