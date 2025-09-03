import heapq as hq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)
        res = []

        min_heap = []
        for p in points:
            eD = math.sqrt(p[0]**2 + p[1]**2)
            hq.heappush(min_heap, (eD, p))
            
        for i in range(k):
            res.append(hq.heappop(min_heap)[1])

        return res
            


            
