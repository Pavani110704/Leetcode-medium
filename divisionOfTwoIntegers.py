class Solution(object):
    def divide(self, dividend, divisor):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Handle overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Sign of the result
        negative = (dividend < 0) != (divisor < 0)

        # Work with absolute values
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0

        # Subtract largest shifted divisor each time
        while dividend >= divisor:
            temp = divisor
            multiple = 1

            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            dividend -= temp
            quotient += multiple

        return -quotient if negative else quotient
