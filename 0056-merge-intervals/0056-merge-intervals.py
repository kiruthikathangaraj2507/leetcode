class Solution:
    def merge(self, intervals):
        # Step 1: Sort intervals
        intervals.sort(key=lambda x: x[0])

        merged = []

        for interval in intervals:
            # If no overlap OR first interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Merge intervals
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged