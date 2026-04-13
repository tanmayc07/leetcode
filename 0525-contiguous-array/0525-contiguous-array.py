class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hm = defaultdict(int)
        cnt = 0
        mx_len = 0
        hm[0] = -1

        for i in range(len(nums)):
            if nums[i]==0: cnt -= 1
            else: cnt += 1

            if cnt in hm:
                mx_len = max(mx_len, i - hm[cnt])
            else:
                hm[cnt] = i

        return mx_len
