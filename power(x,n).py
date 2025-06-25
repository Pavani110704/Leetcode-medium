class Solution(object):
    def myPow(self, x, n):
        result = 1
        for i in range(abs(n)):
            result *= x
        if n < 0:
            return 1.0 / result
        return result
