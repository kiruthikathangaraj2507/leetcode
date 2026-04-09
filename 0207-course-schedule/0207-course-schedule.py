class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = {i: [] for i in range(numCourses)}

        # Build graph
        for a, b in prerequisites:
            graph[a].append(b)

        visit = set()   # visited nodes
        path = set()    # current path (for cycle detection)

        def dfs(course):
            if course in path:
                return False  # cycle found
            if course in visit:
                return True   # already checked

            path.add(course)

            for pre in graph[course]:
                if not dfs(pre):
                    return False

            path.remove(course)
            visit.add(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True
        