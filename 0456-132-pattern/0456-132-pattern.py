class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        st = []
        m = nums[0]

        for i in range(1, len(nums)):
            while st and nums[i] >= nums[st[-1][0]]:
                st.pop()
            
            if st and nums[i] > st[-1][1]:
                return True
            
            st.append((i, m))
            m = min(m, nums[i])

        return False