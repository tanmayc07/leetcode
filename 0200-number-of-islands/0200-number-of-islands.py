class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        counts = 0

        def dfs(r, c):
            if (
                r>=rows or
                c>=cols or
                r<0 or
                c<0 or
                (r, c) in visited or
                grid[r][c] == '0'
            ):
                return

            visited.add((r, c))
            
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r, c-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    dfs(r, c)
                    counts += 1

        return counts