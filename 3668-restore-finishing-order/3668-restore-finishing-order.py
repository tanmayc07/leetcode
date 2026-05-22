class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        hs = set(friends)
        ans = []
        for i in order:
            if i in hs: ans.append(i)
        return ans