class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = [intervals[0]]

        for i in range(1, len(intervals)):
            last_merged = res[-1]
            current = intervals[i]

            if last_merged[1] >= current[0]:
                last_merged[1] = max(current[1], last_merged[1])
            else:
                res.append(current)
        
        return res