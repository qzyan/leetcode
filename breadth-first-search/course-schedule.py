class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = self.build_graph(numCourses, prerequisites)
        course_indegree = self.calc_indegree(graph)

        queue = collections.deque()
        for course, indegree in course_indegree.items():
            if indegree == 0:
                queue.append(course)

        count = 0
        while queue:
            curr_course = queue.popleft()
            count += 1
            for next_course in graph[curr_course]:
                course_indegree[next_course] -= 1
                if course_indegree[next_course] == 0:
                    queue.append(next_course)

        return count == numCourses

    def build_graph(self, course_count, prerequisites):
        graph = {course: set() for course in range(course_count)}
        for to_c, from_c in prerequisites:
            graph[from_c].add(to_c)
        
        return graph

    def calc_indegree(self, graph):
        course_indegree = {course: 0 for course in graph}
        for from_course, to_courses in graph.items():
            for to_course in to_courses:
                course_indegree[to_course] += 1

        return course_indegree
