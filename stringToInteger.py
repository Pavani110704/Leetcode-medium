class Solution(object):
    def myAtoi(self, s):
        s = s.strip()  # Remove leading/trailing spaces
        if not s:
            return 0

        sign = 1
        result = 0
        i = 0

        # Handle optional sign
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1

        # Read digits
        while i < len(s) and '0' <= s[i] <= '9':
            result = result * 10 + int(s[i])
            i += 1

        result *= sign

        # Clamp to 32-bit signed int range
        if result < -2147483648:
            return -2147483648
        if result > 2147483647:
            return 2147483647

        return result