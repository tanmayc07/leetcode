import heapq

class EventManager:

    def __init__(self, events: list[list[int]]):
        self.active = {}
        self.pq = []
        for i in range(len(events)):
            heapq.heappush_max(self.pq, [events[i][1], -events[i][0]])
            self.active[events[i][0]] = events[i][1]

    def updatePriority(self, eventId: int, newPriority: int) -> None:
        self.active[eventId] = newPriority
        heapq.heappush_max(self.pq, [newPriority, -eventId])

    def pollHighest(self) -> int:
        while self.pq:
            pr, id = heapq.heappop_max(self.pq)
            id = -id

            if id in self.active and self.active[id]==pr:
                del self.active[id]
                return id
        
        return -1
                
        

# Your EventManager object will be instantiated and called as such:
# obj = EventManager(events)
# obj.updatePriority(eventId,newPriority)
# param_2 = obj.pollHighest()