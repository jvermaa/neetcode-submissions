class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_matrix = {}
        visited = set()
        for course, pre in prerequisites:
            if course not in adj_matrix:
                adj_matrix[course] = [] 

            adj_matrix[course].append(pre)

        def dfs(course):

            if course in visited:
                return False

            if course not in adj_matrix:  # course has no prerequisites
                return True
                
            if adj_matrix[course] == []:
                return True
            
            visited.add(course)

            for i in adj_matrix[course]:
                if not dfs(i):
                    return False
            
            visited.remove(course)
            adj_matrix[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True