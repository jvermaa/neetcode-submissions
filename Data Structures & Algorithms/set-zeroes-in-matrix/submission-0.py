class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        store = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    store.append((i,j))
        
        
        for r,c in store:
            for gotcha in range(len(matrix)):
                matrix[gotcha][c] = 0 
            for gotcha in range(len(matrix[0])):
                matrix[r][gotcha] = 0 