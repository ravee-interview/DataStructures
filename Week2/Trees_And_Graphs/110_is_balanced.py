# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(root):
            if not root:
                return True, -1
            
            left_height, is_left_balanced = helper(root.left)
            if not is_left_balanced:
                return False, 0
            right_height, is_right_balanced =  helper(root.right)
            if not is_right_balanced:
                return False, 0
            
            if abs(left_height - right_height) > 1:
                return max(left_height, right_height)+1, False
            
            return max(left_height, right_height)+1, True
        
        return helper(root)[1]
        
        


