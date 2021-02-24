from collections import defaultdict, deque
class Solution(object):
    def __init__(self):
        self.graph = defaultdict(list)
        self.indegrees = defaultdict(int)
        self.queue = deque()
        self.visited = set()
        
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if numCourses == 0:
            return True
        if len(prerequisites) <= 1:
            return True
   
        for course in prerequisites:
            dep = course[0]
            prereq = course[1]
            self.graph[prereq].append(dep)
            self.indegrees[dep] +=1
            self.indegrees[prereq] +=0
        
        for course in range(numCourses):
            if self.indegrees[course] == 0:
                self.queue.append(course)
        
        while self.queue:
            prereq = self.queue.popleft()
            self.visited.add(prereq)
            courses = self.graph[prereq]
            for course in courses:
                self.indegrees[course] -=1
                if self.indegrees[course] == 0:
                    self.queue.append(course)
                    
        return len(self.visited) == numCourses
                
     # 4 1 2
     # 1 3
     # 2 3
     # 3 0
            
        
