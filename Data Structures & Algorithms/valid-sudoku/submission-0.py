class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # need to skip if the current box has a .
        # split sets into 9 

        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(9)]

        for row in range(9):
            for column in range(9):
                valid = board[row][column]
                if valid == '.':
                    continue#skip
                box = (row // 3) * 3 + (column // 3)
                if valid in rows[row] or valid in cols[column] or valid in boxes[box]:# if already in, then it's a duplicate 
                    return False
                rows[row].add(valid)
                cols[column].add(valid)
                boxes[box].add(valid)
        return True








        
        