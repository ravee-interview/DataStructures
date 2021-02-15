# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        def preorder_helper(root):
            if not root:
                return result
            result.append(root.val)
            preorder_helper(root.left)
            preorder_helper(root.right)
            return result
        
        
        return preorder_helper(root)
        
