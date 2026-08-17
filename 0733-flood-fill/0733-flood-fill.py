class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        visited = set()

        def bfs(r, c, o):
            q = deque([(r, c)])
            visited.add((r, c))
            image[r][c] = color
            
            while q:
                row, col = q.popleft()

                for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr, nc = row+dr, col+dc

                    if (
                        nr>=0 and 
                        nr<rows and
                        nc>=0 and
                        nc<cols and
                        image[nr][nc] == o and
                        (nr, nc) not in visited
                    ):
                        visited.add((nr, nc))
                        image[nr][nc] = color
                        q.append((nr, nc))


        bfs(sr, sc, image[sr][sc])
        return image
