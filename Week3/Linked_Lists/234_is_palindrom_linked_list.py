# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
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
    
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #reverse second half in place
        if not head or not head.next:
            return True
        
        slow = head
        fast = head
        while fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else: #missed test case if fast points to last node
                fast = None
                
        ptr1 = head
        ptr2 = self.reverseList(slow)
        
        while ptr2 and ptr1.val == ptr2.val:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        if ptr2:
            return False
        return True
        
        
    """
    time complexity O(n)
    space complexity o(1)
    Note: recheck for odd and even length
    
    """
