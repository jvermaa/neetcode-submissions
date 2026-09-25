class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Go through each row and check for repeats
        # Go through each col and check for repeats
        # Go through each small sub-square for repeats

        rows = defaultdict(set) # So rows would be a dictionary of a set. And the goal is to return False if we every come across a value whihc is already in the set for that row.
        cols = defaultdict(set)
        sub_square = defaultdict(set)

        ROWS = len(board)
        COLS = len(board[0])

        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in sub_square[(r//3, c//3)]):
                    return False
                
                if board[r][c] != '.':
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    sub_square[(r//3, c//3)].add(board[r][c])
        
        return True

