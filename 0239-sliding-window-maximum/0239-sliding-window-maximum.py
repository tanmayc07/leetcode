class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i, j, res, q = 0, 0, [], deque()

        while j<len(nums):
            while q and q[-1] < nums[j]:
                q.pop()
            q.append(nums[j])

            if j-i+1 == k:
                res.append(q[0])
                if nums[i] == q[0]:
                    q.popleft()
                i += 1
            j += 1
        return res
