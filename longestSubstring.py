class Solution(object):
    def lengthOfLongestSubstring(self, s):
        current = ""
        max_len = 0

        for char in s:
            if char in current:
                # Remove characters from the beginning up to and including the repeated char
                index = current.index(char)
                current = current[index + 1:]
            current += char
            max_len = max(max_len, len(current))

        return max_len
