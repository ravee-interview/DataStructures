# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def add_nodes(self,carry=0,ptr1=None,ptr2=None):
        if not ptr2:
            sum_ = ptr1.val + carry
        else:
            sum_ = ptr1.val + ptr2.val + carry
        carry = sum_ / 10
        if sum_ > 9:
            sum_ = sum_ % 10    
        rptr = ListNode(sum_)
        return rptr,carry
              
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #edge cases
        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1
        
        ptr1 = l1
        ptr2 = l2
        rhead,carry = self.add_nodes(0,ptr1,ptr2) #7, 0
        ptr1 = ptr1.next
        ptr2 = ptr2.next
        rptr = rhead
        while ptr1 and ptr2:
            node,carry = self.add_nodes(carry,ptr1,ptr2)
            rptr.next = node
            rptr = rptr.next
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        while ptr1:
            node,carry = self.add_nodes(carry,ptr1)
            rptr.next = node
            rptr = rptr.next
            ptr1 = ptr1.next
        while ptr2:
            node,carry = self.add_nodes(carry,ptr2)
            rptr.next = node
            rptr = rptr.next
            ptr2 = ptr2.next
        if carry > 0:
            node = ListNode(carry)
            rptr.next = node
        return rhead

        
        """
        Time complexity: O(n+m)
        Space complexity: O(1) no extra space except for the result array which is O(max(m,n))
        head11 = 2 4 3
        head12 = 5 6 4
        
        head21 = 2
        head22 = 9
        
        head31 = 9 9
        head32 = 9 8
        
        head41 = None
        head42 = 1
        
        """
            
            
            
            
