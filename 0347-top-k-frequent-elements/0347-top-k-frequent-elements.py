class Solution:
    def topKFrequent(self, nums, k):
        from collections import Counter

        # Step 1: Count frequency
        count = Counter(nums)

        # Step 2: Create buckets
        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            bucket[freq].append(num)

        # Step 3: Collect top k frequent elements
        result = []
        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result