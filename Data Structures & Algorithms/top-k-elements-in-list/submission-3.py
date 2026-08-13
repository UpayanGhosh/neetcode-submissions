class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = []
        for num, freq in Counter(nums).most_common(k):
            answer.append(num)
        return answer
        