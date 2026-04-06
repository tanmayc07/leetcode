import heapq

class EventManager:

    def __init__(self, events: list[list[int]]):
        self.mp = {}
        self.pq = []

        for e in events:
            heapq.heappush(self.pq, [-e[1], e[0]])
            self.mp[e[0]] = e[1]

    def updatePriority(self, eventId: int, newPriority: int) -> None:
        heapq.heappush(self.pq, [-newPriority, eventId])
        self.mp[eventId] = newPriority

    def pollHighest(self) -> int:
        while self.pq:
            pair = heapq.heappop(self.pq)
            if pair[1] in self.mp and self.mp[pair[1]]==-pair[0]:
                del self.mp[pair[1]]
                return pair[1]
        return -1


# Your EventManager object will be instantiated and called as such:
# obj = EventManager(events)
# obj.updatePriority(eventId,newPriority)
# param_2 = obj.pollHighest()