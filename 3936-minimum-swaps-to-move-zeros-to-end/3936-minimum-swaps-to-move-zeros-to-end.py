class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        l, r = 0, len(nums)-1

        c = 0
        while l<r:
            while nums[r]==0:
                r -= 1
                if r <= 0: break
            if l>=r or r <= 0: break

            if nums[l]==0:
                nums[l], nums[r] = nums[r], nums[l]
                c += 1
            l += 1

        return c
