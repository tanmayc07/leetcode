class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hm = {}
        hm[0] = 1

        res = 0
        ps = 0

        for num in nums:
            ps += num
            if ps - k in hm:
                res += hm[ps-k]
            
            hm[ps] = hm.get(ps, 0) + 1
    
        return res