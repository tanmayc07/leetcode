class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        s1 = set()
        s2 = set()
        ans = []
        for i in range(len(A)):
            s1.add(A[i])
            s2.add(B[i])
            c = len(s1.intersection(s2))
            ans.append(c)
        return ans