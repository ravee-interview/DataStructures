# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        #find the deepest leaves and call lcs on them

        stack = deque()
        stack.append((root,1)) #3
        
        parent = {root: None}
        max_depth = 0
        deepest_leaves = [] 
        while stack:
            
            node,depth = stack.pop()
            
            if not node.left and not node.right: #leaf node
                if depth == max_depth:
                    deepest_leaves.append(node)
                if depth > max_depth:
                    max_depth = depth
                    deepest_leaves = [node] #reassign deepest leaves on finding a new depth
                    
            if node.left:
                parent[node.left] = node
                stack.append((node.left,depth+1))
            if node.right:
                parent[node.right] = node
                stack.append((node.right,depth+1))
       
        
        #Now we have the deepest nodes  in [] and the parents of each node in parent in {}
        #Find the parent at each level for every leaf and check if it is equal
        #level by level, go to parents of all nodes and compare
        if len(deepest_leaves) == 1:
            return deepest_leaves[0]
        
        children = deepest_leaves
        lca = None
        while lca != root:
            lca = parent[children[0]]
            for child in children:
                if parent[child] != lca:
                    children = [parent[child] for child in children] #find common in next level
                    lca = None
                    break
            if lca:
                return lca
        return root
            
                
  # node = 3
  # depth = 1
  # max_depth = 4
  # children = [7 4]
  # lca_found = False
  # any_parent = 2
        
# parent = { root: None
#            5: 3
#            1: 3
#            0: 1
#            8: 1
#            6: 6
#            2: 5
#            7: 2
#            4: 2
          
#             }

                
#  stack = []   
    
#     9d4 0d3 1d2 3d1
#     4d4 2d3 5d2 3d1
    
    
    

        
