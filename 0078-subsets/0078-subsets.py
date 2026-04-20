class Solution:
    def subsets(self, nums):
        result = []
        def backtrack(start, path):
            result.append(path[:])  # add current subset
            for i in range(start, len(nums)):
                path.append(nums[i])        # choose
                backtrack(i + 1, path)     # explore
                path.pop()                 # un-choose
        backtrack(0, [])
        return result