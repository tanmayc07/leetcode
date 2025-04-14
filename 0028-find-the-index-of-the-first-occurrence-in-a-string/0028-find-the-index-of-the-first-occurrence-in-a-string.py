class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        sz = len(needle)
        st = ""
        i, j = 0, 0
        while j<len(haystack):
            st += haystack[j]

            if j-i+1 == sz:
                if st == needle:
                    return i
                st = st[1:]
                i += 1
            j += 1
        return -1