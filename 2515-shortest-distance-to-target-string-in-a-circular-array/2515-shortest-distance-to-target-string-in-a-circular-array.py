class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        f = 0
        n = len(words)
        p = startIndex
        l, cnt = float('inf'), 0
        while p<=2*len(words)-1:
            if words[p%n] == target:
                f = 1
                l = min(l, cnt)
            cnt += 1
            p += 1

        p = startIndex-1
        cnt = 0
        while (p+n)%n!=startIndex:
            cnt += 1
            if words[(p+n)%n] == target:
                f = 1
                l = min(l, cnt)
            p -= 1

        return l if f else -1
         

