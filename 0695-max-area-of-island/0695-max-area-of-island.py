class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def dfs(r: int, c: int, a: int) -> int:
            if (
                r<0 or r>=rows or c<0 or c>=cols or grid[r][c]==0
            ):
                return 0
            
            grid[r][c] = 0
            a = 1
            
            # print(f"({r},{c},{a}) -> {a}")
            a += dfs(r+1, c, a)
            a += dfs(r-1, c, a)
            a += dfs(r, c+1, a)
            a += dfs(r, c-1, a)

            return a


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = dfs(r, c, 0)
                    max_area = max(max_area, area)

        return max_area