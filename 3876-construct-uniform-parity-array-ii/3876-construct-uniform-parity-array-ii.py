class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        mx = min(nums1)
        even_odd = 0 if mx%2 == 0 else 1

        f = 1
        for i in range(len(nums1)):
            if nums1[i]%2 != even_odd:
                p = nums1[i]-mx
                if p>=1 and p%2 != even_odd:
                    f = 0
                    break

        return f == 1
        