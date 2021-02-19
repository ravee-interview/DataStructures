from collections import defaultdict
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        
        self.graph = defaultdict(defaultdict)
        #build the graph
        for (dividend, divisor),value in zip(equations,values):
            self.graph[dividend][divisor] = value
            self.graph[divisor][dividend] = float(1/value)
        
        #call dfs on each query one by one
        result = []
        for query in queries:
            self.visited = set()
            if query[0] not in self.graph or query[1] not in self.graph:
                result.append(float(-1))
            else:
                answer = self.dfs(query[0], query[1])
                if not answer:
                    result.append(float(-1))
                else:
                    result.append(answer)
        return result
    
    def dfs(self,start, end):
        self.visited.add(start)

        if start == end:
            return 1
        dividend_map = self.graph[start]
        
        if end in dividend_map:
            return self.graph[start][end]
        
        mult = 0
        for node,value in dividend_map.items():
            if node in self.visited:
                continue
            mult = float(value * (self.dfs(node, end)))
            if mult != 0:
                return mult
        return 0
    
#Notes:
    #handle below case in interview
        # if divisor == 0:
        #     raise Error("Divide by zero") #zero division error

#         ["a","b"],["b","c"],["bc","cd"]
#         [["a","c"],["c","b"],["bc","cd"],["cd","bc"]["c","a"]]
#         visited = c
#         self.graph = {
            
#             a : { b : 1.5}
#             b : {a : 1/1.5, c: 2.5}
#             c : {b : 1/2.5}
#             bc : {cd : 5}
#             cd : {bc : 5}
#         }
