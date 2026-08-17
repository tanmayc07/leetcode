class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        visited = set()

        def dfs(r, c, o):
            if (
                r<0 or 
                r>=rows or
                c<0 or
                c>=cols or
                image[r][c] != o or
                (r, c) in visited
            ):
                return
            
            visited.add((r, c))
            image[r][c] = color

            dfs(r+1, c, o)
            dfs(r-1, c, o)
            dfs(r, c+1, o)
            dfs(r, c-1, o)

        dfs(sr, sc, image[sr][sc])
        return image
