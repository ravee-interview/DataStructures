# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Using stack with deque: append and pop
from collections import deque
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        result = []
        #visit node, store in result, store right and left in stack
        #pop stack and repeat
        stack = deque()
        stack.append(root)
        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return result
            
    
        
    
