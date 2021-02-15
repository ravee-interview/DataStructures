# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Use stack from deques
from collections import deque
class Solution(object):
    def maxDepth(self,root):
        
        if not root:
            return 0
        stack = deque() #init stack
        stack.append((root,1)) #put root on stack with depth = 1
        max_depth = 0
        #traverse and add in stack
        while stack:
            node,depth = stack.pop()
            if not node.right and not node.left:
                if depth > max_depth:
                    max_depth = depth
            if node.right:
                stack.append((node.right, depth+1))
            if node.left:
                stack.append((node.left, depth+1))
                
        return max_depth

        
        



    
    
    
    
    
    
    
    
    
    
    
    
    
    def maxDepth_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
