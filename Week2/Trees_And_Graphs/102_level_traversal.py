# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Using stack as queues
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = deque()
        queue.append((root,0))
        result = []
        current_level = -1
        level_traversal = []
        while queue:
            node,level = queue.popleft()
            if level == current_level:
                level_traversal.append(node.val)
            else:
                if len(level_traversal) > 0:
                    result.append(level_traversal)
                level_traversal = []
                level_traversal.append(node.val)
                current_level = level
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        result.append(level_traversal)
        return result
