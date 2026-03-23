class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        row = set()
        col = set()
        is_valid = True
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] in row:
                    is_valid =  False
                    break
                row.add(matrix[i][j])
                
                if matrix[j][i] in col:
                    is_valid = False
                    break
                col.add(matrix[j][i])
            row.clear()
            col.clear()
            
            if not is_valid: break

        return is_valid
                