class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = self.build_graph(numCourses, prerequisites)
        course_indegree = self.calc_indegree(graph)

        paths = []
        path = []
        visited = set()
        for course, indegree in course_indegree.items():
            if indegree == 0:
                path.append(course)
                visited.add(course)
                self.dfs(graph, course_indegree, path, paths, visited)
                path.pop()
                visited.remove(course)

        return paths[0]

    def dfs(self, graph, course_indegree, path, paths, visited):
        if len(path) == len(graph):
            paths.append(path[:])
            return
        
        curr_course = path[-1]
        for next_course in graph[curr_course]:
            course_indegree[next_course] -= 1

        for next_course in graph:
            if next_course in visited:
                continue

            if course_indegree[next_course] == 0:
                path.append(next_course)
                visited.add(next_course)
                self.dfs(graph, course_indegree, path, paths, visited)
                path.pop()
                visited.remove(next_course)

        for next_course in graph[curr_course]:
            course_indegree[next_course] += 1

    def build_graph(self, numCourses, prerequisites):
        graph = {c: set() for c in range(numCourses)}
        for to_c, from_c in prerequisites:
            graph[from_c].add(to_c)

        return graph

    def calc_indegree(self, graph):
        course_indegree = {c: 0 for c in graph}
        for from_c, to_cs in graph.items():
            for to_c in to_cs:
                course_indegree[to_c] += 1

        return course_indegree

            