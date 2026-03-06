class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        st = []

        for i in range(len(nums)):
            if nums[i] != 0:
                st.append(nums[i])
        
        l = 0
        for i in range(len(st)):
            nums[i] = st[i]
            l = i

        l += 1
        while l < len(nums):
            nums[l] = 0
            l += 1
        