class Solution(object):
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)
        
        # Create a (m+1) x (n+1) DP table
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base cases: convert empty string to the other by insertions/deletions
        for i in range(m + 1):
            dp[i][0] = i  # delete all characters from word1
        for j in range(n + 1):
            dp[0][j] = j  # insert all characters to word1 to make word2

        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  # characters match
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],    # delete
                        dp[i][j - 1],    # insert
                        dp[i - 1][j - 1] # replace
                    )

        return dp[m][n]
