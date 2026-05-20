class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        m = defaultdict(int)
        ans = []
        for i in range(len(A)):
            m[A[i]] += 1
            m[B[i]] += 1
            cnt = 0
            for k, v in m.items():
                if v==2: cnt += 1
            ans.append(cnt)
        return ans