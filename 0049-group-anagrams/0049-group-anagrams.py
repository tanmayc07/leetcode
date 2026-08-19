class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        result = []

        for key in strs:
            sorted_key = "".join(sorted(key))
            anagrams[sorted_key].append(key)

        for k, v in anagrams.items():
            result.append(v)

        return result
