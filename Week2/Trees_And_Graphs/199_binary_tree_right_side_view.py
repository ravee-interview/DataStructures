# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        queue = deque()
        queue.append((root,0))
        current_level = -1
        prev_node = None
        result = []
        while queue:
            node,level = queue.popleft()
            if level != current_level:
                if prev_node:
                    result.append(prev_node.val)
                current_level = level
            prev_node = node
            if node.left:
                queue.append((node.left,level+1))
            if node.right:
                queue.append((node.right,level+1))
        result.append(prev_node.val)
        return result
                
        
        
        
        
