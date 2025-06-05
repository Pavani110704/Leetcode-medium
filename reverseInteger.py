class Solution(object):
    def reverse(self, x):
        r = 0
        l = list(map(int, str(x)))
        
        l1 = l.reverse()
        
        result = int("".join(map(str, l1)))

        if x<0:
            result = -result
        return result
    
