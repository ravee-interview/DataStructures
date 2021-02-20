from collections import deque
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        if n == 0:
            return 0
        
        self.graph = defaultdict(list) #for this question, can define a list like in 785 - Bipartite graph
        self.visited = set()
        num_components = 0
        for edge in edges:
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])
        
        for i in range(n):
            if i not in self.visited:
                num_components +=1
                self.dfs(i)
        return num_components
        
    def dfs(self,node):
        if node in self.visited:
            return
        self.visited.add(node) #you are now visiting this node, add to queue
        for neighbor in self.graph[node]:
            self.dfs(neighbor)
            
    
            
    '''
    Comments : Missed a testcase where len(edges) == 0 but n = 1
    Time Complexity = O(V+E)
    Space complexity = O(V+E)
    [[0, 1], [1, 2], [3, 4]]
    
    0: 1
    1: 0 2
    2: 1
    3: 4
    4: 3
    
    visited = (0, 1, 2, 3, 4)
    num_components = 1
    i = 0
    
    '''        
        
    
