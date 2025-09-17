class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp = {}
        st = []

        for num in reversed(nums2):
            while st and st[-1] <= num:
                st.pop()
            mp[num] = -1 if not st else st[-1]
            st.append(num)
        
        return [mp[num] for num in nums1]

        