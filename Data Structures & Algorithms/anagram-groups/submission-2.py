class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)
        for words in strs:
            key = frozenset(collections.Counter(words).items())
            groups[key].append(words)
        return list(groups.values())
        