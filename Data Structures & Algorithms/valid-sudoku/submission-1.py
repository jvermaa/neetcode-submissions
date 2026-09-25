class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_record = defaultdict(set)
        col_record = defaultdict(set)
        block_record = defaultdict(set) # 3x3 subsquares = 1 block
        
        #keys = (row,col) for r,c
        #key for block_record = (r//3, c//3)

        row = len(board)
        col = len(board[0])

        for r in range(row):
            for c in range(col):
                current = board[r][c]
                if current in row_record[r] or current in col_record[c] or current in block_record[(r//3,c//3)]:
                    return False
                
                if current != ".":
                    row_record[r].add(current)
                    col_record[c].add(current)
                    block_record[(r//3,c//3)].add(current)
        
        return True 