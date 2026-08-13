class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_map = {}
        for i, num in enumerate(nums):
            needed = target - num
            if needed in value_map:
                return [value_map[needed],i]
            value_map[num] = i