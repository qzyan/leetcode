class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = self.build_graph(numCourses, prerequisites)
        indegrees = self.get_indegrees(numCourses, graph)

        queue = collections.deque()
        for course, indegree in indegrees.items():
            if indegree == 0:
                queue.append(course)
        sorted_courses = []
        while queue:
            curr_course = queue.popleft()
            sorted_courses.append(curr_course)
            for next_course in graph[curr_course]:
                indegrees[next_course] -= 1
                if indegrees[next_course] == 0:
                    queue.append(next_course)

        return sorted_courses if len(sorted_courses) == numCourses else []

    def build_graph(self, num, prereqs):
        graph = {i: [] for i in range(num)}

        for to_c, from_c in prereqs:
            graph[from_c].append(to_c)

        return graph

    def get_indegrees(self, num, graph):
        indegrees = {i: 0 for i in range(num)}
        for from_c, to_cs in graph.items():
            for to_c in to_cs:
                indegrees[to_c] += 1

        return indegrees