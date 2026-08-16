class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        for num, freq in collections.Counter(nums).most_common(k):
            ans.append(num)
        return ans