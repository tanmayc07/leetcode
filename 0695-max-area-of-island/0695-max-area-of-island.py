class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0

        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def bfs(r, c, a):
            q = deque([(r, c)])

            while q:
                row, col = q.popleft()
                for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr, nc = row+dr, col+dc

                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]!=0:
                        grid[nr][nc] = 0 
                        a += 1
                        q.append((nr, nc))

            return a
                


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    area = bfs(r, c, 1)
                    max_area = max(max_area, area)

        return max_area