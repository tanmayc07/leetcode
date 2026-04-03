class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = 0
        cnt = 0

        for p2 in range(1, len(nums)):
            if nums[p2] != nums[p1]:
                cnt += 1
                nums[p1+1], nums[p2] = nums[p2], nums[p1+1]
                p1 += 1

        return cnt+1

