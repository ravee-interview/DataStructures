# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        #edge cases
        #none
        if not head:
            return None
    
        dummy_head = ListNode(-1)    
        while head and head.val == val:
            head = head.next
            
        dummy_head.next = head
        ptr = head
        while ptr and ptr.next:
            if ptr.next.val == val:
                ptr.next = ptr.next.next
            else: #also takes care of duplicates
                ptr = ptr.next
        dummy_head = None
        return head
                
