class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}

        for i in range(len(nums)):
            hm[nums[i]] = hm.get(nums[i], 0) + 1

        result = sorted(hm, key=lambda x: hm[x], reverse=True)

        return result[:k]