class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            left = 0
            right = len(nums) - 1

            while i != left and i != right and left < right:
                current_sum = nums[left] + nums[right] + nums[i]
                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    break
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1

        return result