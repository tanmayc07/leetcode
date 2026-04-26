class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        if len(nums)<=2: return nums
        res = [nums[0]]
        for i in range(1, len(nums)-1):
            f1 = True
            for j in range(0, i):
                if nums[j] >= nums[i]:
                    f1 = False
                    break

            f2 = True
            for j in range(i+1, len(nums)):
                if nums[j] >= nums[i]:
                    f2 = False
                    break

            if f1 or f2: res.append(nums[i])

        res.append(nums[-1])
        return res