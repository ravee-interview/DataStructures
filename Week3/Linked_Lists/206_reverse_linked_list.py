# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #edge cases
        if not head or not head.next:
            return head
        
        prev_p = head
        curr_p = head.next
        next_p = curr_p.next #can be none
        
        while curr_p:
            curr_p.next = prev_p
            prev_p = curr_p
            curr_p = next_p
            if next_p:
                next_p = curr_p.next
            
        head.next = None
        head = prev_p
        return head
    
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
