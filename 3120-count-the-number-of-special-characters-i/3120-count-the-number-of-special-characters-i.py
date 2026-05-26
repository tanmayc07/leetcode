class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        st = set(word)
        cnt = 0
        print(st)
        for l in st:
            if l.islower() and l.upper() in st:
                cnt += 1
        return cnt