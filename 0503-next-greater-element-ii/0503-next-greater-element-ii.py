class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        st = []
        res = [-1] * len(nums)

        for i in range(2*len(nums)):
            curr = i%len(nums)
            while st and nums[st[-1]] < nums[curr]:
                res[st.pop()] = nums[curr]
            st.append(curr)

        return res 