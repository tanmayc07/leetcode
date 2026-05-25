class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        c = Counter(nums)
        res = []
        for ke, v in c.items():
            if v >= k: res.extend([ke]*k)
            else: res.extend([ke]*v)
        return res
