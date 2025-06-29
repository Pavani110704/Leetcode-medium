class Solution(object):
    def reverseWords(self, s):
        s1 = s.split()
        s1 = s1[::-1]
        result = ' '.join(s1)
        return result
