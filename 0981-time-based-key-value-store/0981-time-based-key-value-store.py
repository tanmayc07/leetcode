class TimeMap:

    def __init__(self):
        self.m = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.m:
            self.m[key] = [(value, timestamp)]
        else:
            self.m[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.m[key]
        start, end = 0, len(arr)-1
        res = ''

        while start <= end:
            mid = start + (end-start)//2

            if arr[mid][1] <= timestamp:
                res = arr[mid][0]
                start = mid + 1
            else:
                end = mid - 1

        return res 


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)