class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        course_graph = {i: [] for i in range(numCourses)} # Key: num, val: [courses]

        # create the graph
        
        for course, prereq in prerequisites:
            if course not in course_graph:
                course_graph[course] = []
            course_graph[course].append(prereq)

        visited = set()

        def dfs(course):
            if course in visited:
                return False

            if course_graph[course] == []:
                return True
            
            visited.add(course)
            for req in course_graph[course]:
                if not dfs(req):
                    return False
            
            
            visited.remove(course)
            course_graph[course] = []
            return True

        # traverse the graph until we find its no pre req then we pop

        # if all gets popped then return True
        # else return false 
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True