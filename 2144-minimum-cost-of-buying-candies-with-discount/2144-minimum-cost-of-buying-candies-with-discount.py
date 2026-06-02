class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        if len(cost) <= 2: return sum(cost)
        q = []

        for c in cost: heapq.heappush(q, -c)

        ct = 0
        while q:
            if len(q) >= 3:
                a = -heapq.heappop(q)
                b = -heapq.heappop(q)
                c = -heapq.heappop(q)
                ct += a + b
            else:
                ct += sum(-x for x in q)
                q = []
        
        return ct
        
        
