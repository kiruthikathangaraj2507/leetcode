class Solution:
    def rob(self, nums):
        prev = 0   # dp[i-2]
        curr = 0   # dp[i-1]
        for num in nums:
            temp = max(curr, prev + num)
            prev = curr
            curr = temp
        return curr