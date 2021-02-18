from collections import deque, defaultdict
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        #Create a {} from and to
        self.dest = defaultdict(list)
        # {
        #     from: to
        # }
        
        for ticket in tickets:
            self.dest[ticket[0]].append(ticket[1])
            
        for to, paths in self.dest.items():
            paths.sort(reverse=True)
            print paths
        
        self.iten = []
        start = "JFK"
        self.dfs(start)
        
        return self.iten[::-1]
        
    def dfs(self,start):
        paths = self.dest[start]
        while paths:
            next_path = paths.pop()
            self.dfs(next_path)
        self.iten.append(start)
        
