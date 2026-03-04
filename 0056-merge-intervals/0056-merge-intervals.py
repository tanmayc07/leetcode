class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:        
        result = []
        intervals.sort()
        current_interval = intervals[0]

        for i in range(1, len(intervals)):
            if current_interval[1] >= intervals[i][0]:
                merged_interval = [current_interval[0], max(intervals[i][1], current_interval[1])]
                current_interval = merged_interval
            else:
                result.append(current_interval)
                current_interval = intervals[i]

        result.append(current_interval)
        
        return result



