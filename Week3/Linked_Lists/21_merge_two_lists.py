# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        #ptr1 points to node such that node.next has val greater than val at ptr2
        #link ptr1.next = ptr2
        #swap ptr1 and ptr2
        
        #edge cases
        #both lists empty
        if not l1 and not l2:
            return None
        #either list empty
        if not l1:
            return l2
        if not l2:
            return l1
        #one node for each list
    
    
        ptr1 = l1
        ptr2 = l2
        new_head = l1
        #ptr2 always points to the biggervalue starting node
        if l1.val > l2.val:
            ptr1 = l2
            ptr2 = l1
            new_head = l2
        
        while ptr1 and ptr2:
            while ptr1.next and ptr1.next.val < ptr2.val:
                ptr1 = ptr1.next

            #ptr1.next now has value greater than ptr2

            temp_ptr = ptr1.next #can be none
            ptr1.next = ptr2
            ptr1 = ptr2
            ptr2 = temp_ptr
            
        return new_head
        
        
        """
        time complexity : o(n+m)
        space complxity: o(1)
        tests
        l1      1 2 3
        l2       1 2 4
        
        l1      1
        l2      1
        
        """
