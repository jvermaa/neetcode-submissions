class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        output = []
        no_prereq = set()
        current_path = set()

        # make the adjacency list

        # make the DFS
            # The dfs checks for cycles and no prereqs
            # The dfs checks for the pre reqs of its own preReqs
            # If all the pre reqs had no pre reqs or they get added in order
            # Then the parent course also gets added
        
        # Then we run the DFS on each course
            # Since one course could be fine while the other could be cycle
            # We know that two unconnected courses can also do the above
            # That is why we need to run the DFS for every course individually
        pre_req = {}
        for i in range(numCourses):
            pre_req[i] = []
        
        for crs, pre in prerequisites:
            pre_req[crs].append(pre)
        
        def dfs(crs):
            if crs in current_path:
                return False
            if crs in no_prereq:
                return True
            
            current_path.add(crs)
            for pres in pre_req[crs]:
                if not dfs(pres):
                    return False
            
            no_prereq.add(crs)
            output.append(crs)
            current_path.remove(crs)

            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return output

