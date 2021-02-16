# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        stack = deque()
        stack.append(root)
        
        parent = {root: None}
        
        while p not in parent or q not in parent:
            
            node = stack.pop()
            
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
            
        p_ancestors = set()
        
        #add all of p's ancestors
        while p:
            p_ancestors.add(p)
            p = parent[p]
        
        
        #search for q's ancestors in dictionary which is also in p's ancestors
        while q not in p_ancestors:
            q = parent[q] #search for next parent of current q
        return q
            
        
        
        
        
        
