class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited_set = set()
        adjacency_list = {i:[] for i in range(numCourses)}

        for current_course, pre_requisite in prerequisites:
            adjacency_list[current_course].append(pre_requisite)

        def dfs(current_course):
            if current_course in visited_set:
                return False
            if adjacency_list[current_course] == []:
                return True
            
            visited_set.add(current_course)

            for pre_req in adjacency_list[current_course]:
                if not dfs(pre_req):
                    return False
            visited_set.remove(current_course)
            adjacency_list[current_course] = []
            return True
        
        for current_course in range(numCourses):
            if not dfs(current_course): return False

        return True