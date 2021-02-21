from collections import deque
class Solution(object):
    def __init__(self):
        self.graph = collections.defaultdict()
        
    def create_graph(self,edges):
        self.graph = collections.defaultdict(list)
        for edge in edges:
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])
        
    def gardenNoAdj(self, n, paths):
        """
        :type n: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        #Create a graph
        self.create_graph(paths)
        
        color = [0 for _ in range(n+1)]
        all_colors = {1,2,3,4}
        
        for node in range(1,n+1):
            queue = deque()
            queue.append(node)
            
            while queue:
                node = queue.popleft()
                if color[node] == 0: #not assigned a type
                    taken_colors = set()
                    for neighbor in self.graph[node]:
                        taken_colors.add(color[neighbor])
                    color[node] = (all_colors - taken_colors).pop()
        
        color.pop(0) # delete the 0th index
        return color
                
    
        '''


        Time complexity O(V+E)
        Space complexity O(V+E)
            
        find bipartite graph and color
        give each partition a color from available colors

        
        1: 2 4 3
        2: 1 3 4
        3: 2 4 1
        4: 1 3 2
        
        
        '''

            
        
            
        
