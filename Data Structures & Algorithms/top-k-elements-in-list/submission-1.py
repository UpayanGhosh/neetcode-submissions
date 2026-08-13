import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        count_map = Counter(nums)
        sorted_items = sorted(count_map.items(), key=lambda x: x[1], reverse=True)
        result = [key for key, value in sorted_items[:k]] 
        return result

        


        