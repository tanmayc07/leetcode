import heapq as hq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = nums
        hq.heapify(arr)
        return hq.nlargest(k, arr)[k-1]