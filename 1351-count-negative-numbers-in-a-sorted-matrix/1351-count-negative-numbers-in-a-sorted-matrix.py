class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        cols = len(grid[0])
        rows = len(grid)

        
        cnt = 0

        for i in range(rows):
            start = 0
            end = cols - 1
            first_neg = cols
            while start <= end:
                mid = start + (end-start) // 2

                if grid[i][mid] < 0:
                    first_neg = mid
                    end = mid - 1
                else: 
                    start = mid + 1
            cnt += cols - first_neg
            
        return cnt

