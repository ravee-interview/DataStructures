# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, OrderedDict
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.node_coordinates = []
        self.BFS(root)
        self.node_coordinates.sort()
        
        
        vertical_order = OrderedDict()
        
        for column, row, value in self.node_coordinates:
            if column in vertical_order:
                vertical_order[column].append(value)
            else:
                vertical_order[column] = [value]
        return vertical_order.values()
                
        
    def BFS(self,root):
        queue = deque()
        queue.append((root,0,0))
        while queue:
            node, row, column = queue.popleft()
            if node:
                self.node_coordinates.append((column,row,node.val))
                queue.append((node.left,row+1,column-1))
                queue.append((node.right,row+1,column+1))
    
    
            
        
        
        """
        Time complexity : N log N 
        Space Complexity: O(N)
        TODO: Partition sorting version of this question
        """
