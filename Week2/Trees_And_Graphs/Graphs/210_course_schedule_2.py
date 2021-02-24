from collections import defaultdict
from collections import deque
class Solution(object):
    def __init__(self):
        self.graph = defaultdict(list)
        self.indegrees = defaultdict(int)
        self.queue = deque()
        self.visited = []
    
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if numCourses == 0:
            return []
   
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
            self.visited.append(prereq)
            courses = self.graph[prereq]
            for course in courses:
                self.indegrees[course] -=1
                if self.indegrees[course] == 0:
                    self.queue.append(course)  
        if len(self.visited) == numCourses:
            return self.visited
        return []
    
    
    """
    Time complexity : O(v+e)
    Space complexity: O(v+e)
    """
     # 4 1 2
     # 1 3
     # 2 3
     # 3 0
        
    
        
        
        
