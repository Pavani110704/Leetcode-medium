class Solution(object):
    def longestPalindrome(self, s):
        max_len = 0
        result = ""

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                sub = s[i:j]
                if sub == sub[::-1] and len(sub) > max_len:
                    result = sub
                    max_len = len(sub)

        return result
