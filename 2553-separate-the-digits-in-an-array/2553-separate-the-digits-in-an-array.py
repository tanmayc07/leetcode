class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        r = []
        for num in nums:
            d = []
            while num:
                d.append(num%10)
                num //= 10
            r.extend(d[::-1])
        return r