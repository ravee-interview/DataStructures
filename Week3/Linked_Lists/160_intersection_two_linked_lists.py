# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        len_a = 0
        len_b = 0
        
        pA = headA
        pB = headB
        
        while pA:
            pA = pA.next
            len_a +=1
            
        while pB:
            pB = pB.next
            len_b +=1
        
        diff = 0
        if len_a < len_b:
            diff = len_b - len_a
            p_big = headB
            p_small = headA
        else:
            diff = len_a - len_b
            p_big = headA
            p_small = headB
        
        
        for _ in range(diff):
            p_big = p_big.next
        
        while p_small != p_big:
            p_small = p_small.next
            p_big = p_big.next
        return p_small
    
    
    """
    time complexity: o(n+m)
    space complexity: o(1)
    """
        
            
