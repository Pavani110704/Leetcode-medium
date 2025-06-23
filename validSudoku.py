class Solution(object):
    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue

                # Check if value already exists in current row
                if val in rows[i]:
                    return False
                rows[i].add(val)

                # Check if value already exists in current column
                if val in cols[j]:
                    return False
                cols[j].add(val)

                # Check if value already exists in current 3x3 box
                box_index = (i // 3) * 3 + (j // 3)
                if val in boxes[box_index]:
                    return False
                boxes[box_index].add(val)

        return True
