class Solution:
    def longestPalindrome(self, s):
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        result = ""

        for i in range(len(s)):
            # Odd length palindrome
            temp1 = expand(i, i)
            if len(temp1) > len(result):
                result = temp1

            # Even length palindrome
            temp2 = expand(i, i+1)
            if len(temp2) > len(result):
                result = temp2

        return result