class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        mp = Counter()

        for i in range(len(word)):
            if word[i].islower():
                mp[word[i]] = i
            if word[i].isupper() and word[i] not in mp:
                mp[word[i]] = i

        cnt = 0
        for k, v in mp.items():
            if k.islower():
                if k.upper() in mp and v<mp[k.upper()]:
                    cnt += 1
        print(mp)
        return cnt
