class Solution:
    def digit_cnt(self, num, digit):
        n1 = num
        cnt = 0
        while n1:
            d = n1%10
            if d==digit: cnt += 1
            n1 //= 10
        return cnt

    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        tc = 0
        for i in range(len(nums)):
            tc += self.digit_cnt(nums[i], digit)
        return tc