import collections

class Solution(object):
    def topKFrequent(self, nums, k):
        # Step 1: Frequency map toiri kora O(n)
        count = collections.Counter(nums)

        # Step 2: Bucket array banano (Index = Frequency)
        # Array size len(nums) + 1 rakhte hobe because max frequency len(nums) hote pare
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            buckets[freq].append(num)

        # Step 3: Pechon (max freq) theke scan kora k elements pawa obdi
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res