from collections import deque
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        
        def toggle_color(x):
            return x^1
            
        color = {}
        RED = 0
        
        for node in range(len(graph)):
            if node not in color:
                queue = deque()
                queue.append(node)
                color[node] = RED
                while queue:
                    node = queue.popleft()
                    #color neighbors and put on queue
                    for neighbor in graph[node]:
                        if neighbor not in color:
                            queue.append(neighbor)
                            color[neighbor] = toggle_color(color[node])
                        elif color[node] == color[neighbor]:
                            return False
        return True
        
#         Questions:
        
#         1. Are there any benefits of using dfs over bfs for this question?

        '''
    node   neighbor     potential bipartites
        0 : [1,3]       [2]
        1 : [0,2]       [3]
        2 : [1,3]       [0]
        3 : [0,2]       [1]
        
        Time Complexity: O(V+E)
        Space Complexity: O(V+E)
        
        '''
