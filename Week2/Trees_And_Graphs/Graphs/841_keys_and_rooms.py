class Solution(object):
    
    def __init__(self):
        self.graph = [] #for this questions, declaing it as a list
        self.visited = set()
        self.num_nodes = 0
    
    def create_graph(self, graph):
        self.graph = graph
        self.num_nodes = len(graph)
        
    def dfs(self,node):
        if node in self.visited:
            return
        self.visited.add(node)
        for neighbor in self.graph[node]:
            self.dfs(neighbor)
               
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        self.create_graph(rooms)
        
        self.dfs(0)
        if len(self.visited) == self.num_nodes:
            return True
        return False
        
"""
Time Complexity : O(V+E)
Space Complexity : O(V+E)
"""
