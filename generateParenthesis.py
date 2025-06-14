from collections import deque

class Solution(object):
    def generateParenthesis(self, n):
        result = []
        queue = deque()
        queue.append(("", 0, 0))  # (current_string, open_count, close_count)

        while queue:
            current, open_cnt, close_cnt = queue.popleft()

            if open_cnt == n and close_cnt == n:
                result.append(current)
            else:
                if open_cnt < n:
                    queue.append((current + "(", open_cnt + 1, close_cnt))
                if close_cnt < open_cnt:
                    queue.append((current + ")", open_cnt, close_cnt + 1))

        return result
