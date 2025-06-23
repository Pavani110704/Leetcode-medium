class Solution(object):
    def countAndSay(self, n):
        result = "1"

        for _ in range(n - 1):
            temp = ""
            count = 1
            for j in range(1, len(result)):
                if result[j] == result[j - 1]:
                    count += 1
                else:
                    temp += str(count) + result[j - 1]
                    count = 1
            temp += str(count) + result[-1]  # Append the last group
            result = temp

        return result
