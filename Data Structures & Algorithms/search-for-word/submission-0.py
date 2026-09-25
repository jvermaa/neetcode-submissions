class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        rows = len(board)
        cols = len(board[0])


        # The logic to search is basically searching in all 4 directions

        def dfs(r, c, i):
            if i == len(word): # This indicates we are at the end of the word, if we made it to the end of a word it means all the previous letters had to match so we found a match
                return True
            
            # All the conditions where it could fail or we know its the incorrect path

            if r<0 or c < 0 or r >= rows or c >= cols or (r,c) in visited or board[r][c] != word[i]:
                return False
            
            # If we passed the above checks it means we our current character matces the character on the board currently

            visited.add((r,c))

            #Check all 4 directions and atleast 1 direction would have the word
            res = dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1)

            # Now our this path is over so we will remove it from visiting
            visited.remove((r,c))

            return res

        # Search the possibility of the word from each letter

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        
        return False
